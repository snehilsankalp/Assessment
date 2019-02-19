from rest_framework import serializers
from .models import DoctorsDb, Appointment

class DoctorsDbSerializer(serializers.ModelSerializer):

    class Meta:

        model = DoctorsDb
        fields = ('url' , 'doc_name' , 'specialization' , 'location' , 'availability' , 'rating' , 'desc' )

class AppointmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Appointment
        fields = ('patient' , 'url' , 'doc_name' , )
