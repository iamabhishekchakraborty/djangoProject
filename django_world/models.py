import uuid

from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here
class Succession(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    # class Meta:
    #     abstract = True

    def __str__(self):
        return self.name


class Succession_Casts(models.Model):
    GENDER = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Other'),
    )
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    birthday = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER, blank=True)
    succession = models.ForeignKey(Succession, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Succession_Seasons(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    # seasonNum = models.AutoField(primary_key = True)
    # seasonNum = models.UUIDField(primary_key=True, default=uuid.uuid4(),editable=False)
    imdbUrl = models.URLField()
    released = models.BooleanField(default=False)
    succession = models.ForeignKey(Succession, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name


class Succession_Season_Episodes(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    episodeAirDate = models.DateField()
    partOfSeason = models.IntegerField(null=True)
    episodeNum = models.IntegerField(null=True)
    # It’s suggested, but not required, that the name of a ForeignKey field (Succession_Seasons in the example) be the name of the model, lowercase. You can call the field whatever you want
    succession_seasons = models.ForeignKey(Succession_Seasons, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    @property
    def episode_information(self):
        """returns information about a episode"""
        return '%s aired on %s is part of Season: %d' % (self.name, self.episodeAirDate, self.partOfSeason)

    # TODO: Add get_absolute_url
    def get_absolute_url(self):
        return reverse('succession_season_episodes_detail', kwargs={"pk": self.pk})
