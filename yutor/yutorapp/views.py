from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import *
from .models import *



class TutorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Tutor.objects.all()
    serializer_class = TutorSerializer
    #permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    #permission_classes = [permissions.IsAuthenticated]




class TimeslotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Timeslot.objects.all()
    serializer_class = TimeslotSerializer
 #   permission_classes = [permissions.IsAuthenticated]




class TuteeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset  =Tutee.objects.all()
    serializer_class = TuteeSerializer
 #   permission_classes = [permissions.IsAuthenticated]




class RequestViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
 #   permission_classes = [permissions.IsAuthenticated]




class TransactionTableViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = TransactionTable.objects.all()
    serializer_class = TransactionTableSerializer
#    permission_classes = [permissions.IsAuthenticated]


class RequestTimeslotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = RequestTimeslot.objects.all()
    serializer_class = RequestTimeslotSerializer
#    permission_classes = [permissions.IsAuthenticated]



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

from django.http import JsonResponse
import json

def accept_request(request):
    data = json.loads(request.body)
    # do something with the your data
    
    # just return a JsonResponse
    return JsonResponse(data)