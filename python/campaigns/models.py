from django.db import models


class Campaign(models.Model):
    """ Parties are groups of users where there is a role difference between game masters and players """

    name = models.CharField(max_length=64)
    desc = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="campaigns/")

    game_masters = models.ManyToManyField("users.User", related_name="gm_campaigns")
    players = models.ManyToManyField("users.User", related_name="player_campaigns")

    def __str__(self):
        return self.name


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

    text = models.TextField()
