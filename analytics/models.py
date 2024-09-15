from django.db import models

class Lead(models.Model):
    createdate = models.DateTimeField()
    email = models.EmailField()
    firstname = models.CharField(max_length=100)
    hs_object_id = models.CharField(max_length=100)
    lastmodifieddate = models.DateTimeField()
    lastname = models.CharField(max_length=100)
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.email