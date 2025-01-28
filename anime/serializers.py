import boto3
from django.conf import settings
from rest_framework import serializers
from .models import Anime, Season, Genre, Studio, TYPES
from user.models import User
import mimetypes

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
    premiereSeason = serializers.CharField(allow_blank=True, required=False)
    genre = serializers.ListField(
        child=serializers.CharField(),
        required=False,
        allow_null=True,
        write_only=True,
        default=[],
        min_length=0
    )
    studio = serializers.CharField(write_only=True, allow_null=True, required=False)

    created_by = serializers.SerializerMethodField()
    def get_created_by(self, obj):
        return obj.created_by.name if obj.created_by else "N/A"
    

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
                  'image',
                  'created_by'
                 ]
        


    def create(self, validated_data):
        # handle data parsing
        premiere_season_str = validated_data.pop('premiereSeason', None)
        season_instance = None
        if premiere_season_str:
            season, year_str = premiere_season_str.split(" ")
            year = int(year_str)
            season_instance, created = Season.objects.get_or_create(year=year, season=season)

        prequel_instance = validated_data.pop('prequel', None)
        sequel_instance = validated_data.pop('sequel', None)

        genre_data = validated_data.pop('genre', [])

        studio_name = validated_data.pop('studio', None)
        studio_instance = None
        if studio_name:
            studio_instance, created = Studio.objects.get_or_create(name=studio_name)

        image = validated_data.pop('image', None)



        anime_instance = self.Meta.model.objects.create(premiereSeason=season_instance, studio=studio_instance, **validated_data)


        if image:
            if hasattr(image, 'file') and image.file:
                content_type = image.content_type
                if content_type.startswith("image/"):


                    s3_file_path = f"anime_images/{anime_instance.id}/{image.name}"

                    s3_client = boto3.client(
                        's3',
                        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                    )

                    try:
                        s3_client.upload_fileobj(
                            image.file,
                            settings.AWS_STORAGE_BUCKET_NAME,
                            s3_file_path,  # Correct file path including folder
                        )
                        # Set the image field on the anime instance
                        anime_instance.image = f"{s3_file_path}"
                        print(f"File uploaded successfully. Final URL: {anime_instance.image}")
                    except Exception as e:
                        print(f"Error uploading file to S3: {e}")
                else:
                    print(f"Invalid file type: {content_type}. Only image files are allowed.")
            else:
                print("No valid image file found.")
        else:
            print("No image provided.")

        # handling prequel / sequel linkage
        if prequel_instance:
            anime_instance.prequel = prequel_instance
            prequel_instance.sequel = anime_instance
            prequel_instance.save()
        if sequel_instance:
            anime_instance.sequel = sequel_instance
            sequel_instance.prequel = anime_instance
            sequel_instance.save()
        #  handle genre linkage
        if isinstance(genre_data, str):
            genre_data = genre_data.split(',')
        for genre_name in genre_data:
            genre, created = Genre.objects.get_or_create(name=genre_name)
            anime_instance.genre.add(genre)

        # save and return
        anime_instance.save()

        return anime_instance
    


    def update(self, instance, validated_data):
        # handle data parsing
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
            if instance.prequel:
                instance.prequel.sequel = None  # Unlink existing prequel
                instance.prequel.save()
            instance.prequel = None
        
        if sequel_instance:
            instance.sequel = sequel_instance
            sequel_instance.prequel = instance
            sequel_instance.save()
        else:
            if instance.sequel:
                instance.sequel.prequel = None  # Unlink existing sequel
                instance.sequel.save()
            instance.sequel = None


        genre_data = validated_data.pop('genre', [])
        if genre_data:
            genre_instances = []
            for genre_name in genre_data:
                genre_instance, _ = Genre.objects.get_or_create(name=genre_name)
                genre_instances.append(genre_instance)
            instance.genre.set(genre_instances)  # Replace genres with new set
        else:
            instance.genre.clear() 


        studio_name = validated_data.pop('studio', None)
        if studio_name:
            studio_instance, _ = Studio.objects.get_or_create(name=studio_name)
            instance.studio = studio_instance
        else:
            instance.studio = None


        # Handle image upload
        
        image = validated_data.pop('image', None)
        if image:
            # Ensure image is valid and has content
            if hasattr(image, 'file') and image.file:
                s3_file_path = f"anime_images/{instance.id}/{image.name}"
                s3_client = boto3.client(
                    's3',
                    aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                )
                try:
                    content_type = mimetypes.guess_type(image.name)[0] or 'application/octet-stream'
                    s3_client.upload_fileobj(
                        image.file,
                        settings.AWS_STORAGE_BUCKET_NAME,
                        s3_file_path,
                        ExtraArgs={'ContentType': content_type}
                    )
                    instance.image = s3_file_path
                except Exception as e:
                    print(f"Error uploading file to S3: {e}")

        # Update remaining fields
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
    