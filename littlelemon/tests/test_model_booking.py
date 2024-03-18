from django.test import TestCase
from restaurant.models import Booking
from django.utils import timezone

class BookingTestCase(TestCase):
    def setUp(self):
        Booking.objects.create(name="Reserva1", no_of_guests=5)

    def test_str_representation(self):
        booking = Booking.objects.get(name="Reserva1")
        self.assertEqual(str(booking), "Reserva1")

    def test_booking_date_auto_now_add(self):
        booking = Booking.objects.get(name="Reserva1")
        # Verifica si la fecha de reserva es aproximadamente la fecha y hora actual
        self.assertAlmostEqual(booking.bookingDate, timezone.now(), delta=timezone.timedelta(seconds=10))
        # Se establece un delta de 10 segundos para permitir una pequeña diferencia entre la hora actual y la hora de reserva
