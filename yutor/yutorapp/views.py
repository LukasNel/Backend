from datetime import datetime
from gcsa.conference import ConferenceSolutionCreateRequest, SolutionType
from django.http import JsonResponse
from gcsa.conference import ConferenceSolution, EntryPoint, SolutionType
from gcsa.recurrence import Recurrence, DAILY, SU, SA
from gcsa.google_calendar import GoogleCalendar, SendUpdatesMode
from gcsa.event import Event
import json
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from .models import *
gc = GoogleCalendar(credentials_path='credentials.json')


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
    queryset = Tutee.objects.all()
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
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmailSet(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """

    def post(self, request, format=None):
        """
        Return a list of all users.
        """
        data = json.loads(request.body)
        # do something with the your data
        print(data)
        # just return a JsonResponse
        request = Request.objects.get(id=data['id'])
        for ts in request.timeslots.all():
            event = Event(
                'Meeting with ' + str(request.Tutor),
                start=ts.start,
                end=ts.end,
                conference_solution=ConferenceSolutionCreateRequest(
                    solution_type=SolutionType.HANGOUTS_MEET,
                ),
                
                attendees=[request.Tutor.email, request.Tutee.email]
            )
            gc.add_event(event,send_updates =SendUpdatesMode.ALL,)
            if event.conference_solution.status == 'success':
                print(event.conference_solution.solution_id)
                ts.zoom_link = event.conference_solution.entry_points[0].uri
                ts.save()
            elif event.conference_solution.status == 'pending':
                print('Conference request has not been processed yet.')
            elif event.conference_solution.status == 'failure':
                print('Conference request has failed.')
        request.status="accepted"
        request.save()
        return Response('Successfully sent to %s and %s' % (request.Tutor.email, request.Tutee.email) )
