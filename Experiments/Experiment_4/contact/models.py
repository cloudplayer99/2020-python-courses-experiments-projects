from django.db import models

# Create your models here.


class People(models.Model):
    name_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('data published')

    def __str__(self):
        return self.name_text


class Phone(models.Model):
    People = models.ForeignKey(People, on_delete=models.CASCADE)
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number


class Address(models.Model):
    People = models.ForeignKey(People, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address
