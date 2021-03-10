from django.db import models

# ORM Maping.

class Service(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    image=models.ImageField(upload_to='ServicesApp')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    # Name that will have this service in the DB
    class Meta:
        verbose_name='service'
        verbose_name_plural='services'

    def __str__(self):
        return self.title