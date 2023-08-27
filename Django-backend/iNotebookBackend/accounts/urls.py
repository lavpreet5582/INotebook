from django.urls import include, path
from rest_framework import routers
from accounts import views
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

