from rest_framework.routers import DefaultRouter
from api.views import PridctionViewSet


PREDICTION_ROUTER = DefaultRouter()
PREDICTION_ROUTER.register(r'predict', PridctionViewSet, basename='Predict')


urlpatterns =[]

urlpatterns += PREDICTION_ROUTER.urls