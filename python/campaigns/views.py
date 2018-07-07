from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView

from braces.views import LoginRequiredMixin

from .forms import CampaignForm
from .models import Campaign


class CampaignOverView(CreateView):
    template_name = 'campaigns/campaigns_overview.html'
    form_class = CampaignForm

    def get_context_data(self, **kwargs):
        self.object = None
        context = super().get_context_data(**kwargs)
        context['play_campaigns'] = self.request.user.player_campaigns.all()
        context['gm_campaigns'] = self.request.user.gm_campaigns.all()
        return context

# @login_required
# def campaigns(request):
#     """Campaign overview for a user"""
#     gming = request.user.gm_campaigns.all()
#     playing = request.user.player_campaigns.all()
#     return render(request, "campaigns/campaigns_overview.html", {"playing": playing, "gming": gming})
#
#
# def campaign_create(request):
#     """ Create a new campaign """
#
#     form = CampaignForm(data=request.POST or None)
#
#     return render(request, "campaigns/campaigns_create.html", {"playing": playing, "gming": gming})