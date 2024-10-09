from rest_framework import serializers
from .models import Anime, Season

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
    premiereSeason = serializers.CharField()


    class Meta:
        model = Anime
        fields = [
                  'id', 
                  'titleEnglish', 
                  'titleJpRoman', 
                  'titleJpKanji', 
                  'description', 
                  'episodes', 
                  'episodeDuration', 
                  'premiereSeason', 
                  'genre', 
                  'prequel', 
                  'sequel',
                  'demographic',
                  'airDate',
                  'endDate',
                  'aggregateRating'
                 ]

    def create(self, validated_data):

        # handling season field
        premiere_season_str = validated_data.pop('premiereSeason')
        season, year_str = premiere_season_str.split(" ")
        year = int(year_str)
        season_instance, created = Season.objects.get_or_create(year=year, season=season)
        # parsing prequel / sequel
        prequel_instance = validated_data.pop('prequel', None)
        sequel_instance = validated_data.pop('sequel', None)


        # handling primary creation
        anime_instance = self.Meta.model.objects.create(premiereSeason=season_instance, **validated_data)

        # handling prequel / sequel linkage
        if prequel_instance:
            anime_instance.prequel = prequel_instance
            prequel_instance.sequel = anime_instance
            prequel_instance.save()
        if sequel_instance:
            anime_instance.sequel = sequel_instance
            sequel_instance.prequel = anime_instance
            sequel_instance.save()

        # save and return
        anime_instance.save()
        return anime_instance