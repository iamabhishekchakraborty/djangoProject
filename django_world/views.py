from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404
from . import models
from django.template import loader
from django.views import generic


# Create your views here.
# helper function to return text or other primitive types to caller
def index(request):
    return HttpResponse("Hello, this is index from Django!!!")


def succession_season_list(request):
    succession_seasons = models.Succession_Seasons.objects.all()
    # template = loader.get_template('succession_season_list.html')
    context = {'succession_seasons': succession_seasons}             # context is a dictionary mapping template variable names to Python objects
    # return HttpResponse(template.render(context, request))
    return render(request, 'succession_season_list.html', context)


def succession_cast_list(request):
    succession_casts = models.Succession_Casts.objects.all()
    context = {'succession_casts': succession_casts}
    return render(request, 'succession_cast_list.html', context)


def succession_season_episodes_list(request, partOfSeason):
    # succession_season_episodes = get_list_or_404(models.Succession_Season_Episodes, pk=partOfSeason)
    succession_season_episodes = models.Succession_Season_Episodes.objects.filter(partOfSeason=partOfSeason).order_by('episodeAirDate')
    context = {'succession_season_episodes': succession_season_episodes}
    return render(request, 'succession_season_episode_list.html', context)


# def succession_season_episodes_list(request):
#    succession_season_episodes = models.Succession_Season_Episodes.objects.all()
#    context = {'succession_season_episodes': succession_season_episodes}
#    return render(request, 'succession_episode_list.html', context)


class SuccessionSeasonEpisodeDetailView(generic.DetailView):
    model = models.Succession_Season_Episodes
    template_name = 'succession_season_episodes_detail.html'
    context_object_name = 'succession_season_episodes'


class SuccessionSeasonEpisodeCreateView(generic.CreateView):
    model = models.Succession_Season_Episodes
    template_name = 'succession_season_episodes_form.html'
    fields = ['succession_seasons', 'name', 'description', 'episodeAirDate', 'partOfSeason', 'episodeNum']
