from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets

from . models import DoctorsDb, Appointment
from . serializers import DoctorsDbSerializer, AppointmentSerializer
class DoctorsDbList (viewsets.ModelViewSet):

        queryset = DoctorsDb.objects.all()
        serializer_class = DoctorsDbSerializer
        filter_backends = (SearchFilter, OrderingFilter, )
        search_fields = ('specialization', 'location')
        ordering_fields = ('rating', )

class AppointmentList (viewsets.ModelViewSet):
        queryset = Appointment.objects.all()
        serializer_class = AppointmentSerializer

# def get(self,request):
    #     doctorsdb1=DoctorsDb.objects.all()
    #     serializer=DoctorsDbSerializer(doctorsdb1, many=True)
    #     return Response(serializer.data)
