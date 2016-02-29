from django.db import models

class User(models.Model):
    name = models.CharField(max_length=4096)
    email_address = models.CharField(max_length=8192)
    
    def __str__(self):
        return self.name + ': ' + self.email_address
    

class UsualHours(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    day_name = models.CharField(max_length=10)
    start_time = models.CharField(max_length=5)
    end_time = models.CharField(max_length=5)

    def __str__(self):
        return self.user.name + ': ' + self.day_name + ' from: ' + self.start_time + ' to: ' + self.end_time
