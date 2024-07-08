from rest_framework import serializers
from django.contrib.auth import get_user_model
from . import models
User = get_user_model()

class SendProposalSerializers(serializers.ModelSerializer):
    project = serializers.StringRelatedField()
    freelancer = serializers.StringRelatedField()
    class Meta:
        model = models.Proposal
        fields = '__all__'


