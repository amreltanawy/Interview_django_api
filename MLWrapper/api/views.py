from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from api.serializers import FeatureSetSerializer
from api.models import FeatureSet, PredictionResult


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


    def create(self, request, *args, **kwargs):
        """
        Create a Prediction given a set of features
        :return:
        returns a list of top 7 Predicted Product recommendations
        """
        pass
        
