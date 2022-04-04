"""Unit tests for global diagram plugin."""
from copy import deepcopy
from django.contrib.auth import get_user_model

from django.urls import reverse

from nautobot.utilities.testing import APITestCase
from .conftest import create_site

class GlobalDiagramAPITest(APITestCase):  # pylint: disable=too-many-ancestors
    """Test the Global Diagram API."""

    def setUp(self):
        """Create a site for testing purposes"""
        super().setUp()
        self.site = create_site()

    def test_site_data(self):
        """Verify that the site has coordinates and physical address"""
        latitude = self.site.latitude
        longitude = self.site.longitude
        physical_address = self.site.physical_address
        self.assertEqual(latitude, 40.7831)
        self.assertEqual(longitude, 73.9712)
        self.assertEqual(physical_address, "Manhattan NY, USA")




