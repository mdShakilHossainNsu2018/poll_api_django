from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIRequestFactory
from polls import apiviews
from rest_framework import status
from rest_framework.authtoken.models import Token


def setup_user():
    User = get_user_model()

    user = User.objects.create_user(
        'test',
        'test@gmail.com',
        'test',
    )

    return user


class TestPoll(APITestCase):
    def setUp(self) -> None:
        self.user = setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.factory = APIRequestFactory()
        self.view = apiviews.PollViewSets.as_view({'get': 'list'})
        self.uri = '/polls/'

    def test_list(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key))
        res = self.view(request)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_list2(self):
        self.client.login(username="test", password="test")

        response = self.client.get(self.uri)
        self.assertEqual(response.status_code, 200,
                         'Expected Response Code 200, received {0} instead.'.format(response.status_code))

    def test_create(self):
        self.client.login(username="test", password="test")

        params = {
            "question": "How are you?",
            "created_by": 1
        }

        response = self.client.post(self.uri, params)
        self.assertEqual(response.status_code, 201,
                         'Expected Response Code 201, received {0} instead.'
                         .format(response.status_code))
