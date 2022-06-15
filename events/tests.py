from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import eventModels

class eventTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model.objects.create_user(username="testuser", email = "test@email.com", password = "password" )
        cls.eventModels = eventModels.obejects.create(title= "New", date = "1/1/2020", eventDescription = "test description", location = "somewhere")
    
    
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
      
        def test_updateEvent(self):
            response = self.client.post(
            reverse("update", args = 1),
            {
                "title": "Updated Title",
                "location": "Middle Earth"
            }

            )

            self.assertEquals(response.status_code, 302)
            self.assertEquals(eventModels.objects.last().title(), "Updated Title")

        def test_deleteEvent(self):
            response = self.client.post("delete", args = 1)
            self.assertEquals(response.status_code, 302) 

      
      
      
      
      
        # Create your tests here.
