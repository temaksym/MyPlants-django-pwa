from django.test import TestCase, Client
from django.contrib.auth.models import User
from app.models import Plant, UserPlant
from django.utils.timezone import now

# Test for the Plant List View
class PlantListViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = Client()

        # Create a test plant
        self.plant = Plant.objects.create(
            name="Test Plant",
            description="A test plant",
            care_instructions="Water daily",
            watering_frequency_days=1
        )

        # Create a UserPlant for the test user
        self.user_plant = UserPlant.objects.create(
            user=self.user,
            plant=self.plant,
            last_watered=now()
        )

    def test_plant_list_view_authenticated(self):
        # Log in the test user
        self.client.login(username='testuser', password='testpassword')

        # Access the plant list view
        response = self.client.get('/plants/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Plant")

    def test_plant_list_view_unauthenticated(self):
        # Access the plant list view without logging in
        response = self.client.get('/plants/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertRedirects(response, '/login/')


# Test for the UserPlant model
class UserPlantModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.plant = Plant.objects.create(
            name="Test Plant",
            description="A test plant",
            care_instructions="Water daily",
            watering_frequency_days=1
        )
        self.user_plant = UserPlant.objects.create(
            user=self.user,
            plant=self.plant,
            last_watered=now()
        )

    def test_user_plant_str(self):
        self.assertEqual(str(self.user_plant), "testuser's Test Plant")