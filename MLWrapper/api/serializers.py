from rest_framework import serializers
from api.models import FeatureSet, PredictionResult



class FeatureSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureSet
        fields = '__all__'

class PredictionResultSerializer(serializers.ModelSerializer):
    feature_set = FeatureSet
    class Meta:
        model = PredictionResult
        fields = '__all__'