from rest_framework.serializers import ModelSerializer
from .models import Reservation
from .models import Contact

class ReservationSerializer(ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'