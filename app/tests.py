from django.test import TestCase
from app.models import Event

# Create your tests here.
class EventTest(TestCase):
    def setUp(self):
        Event.objects.create(title='Thanksgiving', day='2020-11-26', info='Thanksgiving dinner',image='dinner.jpg',location='Charlottesville',poster='')
    def test_event_made(self):
        Event.objects.create(title='New event', day='2020-11-24')
        ev = Event.objects.all()
        self.assertEquals(ev.__sizeof__, 2)
