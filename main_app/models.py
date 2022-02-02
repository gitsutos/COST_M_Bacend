from django.db import models
from django.contrib.auth.models import User

user = User

# Create your models here.


class Costs(models.Model):
    User = models.ForeignKey(user, default=1, on_delete=models.CASCADE)
    Title = models.CharField(max_length=30)
    Description = models.CharField(null=True, max_length=500)
    Amount = models.IntegerField()
    Added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.Title)


class Family(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(
        user, through="Membership", through_fields=("family", "member"),
    )
    Created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class Membership(models.Model):
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    member = models.ForeignKey(user, related_name="inviter", on_delete=models.CASCADE)
    inviter = models.ForeignKey(
        user, on_delete=models.CASCADE, related_name="membership_invites",
    )

    def __str__(self):
        return str(self.member)
