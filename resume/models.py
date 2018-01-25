from django.db import models



class Login(models.Model):
    userName=models.CharField(max_length=20)
    userEmail=models.CharField(max_length=50)
    password=models.CharField(max_length=30)


class About_Me(models.Model):
    firstName=models.CharField(max_length=200)
    middleName=models.CharField(max_length=200)
    lastName=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    #password=models.CharField(max_length=200)
    #mobile_no1=models.CharField(max_length=200)
    mobile_no=models.CharField(max_length=200)
    City=models.CharField(max_length=200)
    Street=models.CharField(max_length=200)
    State=models.CharField(max_length=200)
    Pincode=models.CharField(max_length=200)
    birthDate=models.DateField()
    objective=models.CharField(max_length=1000)
    whatIDo=models.CharField(max_length=1000)

    def __str__(self):
    	return self.email

class Home_Page(models.Model):
    proffesion=models.CharField(max_length=100)
    someIntro=models.CharField(max_length=300)

class Education(models.Model):
    degree=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    university=models.CharField(max_length=100)
    description=models.CharField(max_length=300)
    start_year=models.CharField(max_length=4)
    end_year=models.CharField(max_length=4)

class Experience(models.Model):
    employer=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    joining_date=models.DateField()
    resign_date=models.DateField()

class Projects(models.Model):
    projects_name=models.CharField(max_length=100)
    technologies=models.CharField(max_length=100)
    description=models.CharField(max_length=500)
    time_required=models.CharField(max_length=3)


# Create your models here.
