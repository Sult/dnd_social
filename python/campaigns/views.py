from django.urls import reverse
from django.views import generic

from braces.views import LoginRequiredMixin, UserFormKwargsMixin

from .forms import CampaignForm
from.models import Campaign


class CampaignOverView(LoginRequiredMixin, UserFormKwargsMixin, generic.edit.CreateView):
    template_name = 'campaigns/campaigns.html'
    form_class = CampaignForm

    def get_context_data(self, **kwargs):
        self.object = None      # set object to non to create new

        context = super().get_context_data(**kwargs)
        context['campaigns'] = self.request.user.campaigns.all()
        return context

    def get_success_url(self):
        # return to newly created object
        return reverse('campaigns:campaign_details', args=(self.object.slug,))


class CampaignDetails(LoginRequiredMixin, generic.DetailView):
    template_name = 'campaigns/campaign_details.html'
    model = Campaign
