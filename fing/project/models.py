from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return f" {self.name}"


class Project(models.Model):
    user = models.CharField(max_length=60)
    title = models.CharField(max_length=500)
    imageUrl = models.URLField(blank=True)
    date = models.DateTimeField()
    active = models.BooleanField()
    version = models.IntegerField()
    file = models.FileField(upload_to='tmp')
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    document= models.TextField()
    code = models.TextField()
    contributor = models.EmailField(max_length=30)
    
    def __str__(self):
        return f" {self.category.name}\nPosted at : {self.date}\nValue : {self.price}\nDescription : {self.description}\n"