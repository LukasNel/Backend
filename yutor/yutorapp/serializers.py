from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model  # If used custom user model

from rest_framework import serializers
from .models import *

UserModel = get_user_model()


class RequestTimeslotSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestTimeslot
        fields = '__all__'






class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
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
        fields = ["timeslots", "tutor_done", "tutee_done",
                  "id", 'Tutor', 'Tutee', 'zoom_link', 'status']
class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'

class TutorSerializer(serializers.ModelSerializer):
    requests = RequestSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    rating = serializers.SerializerMethodField('get_rating')
    
    def get_rating(self, obj):
        ct = 0
        tot = 0
        for rt in obj.ratings.all():  
            ct = ct + 1
            tot=tot+rt.rating
        ct = max(1,ct)
        return tot / ct if ct > 0 else tot

    class Meta:
        model = Tutor
        fields = ['id',
                  'requests',
                  'subjects',
                  'first_name',
                  'last_name',
                  'email',
                  'picture',
                  'user',
                  'hourly_rate',
                  'rating',
                  "numRatings", 
                  'bio']


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


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'password']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
