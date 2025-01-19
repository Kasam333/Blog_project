from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('home')
    
    class Meta:
        ordering = ["name"]
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    title_description = models.CharField(max_length=250, default="")
    body = RichTextField(blank = True, null = True)
    #body=models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=200, default="ALL")
    post_image = models.ImageField(null=True, blank=True, upload_to="images/", default='images/default_image.jpg')

    def __str__(self):
        return f"{self.title} | {str(self.author)}"
    
    def get_absolute_url(self):
        return reverse("home")
    
class Comments(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    # Automatically set the name to the logged-in user's username
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.post.title} - {self.author.first_name}"
    
    def get_absolute_url(self):
        return reverse("home")
    
    