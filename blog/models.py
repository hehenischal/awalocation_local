from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#model named blog that has title,desc,created_at,author, latitude,longitude
#make a table named description, that has "things to do", "best time to visit","Unique features" that will be displayed in the blog
class Description(models.Model):
    things_to_do = models.CharField(max_length=2000 ,null=True,blank=True)
    best_time_to_visit = models.CharField(max_length=50,null=True,blank=True)
    unique_features = models.CharField(max_length=50,null=True,blank=True)
    def __str__(self):
        return self.things_to_do

class Blog(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200,null=True,blank=True)
    desc = models.ForeignKey(Description, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='images/',null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author_id = models.IntegerField(null=True,blank=True)
    #category selection field with food,accomodation,cultural,historic and others as options
    choices = (
        ('Food', 'Food'),
        ('Accomodation', 'Accomodation'),
        ('Cultural', 'Cultural'),
        ('Historic', 'Historic'),
        ('Others', 'Others'),
    )
    category = models.CharField(max_length=200, choices=choices, default='Others')
    author_name = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title
