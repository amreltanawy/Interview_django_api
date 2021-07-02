from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from api.serializers import FeatureSetSerializer, PredictionResultSerializer
from api.models import FeatureSet, PredictionResult
from api.Predictor import Predictor



# Create your views here.

class PridctionViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing featureSets supplied.

    create:
    Create a Prediction.

    update:
    update an old featureset details.

    
    retrieve:
    Retrieve an existing FeatureSet with a certain id

    delete:
    Deletes a certain FeatureSet with a certain id
    """
    queryset = FeatureSet.objects.all()
    serializer_class = FeatureSetSerializer
    http_method_names = ["get", "post", "put", "delete"]

    def get_permissions(self):
        if  self.action == 'destroy':
            permission_classes = [permissions.IsAdminUser]
        else:
            if self.request.user.is_blocked:
                permission_classes = [permissions.IsAdminUser]
            else:
                permission_classes = [permissions.AllowAny]
        return [permission() for permission in permission_classes]


    @swagger_auto_schema(request_body=FeatureSetSerializer,responses={201:PredictionResultSerializer})
    def create(self, request, *args, **kwargs):
        """
        Create a Prediction given a set of features
        :return:
        returns a list of top 7 Predicted Product recommendations
        """
        serializer = FeatureSetSerializer(data=request.data)
        # change in model customer_seniority to antiguedad
        if serializer.is_valid():
            predictor_instance = Predictor()
            prediction_serializer_instance = predictor_instance.predict(serializer)
            return Response(prediction_serializer_instance.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
