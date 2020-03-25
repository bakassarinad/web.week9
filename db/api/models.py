from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
# Create your models here.
    def to_json(self):
        return {
            'id':self.id,
            'name':self.name
        }
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,

        }
