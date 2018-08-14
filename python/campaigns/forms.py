from django import forms
from braces.forms import UserKwargModelFormMixin

from campaigns.models import Campaign, CampaignMember


class CampaignForm(UserKwargModelFormMixin, forms.ModelForm):
    """ Form to create or edit Campaigns. Only GMs can edit """

    class Meta:
        model = Campaign
        fields = ['name', 'desc', 'image', ]

    def save(self, commit=True):
        campaign = super().save(commit=commit)
        CampaignMember.objects.create(member=self.user, campaign=campaign, gm=True)
        return campaign
