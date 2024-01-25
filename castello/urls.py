from django.urls import path, include
from rest_framework import routers
from castello import views

router = routers.DefaultRouter()

router.register('userform', views.UserView, basename='castello')

# router.register(prefix r'recipeform', views. Recipe View, basename='castello')

urlpatterns= [

    path('castello/', include(router.urls)),

]