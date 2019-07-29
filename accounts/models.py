from django.db import models

class Volunteer(models.Model):
    name = models.CharField(max_length=20)
    goingdate = models.DateTimeField('가는 날짜')
    email = models.EmailField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    addresss =models.CharField(max_length=50)

    def __str__(self):
        return self.name

class AnimalOrganization(models.Model):
    companyName = models.CharField(max_length=30)
    contact = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    hompage = models.URLField()

    def __str__(self):
        return self.companyName
# Create your models here.


CHOICE = [(1, 'male'),(2, 'female')]
STATUS_CHOICES = (
    (1, ("korea")),
    (2, ("USA")),
    (3, ("Canada"))
)
class Doginfo(models.Model):
    # dog_picture = models.ImageField(upload_to=/images, height_field=None, width_field=None, max_length=None)
    dog_name = models.CharField(max_length=20)
    dog_sex = models.BooleanField(choices=CHOICE, default=1, blank=False)
    dog_pub_date = models.DateTimeField('date published')
    # dog_description = models.TextField(max_length=200)
    # dog_nation = models.ListField()
    dog_nation = models.IntegerField(choices=STATUS_CHOICES, default=1)
    dog_adoptor_name = models.CharField(max_length=20)
    dog_adoptor_SNS = models.CharField(max_length=20)

    def __str__(self):
        return self.dog_name
