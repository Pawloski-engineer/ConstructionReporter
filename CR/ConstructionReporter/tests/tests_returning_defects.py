from rest_framework.test import APITestCase
from rest_framework import status


class DefectReturnTestCase(APITestCase):
    def test_returning_defects(self):
        data = {"location_type_name": "test location type"}
        response = self.client.get("/api/defects-detail/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

