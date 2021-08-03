from rest_framework.test import APITestCase
from rest_framework import status
# from ..models import LocationType, Location, DefectStatus
# from ../views import LocationTypeViewSet, LocationViewSet, DefectStatusViewSet, GroupViewSet
# import views
# from CR.ConstructionReporter import views
from ConstructionReporter import views, models


class DefectCreationTestCase(APITestCase):
    def setUp(self):
        defect_status = models.DefectStatus.objects.create(defect_status='some_status', id=1)
        location_type = models.LocationType.objects.create(location_type_name='some_type', id=1)
        defect_respondent = models.Group.objects.create(name='some_group', id=1)
        location = models.Location.objects.create(location_type=location_type)

    def test_defect_creation(self):
        data = {
                "defect_name":"sunday",
                "defect_description":"testing",
                "defect_status": 1,
                "defect_location":1,
                "defect_respondent":1
}
        response = self.client.post("/api/defects-detail/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
