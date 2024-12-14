from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('agencies/', views.agency_list, name='agency_list'),
    path('agencies/<int:pk>/', views.agency_detail, name='agency_detail'),
    path('forum/', views.forum_home, name='forum_home'),
    path('forum/start/', views.start_discussion, name='start_discussion'),
    path('forum/create/', views.create_discussion, name='create_discussion'),
    path('forum/<int:discussion_id>/', views.discussion_detail, name='discussion_detail'),
    path('map/', views.map_view, name='map_view'),
    path('news/', views.news_list, name='news_list'),
    path('missions/', views.missions_list, name='missions_list'),
    path('timeline/', views.timeline_view, name='timeline_view'),
    #path('space-objects/', space_objects_view, name='space_objects'),
]
