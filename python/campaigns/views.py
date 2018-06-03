from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from campaigns.models import Campaign


@login_required
def campaigns(request):
    """Campaign overview for a user"""
    gming = request.user.gm_campaigns.all()
    playing = request.user.player_campaigns.all()
    return render(request, "campaigns/campaigns_overview.html", {"playing": playing, "gming": gming})


def campaign_create(request):
    """ Create a new campaign """

    form = CampaignForm(data=request.POST or None)

    return render(request, "campaigns/campaigns_create.html", {"playing": playing, "gming": gming})