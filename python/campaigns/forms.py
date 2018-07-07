from django import forms
from braces.forms import UserKwargModelFormMixin

from campaigns.models import Campaign


class CampaignForm(UserKwargModelFormMixin, forms.ModelForm):
    """ Form to create or edit Campaigns. Only GMs can edit """

    class Meta:
        model = Campaign
        fields = ['name', 'desc', 'image', ]

    def save(self):
        campaign = super().save()

        # creator of campaign is be default also game_master
        campaign.game_masters.add(self.user)
        return campaign
