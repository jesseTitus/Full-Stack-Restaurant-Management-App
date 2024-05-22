from django.test import TestCase
from myapp.models import Booking
from datetime import datetime, time, date
from django.contrib.auth.models import User
# Create your tests here.

class BookingModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='12345')
        cls.reservation = Booking.objects.create(
            customer=cls.user,
            name = "john mcdonald",
            date = date(2023, 5, 21),
            time=time(19, 30),
            guests=4
        )

    def test_fields(self):
        self.assertIsInstance(self.reservation.customer, User)
        self.assertEqual(self.reservation.name, "john mcdonald")
        self.assertEqual(self.reservation.date, date(2023, 5, 21))
        self.assertEqual(self.reservation.time, time(19, 30))
        self.assertEqual(self.reservation.guests, 4)

    def test_timestamps(self):
        self.assertIsInstance(self.reservation.created_at, datetime)
        self.assertIsInstance(self.reservation.updated_at, datetime)
        