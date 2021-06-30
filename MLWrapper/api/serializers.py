from rest_framework import serializers
from api.models import FeatureSet


class FeatureSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureSet
        fields = '__all__'
