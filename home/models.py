from django.db import models
from django.contrib.auth.models import User

class AgencyProfile(models.Model):
    country_name = models.CharField(max_length=100)
    agency_name = models.CharField(max_length=100)
    overview = models.TextField()
    history = models.TextField()
    notable_missions = models.TextField()
    technological_innovations = models.TextField()
    collaborations = models.TextField()
    future_plans = models.TextField()
    flag = models.ImageField(upload_to='flags/')
    latitude = models.FloatField()
    longitude = models.FloatField()
    annual_government_spending = models.FloatField(null=True, blank=True)  # New field for government spending

    def __str__(self):
        return self.country_name

class Discussion(models.Model):
    subject = models.CharField(max_length=255)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject

class Reply(models.Model):
    discussion = models.ForeignKey(Discussion, related_name='replies', on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, default='Anonymous')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.name} on {self.created_at}'

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField()
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Mission(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField()
    date = models.DateField()

    def __str__(self):
        return self.title

class TimelineEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    media_url = models.URLField(blank=True, null=True)  # Optional media URL
    media_caption = models.CharField(max_length=200, blank=True, null=True)  # Optional media caption
    link = models.URLField(blank=True, null=True)  # Optional link for more details

    def __str__(self):
        return self.title

class SpaceObject(models.Model):
    agency_profile = models.ForeignKey(AgencyProfile, on_delete=models.CASCADE)
    international_designator = models.CharField(max_length=50, blank=True)
    national_designator = models.CharField(max_length=50, blank=True)
    name_of_space_object = models.CharField(max_length=100)
    state_organization = models.CharField(max_length=100)
    date_of_launch = models.DateField(blank=True, null=True)
    gso_location = models.CharField(max_length=100, blank=True)
    un_registered = models.CharField(max_length=10, blank=True)
    registration_document = models.CharField(max_length=100, blank=True)
    other_documents = models.TextField(blank=True)
    status = models.CharField(max_length=50, blank=True)
    date_of_decay_or_change = models.DateField(blank=True, null=True)
    function_of_space_object = models.TextField(blank=True)
    secretariats_remarks = models.TextField(blank=True)
    external_website = models.URLField(blank=True)

    def __str__(self):
        return f"{self.name_of_space_object} ({self.state_organization})"
