from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from . import views
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
  url(r'^admin/', admin.site.urls),
  path('',views.index,name='index'),
  path('', include(router.urls)),
  path(r'api-token-auth/', obtain_jwt_token),
  path(r'api-token-refresh/', refresh_jwt_token),
  path(r'current_user/',views.current_user),
]

