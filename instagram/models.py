from django.db import models

# Create your models here.
class Image(models.Model):
    image_name = models.CharField(max_length=120)
    caption = models.TextField()
    # likes = models.ManyToManyField(User, related_name='blogpost_like')
    comments = models.TextField()


    def __str__(self):
        return self.image_name

    # def number_of_likes(self):
    #     return self.likes.count()

