from django.db import models

class User(models.Model):
    fName = models.CharField(max_length=50)
    lName = models.CharField(max_length=50)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mNumber = models.IntegerField()

    class Meta:
        db_table = "auth_table"