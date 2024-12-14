from django.db import models


from django.conf import settings

DEMOGRAPHIC = [
    ('Shounen', 'Shounen'),
    ('Seinen', 'Seinen'),
    ('Shoujo', 'Shoujo'),
    ('Josei', 'Josei')
]

TYPES = [
    ('TV', 'TV'),
    ('Movie', 'Movie'),
    ('OVA', 'OVA')
]


# genre model
class Genre(models.Model):
    name = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.name

# studio model
class Studio(models.Model):
    name = models.CharField(max_length=30, unique=True)
    establishedDate = models.DateField(null=True, blank=True)
    website = models.CharField(max_length=50, unique=True, blank=True)

# season model
class Season(models.Model):
    year = models.IntegerField()
    season = models.CharField(max_length=20, choices=[
        ("Spring", "Spring"),
        ("Summer", "Summer"),
        ("Fall", "Fall"),
        ("Winter", "Winter")
    ])
    class Meta:
        unique_together = ('year', 'season')
        ordering = ['-year', 'season']

    def __str__(self):
        return f"{self.season} {self.year}"
    
# rating model
class Rating(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()

    class Meta:
        unique_together = ('user', 'anime')

    def save(self, *args, **kwargs):
        anime = self.anime
        if self.pk is None:  # If it's a new rating
            anime.rating_count += 1
            anime.total_rating += self.score
        else:  # If it's an update to an existing rating
            old_rating = Rating.objects.get(pk=self.pk)
            anime.total_rating = anime.total_rating - old_rating.score
            anime.total_rating += self.score

        super().save(*args, **kwargs)
        anime.save()
        anime.update_aggregate_rating()
        anime.save()

# Main Model
class Anime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    titleEnglish = models.CharField(max_length=255, unique=True, null=True)
    titleJpRoman = models.CharField(max_length=255, unique=True,)
    titleJpKanji = models.CharField(max_length=255, unique=True, null=True)
    description = models.CharField(max_length=1000, unique=True, null=True)
    image = models.ImageField(upload_to='anime_images/', null=True, blank=True)
    type = models.CharField(choices=TYPES, null=True)
    episodes = models.IntegerField(null=True)
    episodeDuration = models.IntegerField(null=True)
    premiereSeason = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.ManyToManyField(Genre)
    prequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='prequel_anime', null=True, blank=True)
    sequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='sequel_anime', null=True, blank=True)
    demographic = models.CharField(max_length=20, choices=DEMOGRAPHIC, null=True)
    # YYYY-MM-DD
    airDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    rating_count = models.IntegerField(default=0)
    total_rating = models.BigIntegerField(default=0)
    aggregateRating = models.FloatField(default=0)
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True, blank=True)

    def update_aggregate_rating(self):
        if self.rating_count > 0:
            self.aggregateRating = self.total_rating / self.rating_count
        else:
            self.aggregateRating = 0
        self.save()













    

    ### user based relations below ###
    #watched episodes
    #review by user
    #favorite anime function

    ### manga based relations below ###
    #manga link? consider putting characters under the manga model
    #characters? consider under manga
    #authors? under manga model
    #Source material should link to a written manga model

    #number of users that have added the anime to their list
    #rank based on where it compares to other anime ratings ?
    #user favorites feature ? under
    def __str__(self):
        return self.titleJpRoman