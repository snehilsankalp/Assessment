from django.urls import path, include
from .import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('doctors',  views.DoctorsDbList)
router.register('appointment', views.AppointmentList)

urlpatterns = [

    path('', include(router.urls))
]