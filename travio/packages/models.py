from django.db import models

# Create your models here.

import uuid

from multiselectfield import MultiSelectField



class BaseClass(models.Model):

    uuid = models.UUIDField(unique=True,default=uuid.uuid4)

    active_status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True,null=True,blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:

        abstract = True



class PackageChoices(models.TextChoices):
    
        BUDGET = 'Budget', 'Budget'

        STANDARD = 'Standard', 'Standard'

        LUXURY = 'Luxury', 'Luxury'


class DestinationTypeChoices(models.TextChoices):
    
        DOMESTIC = 'Domestic', 'Domestic'

        INTERNATIONAL = 'International', 'International'


class MentorChoices(models.TextChoices):
      
      HARI = 'Hari','Hari'

      RAHUL = 'Rahul','Rahul'

      ALAN = 'Alan','Alan'



class Mentor(BaseClass):
     
    name = models.CharField(max_length=50)

    staff_no = models.TextField()

    class Meta :

        verbose_name = 'Mentors'

        verbose_name_plural = 'Mentors'


    def __str__(self):
        return self.name
    


class Package(BaseClass):

    uuid = models.UUIDField(default=uuid.uuid4,editable=False,unique=True)

    name = models.CharField(max_length=100)

    photo = models.ImageField(upload_to='packages/banner-images')

    description = models.TextField()

    start_date = models.DateField()

    destination_type = models.CharField(max_length=20,choices=DestinationTypeChoices.choices)

    duration = models.CharField(max_length=50)

    package_type = models.CharField(max_length=20,choices=PackageChoices.choices)

    # mentor = MultiSelectField(max_length=50,choices=MentorChoices.choices)

    mentor = models.ForeignKey('Mentor',on_delete=models.CASCADE)

    price = models.IntegerField()
    
    
    class Meta :

        verbose_name = 'Packages'

        verbose_name_plural = 'Packages'


    def __str__(self):

        return f'{self.name}'