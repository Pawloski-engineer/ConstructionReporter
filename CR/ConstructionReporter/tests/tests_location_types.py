from django.test import TestCase
import json
from rest_framework.test import APITestCase
from rest_framework import status


class DefectCreationTestCase(APITestCase):
    def test_location_type_creation(self):
        data = {"location_type_name": "test location type"}
        response = self.client.post("/api/locationtype-detail/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
