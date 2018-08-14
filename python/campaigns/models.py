import uuid
from django.db import models
from django.utils.translation import gettext as _

from utils.helpers import get_unique_slug


class Campaign(models.Model):
    """ Parties are groups of users where there is a role difference between game masters and players """

    name = models.CharField(_("name"), max_length=64)
    slug = models.SlugField(unique=True)
    desc = models.TextField(_("description"), null=True, blank=True)
    image = models.ImageField(_("image"), upload_to="campaigns/", null=True, blank=True)

    members = models.ManyToManyField('users.User', through="campaigns.CampaignMember", related_name="campaigns")

    # used for enabling sharing link
    share = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(self, 'name', 'slug')
        super().save(*args, **kwargs)

    @property
    def image_url(self):
        return self.image.url if self.image else "/static/campaigns/campaign-party.jpg"

    @property
    def players(self):
        return self.members.filter(member__gm=False)

    @property
    def game_masters(self):
        return self.members.filter(member__gm=True)


class CampaignMember(models.Model):
    """M2M between users and campaigns to keep track of their member status and more"""

    campaign = models.ForeignKey('campaigns.Campaign', related_name='member', on_delete=models.CASCADE)
    member = models.ForeignKey('users.User', related_name='member', on_delete=models.CASCADE)

    gm = models.BooleanField(default=False)


class Handout(models.Model):
    """
    Link objects to players in a party. Users in received have access to the handout
    any game master from the party can handout and change who has access 
    """

    NPC = 1
    ITEM = 2
    TEXT = 3
    CATEGORIES = (
        (NPC, "NPC"),
        (ITEM, "Item"),
        (TEXT, "Text"),
    )
    category = models.PositiveSmallIntegerField()
    campaign = models.ForeignKey("campaigns.Campaign", related_name="handouts", on_delete=models.CASCADE)
    received = models.ManyToManyField("users.User", related_name="player_handouts")

    name = models.CharField(_("name"), max_length=64)
    text = models.TextField()
