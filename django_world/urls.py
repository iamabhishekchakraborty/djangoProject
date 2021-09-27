from django.urls import path
from . import views

app_name = 'django_world'
# this is a tuple where the views and URLs are connected or mapped
urlpatterns = [
    path('', views.index, name='index'),
    # the 'name' value as called by the {% url %} template tag
    path('Seasons', views.succession_season_list, name='succession_seasons'),
    path('Casts', views.succession_cast_list, name='succession_casts'),
    # path('Episodes', views.succession_season_episodes_list, name='succession_season_episodes'),
    path('succession_season_episodes/<int:partOfSeason>', views.succession_season_episodes_list, name='succession_season_episodes'),
    path('succession_season_episodes_detail/<int:pk>', views.SuccessionSeasonEpisodeDetailView.as_view(), name='succession_season_episodes_detail'),
    path('succession_season_episodes/register', views.SuccessionSeasonEpisodeCreateView.as_view(), name='succession_season_episodes_register'),
]
