from django.urls import path

from campaigns import views


app_name = 'campaigns'
urlpatterns = [
    path('', views.campaigns, name='overview'),
]
