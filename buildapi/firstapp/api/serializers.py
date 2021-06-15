from rest_framework import serializers
from firstapp.models import Note



class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"