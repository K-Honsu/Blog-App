from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    
    def __str__(self):
        return self.title