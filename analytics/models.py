from django.db import models

class Lead(models.Model):
    hubspot_id = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True, blank=True)
    company = models.CharField(max_length=255, null=True, blank=True)
    lead_status = models.CharField(max_length=100)
    created_at = models.DateTimeField()

    def __str__(self):
        return self.name


class Interaction(models.Model):
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)  
    interaction_date = models.DateTimeField()
    notes = models.TextField()

    def __str__(self):
        return f"{self.type} with {self.lead.name}"
