"""Urls for diagram."""

from django.urls import path

from nautobot_circuit_diagram_plugin import views

app_name = "nautobot_circuit_diagram_plugin"

urlpatterns = [
    path("sites/ajax-data/", views.load_site_coordinates, name='load-sites'),
    path("org-map/", views.world_map_view, name='world-map-view'),
]