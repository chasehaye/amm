from django.db import models

#field inputs for anime model
def generate_seasons(start_year=1970, end_year=2070):
    seasons = ["Spring", "Summer", "Fall", "Winter"]
    return [(f"{season} {year}", f"{season} {year}") for year in range(start_year, end_year + 1) for season in seasons]
SEASONS = generate_seasons()

# Create your models here.

class Anime(models.Model):
    titleEnglish = models.CharField(unique=True)
    titleJpRoman = models.CharField(unique=True)
    titleJpKanj = models.CharField(unique=True)

    description = models.CharField(unique=True)

    prequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='sequel_anime', null=True, blank=True)
    sequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='prequel_anime', null=True, blank=True)

    #studio should be linked to another model
    #global variable calculation rating calc
    #img?

    #user rating?
    #user review

    #adaptation link to anime

    #array of options
    genre = models.CharField(unique=True)
    demographic = models.CharField(unique=True)
    animeType = models.CharField(unique=True)
    
    episodes = models.IntegerField()
    episodesWatched = models.IntegerField()
    episodeDuration = models.IntegerField()


    premireSeason = models.CharField(max_length=20, choices=SEASONS)
    airDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)


