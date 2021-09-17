from rest_framework  import serializers
from .models import details


class Appser(serializers.ModelSerializer):
    class Meta:
        model = details
        fields = ('id','Name','Contact','Place')