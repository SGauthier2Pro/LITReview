from django.db import models
from django.conf import settings
from PIL import Image
from django.core.validators import MinValueValidator, MaxValueValidator


class Ticket(models.Model):
    title = models.CharField(max_length=128, verbose_name='Titre')
    description = models.TextField(max_length=2048, blank=True, verbose_name='Description')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True, verbose_name='Image')
    time_created = models.DateTimeField(auto_now_add=True)

    IMAGE_MAX_SIZE = (300, 500)

    def resize_image(self):
        image = Image.open(self.image)
        image.thumbnail(self.IMAGE_MAX_SIZE)
        image.save(self.image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.resize_image()


class Review(models.Model):

    RATING_CHOICES = (
        ('1', 1),
        ('2', 2),
        ('3', 3),
        ('4', 4),
        ('5', 5),
    )

    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(max_length=1024,
                                         validators=[MinValueValidator(0), MaxValueValidator(5)],
                                         choices=RATING_CHOICES,
                                         verbose_name='Note')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128, verbose_name='Titre')
    body = models.TextField(max_length=8192, blank=True, verbose_name='Commentaire')
    time_created = models.DateTimeField(auto_now_add=True)


class UserFollows(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

    class Meta:
        unique_together = ('user', 'followed_user')
