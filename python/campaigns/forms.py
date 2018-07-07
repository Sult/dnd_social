from django import forms

from campaigns.models import Campaign


class CampaignForm(forms.ModelForm):
    """ Form to create or edit Campaigns. Only GMs can edit """

    class Meta:
        model = Campaign
        fields = ['name', 'desc', 'image', ]

    def save(self, *args, **kwargs):
        import pdb
        pdb.set_trace()