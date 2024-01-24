from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    #name #designation add also
    def __str__(self):
        return self.user.username
    
class Post(models.Model):
    date = models.DateField()
    description = models.TextField(max_length=200)
    photo1 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo2 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    photo3 = models.ImageField(upload_to='post_photos/', blank=True, null=True)
    likes_received = models.IntegerField(default=0)

    def __str__(self):
        return f"Post {self.id}"
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"Comment {self.id} by {self.user.username}"