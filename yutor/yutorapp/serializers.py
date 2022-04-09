from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Tutor
class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'

