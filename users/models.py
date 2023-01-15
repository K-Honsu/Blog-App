from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# CASCADE MEANS THAT IF THE USER IS DELETED, THEN DELELTE THE USER, BUT IF THE PROFILE IS DELETED THEN IT DOESN'T DELTE THE USER

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile' 
