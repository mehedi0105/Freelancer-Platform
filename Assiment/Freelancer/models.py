from django.db import models
from django.contrib.auth import get_user_model
from Buyers.models import AddJob
User = get_user_model()

# Create your models here.
class Proposal(models.Model):
    project = models.ForeignKey(AddJob, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)
    proposal_text = models.TextField()

    def __str__(self):
        return self.freelancer.username