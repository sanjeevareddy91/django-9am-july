from rest_framework.serializers import ModelSerializer
from .models import Team_Info

class TeamInfoSerializer(ModelSerializer):
    class Meta:
        model = Team_Info
        fields = "__all__"