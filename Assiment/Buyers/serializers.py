from rest_framework import serializers
from . import models

class AddPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.AddJob
        fields = '__all__'

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Reveiw
        fields = '__all__'