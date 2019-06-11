"""ufunction URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from application.api.views.GoalView import GoalViewSet
from application.api.views.ActionView import ActionViewSet
from application.api.views.IntentionView import IntentionViewSet
from application.api.views.MeasurementView import MeasurementViewSet
from application.api.views.ReviewView import ReviewViewSet
from application.api.views.RewardView import RewardViewSet
from application.api.views.GoalProgressView import GoalProgressViewSet

router = routers.DefaultRouter()
router.register('goals', GoalViewSet)
router.register('actions', ActionViewSet)
router.register('intentions', IntentionViewSet)
router.register('measurements', MeasurementViewSet)
router.register('reviews', ReviewViewSet)
router.register('rewards', RewardViewSet)

router.register(r'progress', GoalProgressViewSet, basename='progress')


urlpatterns = [
    url('', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls')),
]
