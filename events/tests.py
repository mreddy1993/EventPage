from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import eventModels

class eventTests(TestCase):
    @classmethod
    
    def test_Event_Content(self):
        def test_createEvent(self):
            response = self.client.post(
                reverse("create"),
                {
                    "title": "test1",
                    "date": "1/2/2022",
                    "eventDescription": "test description",
                    "location": "Narnia"
                }   
            )
            self.assertEquals(response.status_code, 302)
            self.assertEquals(eventModels.objects.last().title(),"test1")
      
      
      
      
      
      
        # Create your tests here.
