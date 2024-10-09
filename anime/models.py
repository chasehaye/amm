from django.db import models


from django.conf import settings

# fields for main model
GENRE_CHOICES = [
('Action', 'Action'),
('Adventure', 'Adventure'),
('Comedy', 'Comedy'),
('Drama', 'Drama'),
('Fantasy', 'Fantasy'),
('Horror', 'Horror'),
('Romance', 'Romance'),
('Sci-Fi', 'Sci-Fi')
]

DEMOGRAPHIC = [
    ('Shonen', 'Shonen'),
    ('Seinen', 'Seinen'),
    ('Shojo', 'Shojo')
]


# sub models
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
    
# finish
class Rating(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    anime = models.ForeignKey('Anime', on_delete=models.CASCADE)
    score = models.IntegerField()
    class Meta:
        unique_together = ('user', 'anime')
    def save(self, *args, **kwargs):
        anime = self.anime
        if self.pk is None:  # Only if it's a new rating
            anime.rating_count += 1
            anime.total_rating += self.score
            anime.update_aggregate_rating()

        super().save(*args, **kwargs)
#  finish

# Main Model
class Anime(models.Model):


    titleEnglish = models.CharField(max_length=255, unique=True)
    titleJpRoman = models.CharField(max_length=255, unique=True, null=True)
    titleJpKanji = models.CharField(max_length=255, unique=True, null=True)

    description = models.CharField(max_length=255, unique=True, null=True)

    episodes = models.IntegerField()
    episodeDuration = models.IntegerField()
    
    premiereSeason = models.ForeignKey(Season, on_delete=models.SET_NULL, null=True, blank=True)
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)

    prequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='prequel_anime', null=True, blank=True)
    sequel = models.ForeignKey('self', on_delete=models.SET_NULL, related_name='sequel_anime', null=True, blank=True)

    demographic = models.CharField(max_length=20, choices=DEMOGRAPHIC)

    # YYYY-MM-DD
    airDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)

    rating_count = models.IntegerField(default=0)
    total_rating = models.IntegerField(default=0)
    aggregateRating = models.FloatField(default=0)

    def update_aggregate_rating(self):
        if self.rating_count > 0:
            self.aggregateRating = self.total_rating / self.rating_count
        else:
            self.aggregateRating = 0
        self.save()


    #rating
    #watched episodes
    #rating by user
    #global rating
    #review by user

    #studio that made the anime model
    #Source material should link to a written manga model
    #img that links to something like aws
    #number of users that have added the anime to their list
    #rank based on where it compares to other aniem ratings
    #user favorites feature
    def __str__(self):
        return self.titleEnglish