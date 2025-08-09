from django.db import models

# Create your models here.
class Tweet(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='tweet_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Tweet {self.id}: {self.content[:20]}...'

    class Meta:
        ordering = ['-created_at']
