from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *


class RequestTimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTimeslot
        fields = '__all__'


class RequestSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        kwargs['partial'] = True
        super(RequestSerializer, self).__init__(*args, **kwargs)
    timeslots = RequestTimeslotSerializer(many=True)

    def create(self, validated_data):
        tracks_data = validated_data.pop('timeslots')
        print(tracks_data)
        print(validated_data)
        request = Request.objects.create(**validated_data)
        for track_data in tracks_data:
            RequestTimeslot.objects.create(request=request, **track_data)
        return request
   
    class Meta:
        model = Request
        fields = ["timeslots","tutor_done","tutee_done","id",'Tutor','Tutee','zoom_link', 'status']


class TutorSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True, read_only=True)

    class Meta:
        model = Tutor
        fields = ['id','requests','first_name','last_name','email','picture','user','hourly_rate','rating', "numRatings",'bio']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class TimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeslot
        fields = '__all__'


class TuteeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutee
        fields = '__all__'


class TransactionTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionTable
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
