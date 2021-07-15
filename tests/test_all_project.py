from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from pokemon.models import Pokemon
from pokemon.services import get_detail_pokemon


class BaseTest(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_profile = reverse("pokemon_app:user_profile")
        self.test_pok = Pokemon(name= "pok1",
                                id=10000,  #It's Over 9000!
                                weight=100,
                                height= 165,
                                base_happiness= 55,
                                image="image_url",
                                capture_rate= 68,
                                has_gender_differences= False,
                                is_baby= False,
                                is_legendary= True,
                                is_mythical= True,
                                is_playing= False,).save()

        self.test_user = User(username="pok1",
                             password="testuser1111",
                             email="testuser@gmail.com",
                             ).save()
        self.user = {
            'username': 'testuser1010',
            'email': 'testemail@gmail.com',
            'password1': 'user1111',
            'password2': 'user1111',
        }
        self.user_login = {
            'username': 'testuser1010',
            'password': 'user1111',
        }
        self.user_incorrect_login = {
            'username': 'testuser1010',
            'password': 'user1110',
        }
        self.user_short_password = {
            'email': 'testemail@gmail.com',
            'username': 'user_name',
            'password1': '1',
            'password2': '1',
        }
        self.user_unmatching_password = {
            'email': 'testemail@gmail.com',
            'username': 'user_name',
            'password1': 'pass',
            'password2': 'paww',
        }

        self.user_invalid_email = {
            'email': 'surely_not_email',
            'username': 'user_name',
            'password1': 'pass',
            'password2': 'paww',
        }

        self.user_no_email = {
            'email': 'surely_not_email',
            'username': 'user_name',
            'password1': 'pass',
            'password2': 'paww',
        }
        self.choose_data = {
            'catch': 'Поймать!',
            'pokeid': '10000',
        }
        return super().setUp()


class RegisterTest(BaseTest):
    def test_can_view_register_page_correctly(self):
        """ Test to check if user can see correct register page """
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register/register.html')

    def test_can_register_user(self):
        """ Test to check if user can register with valid data """
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_cant_register_user_with_short_password(self):
        """ Test to check if user can register with too short password """
        response = self.client.post(self.register_url, self.user_short_password, format='text/html')
        self.assertNotEqual(response.status_code, 302)

    def test_cant_register_user_with_unmatching_passwords(self):
        """ Test to check if user can register with different password1 and password2 """
        response = self.client.post(self.register_url, self.user_unmatching_password, format='text/html')
        self.assertNotEqual(response.status_code, 302)

    def test_cant_register_user_with_invalid_email(self):
        """ Test to check if user can register with invalid email """
        response = self.client.post(self.register_url, self.user_invalid_email, format='text/html')
        self.assertNotEqual(response.status_code, 302)

    def test_cant_register_user_with_no_email(self):
        """ Test to check if user can register without email """
        response = self.client.post(self.register_url, self.user_invalid_email, format='text/html')
        self.assertNotEqual(response.status_code, 302)

    def test_cant_register_user_with_taken_name_or_email(self):
        """ Test to check if two users can have the came name/email """
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.register_url, self.user, format='text/html')
        self.assertNotEqual(response.status_code, 302)


class LogInTest(BaseTest):
    def test_can_view_login_page_correctly(self):
        """ Test to check if user can see correct login page """
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')


    def test_can_login_user(self):
        """ Test to check if user can login with valid data """
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.user_login, format='text/html')
        self.assertEqual(response.status_code, 302)

    def test_can_login_user_with_invalid_data(self):
        """ Test to check if user can login with invalid data """
        self.client.post(self.register_url, self.user, format='text/html')
        response = self.client.post(self.login_url, self.user_incorrect_login, format='text/html')
        self.assertNotEqual(response.status_code, 302)


class PokemonChooseTest(BaseTest):

    def test_can_view_profile_page_correctly(self):
        """ Test to check if user can see correct profile page """
        self.client.post(self.register_url, self.user, format='text/html')
        self.client.post(self.login_url, self.user_login, format='text/html')
        response = self.client.get(self.user_profile)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'sitetemplates/profile.html')

    def test_can_choose_pokemon(self):
        """ Test to check if user can see correct profile page """
        Pokemon(name="pok1",
                id=10000,  # It's Over 9000!
                weight=100,
                height=165,
                base_happiness=55,
                image="image_url",
                capture_rate=68,
                has_gender_differences=False,
                is_baby=False,
                is_legendary=True,
                is_mythical=True,
                is_playing=False, ).save()

        self.client.post(self.register_url, self.user, format='text/html')
        self.client.post(self.login_url, self.user_login, format='text/html')
        self.client.post(self.user_profile, self.choose_data, format='text/html')
        p = Pokemon.objects.get(id=10000)
        self.assertEqual(p.user.first().username, self.user_login["username"])

class GetDetailPokemonAPITest(BaseTest):

    def test_can_get_detail_pokemon(self):
        """ Test to check if there is a possibility to get info about pokemon via PokeAPI  """
        res = get_detail_pokemon(1)
        self.assertEqual(res["name"], "bulbasaur")
