"""yutor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.urls import path
from rest_framework import routers
from yutorapp.views import *
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token  # <-- Here


router = routers.DefaultRouter()
router.register(r'tutors', TutorViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'requests', RequestViewSet)
router.register(r'ratings', RatingViewSet)
router.register(r'timeslots', TimeslotViewSet)
router.register(r'requesttimeslots', RequestTimeslotViewSet)
router.register(r'tutees', TuteeViewSet)
router.register(r'transactions', TransactionViewSet)

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),    
    path('accept_request/', EmailSet.as_view()),
    path('check_tutor/', CheckTutor.as_view()),
    path('finalize_request/', FinalizeReview.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)