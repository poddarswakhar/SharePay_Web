from rest_framework import serializers
from block.models import Group


class GroupSerializers(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
