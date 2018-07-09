from django.urls import path

from . import views


app_name = 'campaigns'
urlpatterns = [
    path('', views.CampaignOverView.as_view(), name='campaigns'),
    path('<slug:slug>', views.CampaignView.as_view(), name='campaign_details')
]
