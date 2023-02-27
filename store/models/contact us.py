from django.db import models


class Contactus(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=25)
    message = models.CharField(max_length=50)
   
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
           return Customer.objects.get(email=email)
        except:
            return False

            
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
