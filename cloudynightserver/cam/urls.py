"""Licensed under a 3-clause BSD style license - see LICENSE.rst

This file is part of
cloudynight (c) Michael Mommert (mommermiscience@gmail.com), 2020

This file can be copied directly into your Django project.
"""
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Labeled', views.LabeledViewSet)
router.register(r'Unlabeled', views.UnlabeledViewSet)
router.register(r'Subregion', views.SubregionViewSet)

urlpatterns = [
    # actual pages
    path('', views.projectHome.as_view()),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data/', include(router.urls)),
    path('label/', views.labeler),
    path('check/', views.checker),
    # API data retrieval tools
    path('predictLatestUnlabeled/', views.predictLatestUnlabeled),
    path('getAllUnlabeled/', views.getAllUnlabeled),
    path('getAllLabeled/', views.getAllLabeled),
    path('getRandomUnlabeled/', views.getRandomUnlabeled),
    path('getLatestUnlabeled/', views.getLatestUnlabeled),
    # interface for manual labeling
    path('assignLabels/', views.assignLabels),

]
