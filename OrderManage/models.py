from django.db import models

# Create your models here.


class Costumers(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50, verbose_name='Address')
    mail = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=30)
    section = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return 'Article: %s, Section: %s, Price: %s' % (self.name, self.section, self.price)


class Orders(models.Model):
    number = models.IntegerField()
    date = models.DateField()
    received = models.BooleanField()
