from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *
class TutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutor
        fields = '__all__'


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TimeslotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeslot
        fields = '__all__'

class TuteeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tutee
        fields = '__all__'

class RequestSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Request
        fields = '__all__'

class TransactionTableSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransactionTable
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']