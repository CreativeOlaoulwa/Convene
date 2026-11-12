from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('tech', 'Technology'),
        ('business', 'Business'),
        ('creative', 'Creative & Design'),
        ('community', 'Community'),
        ('education', 'Education'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='tech')
    organiser = models.CharField(max_length=150, blank=True)
    venue_address = models.CharField(max_length=255, blank=True)
    image_url = models.URLField(blank=True, help_text='Link to a cover photo, e.g. from Unsplash.')
    capacity = models.IntegerField()
    banner_image = models.ImageField(upload_to='events/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def spots_left(self):
        return self.capacity - self.registrations.count()

    @property
    def is_past(self):
        return self.end_date < timezone.now()

    @property
    def percent_full(self):
        if self.capacity == 0:
            return 100
        return round((self.capacity - self.spots_left) * 100 / self.capacity)



class Session (models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ({self.event.title})"


class Registration (models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='registrations')
    registered_at = models.DateTimeField(auto_now_add=True)
    checked_in = models.BooleanField(default=False)
    checked_in_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.attendee.username} → {self.event.title}"

class Speaker(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='speakers')
    name = models.CharField(max_length=150)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='speakers/', blank=True, null=True)

    def __str__(self):
        return self.name