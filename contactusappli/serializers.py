from rest_framework import serializers
from contactusappli.models import Contact

class ContactusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ('id', 'name', 'email', 'number', 'subject')