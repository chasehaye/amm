import boto3
from django.conf import settings
from rest_framework import serializers
from .models import Anime, Season, Genre, Studio

class AnimeAbbrvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = ['id', 'titleEnglish', 'titleJpRoman', 'image']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['id', 'name']

class StudioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = ['id', 'name', 'establishedDate', 'website']

class AnimeSerializer(serializers.ModelSerializer):
    #  pre/se field
    prequel = serializers.PrimaryKeyRelatedField(
        queryset=Anime.objects.all(),
        allow_null=True,
        required=False
    )
    sequel = serializers.PrimaryKeyRelatedField(
        queryset=Anime.objects.all(),
        allow_null=True,
        required=False
    )
    # season field
    premiereSeason = serializers.CharField(allow_null=True)
    # genre field
    genre = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        allow_null=True
    )
    # studio field
    studio = serializers.CharField(write_only=True, allow_null=True)
    

    class Meta:
        model = Anime
        fields = [
                  'id', 
                  'titleEnglish', 
                  'titleJpRoman', 
                  'titleJpKanji', 
                  'description',
                  'type',
                  'episodes', 
                  'episodeDuration', 
                  'premiereSeason',  
                  'genre',
                  'prequel', 
                  'sequel',
                  'demographic',
                  'airDate',
                  'endDate',
                  'aggregateRating',
                  'studio',
                  'created_at',
                  'updated_at',
                  'image'
                 ]

    def create(self, validated_data):
        image = validated_data.pop('image', None)

        # handling season field
        premiere_season_str = validated_data.pop('premiereSeason', None)
        season_instance = None
        if premiere_season_str:
            season, year_str = premiere_season_str.split(" ")
            year = int(year_str)
            season_instance, created = Season.objects.get_or_create(year=year, season=season)


        # parsing prequel / sequel
        prequel_instance = validated_data.pop('prequel', None)
        sequel_instance = validated_data.pop('sequel', None)


        # handling genre
        genres_data = validated_data.pop('genre', [])
        genre_instances = []
        if genres_data:
            for genre_data in genres_data:
                genre_instance, created = Genre.objects.get_or_create(name=genre_data)
                genre_instances.append(genre_instance)


        # handling studio
        studio_name = validated_data.pop('studio', None)
        studio_instance = None
        if studio_name:
            studio_instance, created = Studio.objects.get_or_create(name=studio_name)

        # handling primary creation
        anime_instance = self.Meta.model.objects.create(premiereSeason=season_instance, studio=studio_instance, **validated_data)


        if image:
            # Initialize S3 client
            s3_client = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            # Ensure image is valid and has content
            if hasattr(image, 'file') and image.file:
                s3_file_path = f"anime_images/{anime_instance.id}/{image.name}"
                s3_client.upload_fileobj(
                    image.file,
                    settings.AWS_STORAGE_BUCKET_NAME,
                    s3_file_path,
                    ExtraArgs={'ContentType': image.content_type}
                )
                anime_instance.image = f"{s3_file_path}"

        # handling prequel / sequel linkage
        if prequel_instance:
            anime_instance.prequel = prequel_instance
            prequel_instance.sequel = anime_instance
            prequel_instance.save()
        if sequel_instance:
            anime_instance.sequel = sequel_instance
            sequel_instance.prequel = anime_instance
            sequel_instance.save()
        #  handling genre linkage
        anime_instance.genre.set(genre_instances)

        # save and return
        anime_instance.save()
        return anime_instance
    


    def update(self, instance, validated_data):
        premiere_season_str = validated_data.pop('premiereSeason', None)
        if premiere_season_str:
            season, year_str = premiere_season_str.split(" ")
            year = int(year_str)
            season_instance, _ = Season.objects.get_or_create(year=year, season=season)
            instance.premiereSeason = season_instance
        else:
            instance.premiereSeason = None

        prequel_instance = validated_data.pop('prequel', None)
        sequel_instance = validated_data.pop('sequel', None)
        # Prevent linkage to parent
        if prequel_instance == instance:
            prequel_instance = None
        if sequel_instance == instance:
            sequel_instance = None

        if prequel_instance:
            instance.prequel = prequel_instance
            prequel_instance.sequel = instance
            prequel_instance.save()
        else:
            instance.prequel = None  # Remove existing prequel if not provided
        
        if sequel_instance:
            instance.sequel = sequel_instance
            sequel_instance.prequel = instance
            sequel_instance.save()
        else:
            instance.sequel = None  # Remove existing sequel if not provided

        # Handle genres
        genres_data = validated_data.pop('genre', [])
        genre_instances = []
        for genre_data in genres_data:
            genre_instance, _ = Genre.objects.get_or_create(name=genre_data)
            genre_instances.append(genre_instance)
        if genre_instances:
            instance.genre.set(genre_instances)
        else:
            instance.genre.clear()

        # Handle studio
        studio_name = validated_data.pop('studio', None)
        if studio_name:
            studio_instance, _ = Studio.objects.get_or_create(name=studio_name)
            instance.studio = studio_instance
        else:
            instance.studio = None


        # Handle image upload
        image = validated_data.pop('image', None)
        if image:
            s3_client = boto3.client(
                's3',
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
            )
            # Ensure image is valid and has content
            if hasattr(image, 'file') and image.file:
                s3_file_path = f"anime_images/{instance.id}/{image.name}"
                s3_client.upload_fileobj(
                    image.file,
                    settings.AWS_STORAGE_BUCKET_NAME,
                    s3_file_path,
                    ExtraArgs={'ContentType': image.content_type}
                )
                instance.image = f"{s3_file_path}"

        # Update the remaining fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Save and return the updated instance
        instance.save()
        return instance



    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genre'] = [genre.name for genre in instance.genre.all()]
        if instance.studio:
            representation['studio'] = {
                'name': instance.studio.name
            }
        else:
            representation['studio'] = None
        return representation
    