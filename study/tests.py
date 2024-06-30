from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase, APIClient

from .models import Study


class StudyTestCase(APITestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.study = Study.objects.create(name='test', serial=1, description='test_description')

    def test_list_study(self):
        response = self.client.get(
            reverse('study_:study_list'),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            [{
                "id": self.study.pk,
                "name": self.study.name,
                "serial": self.study.serial,
                "description": self.study.description
            }]
        )

    def test_create_study(self):
        data = {
            "name": "test2",
            "serial": 2,
            "description": "test_description2",
        }
        response = self.client.post(reverse('study_:study_create'), data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.json(),
                         {
                             "id": 2,
                             "name": "test2",
                             "serial": 2,
                             "description": "test_description2"
                         }
                         )

    def test_retrieve_study(self):
        response = self.client.get(
            reverse('study_:study_retrieve', kwargs={'pk': self.study.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {
                             'id': self.study.pk,
                             'name': self.study.name,
                             'serial': self.study.serial,
                             'description': self.study.description
                         }
                         )

    def test_update_study(self):
        data = {
            "name": "test2",
            "serial": 2,
            "description": "test_description2",
        }
        response = self.client.patch(
            reverse('study_:study_update', kwargs={'pk': self.study.pk}),

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(response.json(),
                         {
                             'id': self.study.pk,
                             'name': "test2",
                             'serial': 2,
                             'description': "test_description2"
                         }
                         )

    def test_delete_study(self):
        response = self.client.delete(
            reverse('study_:study_delete', kwargs={'pk': self.study.pk}),
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
