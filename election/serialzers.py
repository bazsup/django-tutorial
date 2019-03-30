from rest_framework import serializers
from election.models import Party


class PartySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ('id', 'name', 'description')