from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
# from django.urls import reverse


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]
    #
    # def get_absolute_url(self):  # hei hi post zawh veleh a, a luh leh na tur a ni
    #     return reverse('blog-home')  # homepage a luh nghalna.
    #     #  return reverse('post-detail', kwargs={'pk': self.pk})  # hei hi kan thil post zawh chiah a luh nghalna.
