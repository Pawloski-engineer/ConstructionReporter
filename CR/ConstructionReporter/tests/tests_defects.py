from django.test import TestCase
import json
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Defect
from .models import DefectSerializer


class DefectCreationTestCase(APITestCase):
    def test_defect_creation(self):
        data = {"defect_name": "test", "defect_description": "testing", "defect_status": 1,
                "defect_location": 1, "defect_respondent": 1}
        response = self.client.post("/api/defects-detail/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
