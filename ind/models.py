from django.contrib.auth.models import User

from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255, default="Default Designation")

    def __str__(self):
        return self.user.username

    
class Member(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200,blank = False)
    # image1 = models.ImageField(upload_to='images/',blank =True)
    # image2 = models.ImageField(upload_to='images/',blank=True)
    # image3 = models.ImageField(upload_to='images/',blank = True)

    # def __str__(self):
    #     return f"Member {self.id}"
    
# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     comment = models.TextField()

#     def __str__(self):
#         return f"Comment {self.id} by {self.user.username}"