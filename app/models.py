from django.db import models
from datetime import timedelta


class Plant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='plants/')
    care_instructions = models.TextField()
    watering_frequency_days = models.IntegerField(default=7)

    def __str__(self):
        return self.name
    

class UserPlant(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s {self.plant.name}"
    
    def get_next_watering_date(self):
        return self.date_added + timedelta(days=self.plant.watering_frequency_days)
    

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CareNotification(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    message = models.TextField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)

    def mark_as_complete(self):
        self.is_complete = True
        self.save()
        # Here you would typically send a notification to the user

    def send_notification(self):
        # Logic to send notification to the user
        pass

    def __str__(self):
        return f"Notification for {self.user.username}"
    

