from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    thumbnail_image = models.CharField(max_length=200)
    preview_image = models.CharField(max_length=200)
    description = models.TextField()
    video_ogv = models.CharField(max_length=1000, null=True, blank=True)
    video_mp4 = models.CharField(max_length=1000, null=True, blank=True)
    video_vp8 = models.CharField(max_length=1000, null=True, blank=True)
    length = models.PositiveIntegerField()
    episode = models.PositiveIntegerField()
    publish_date = models.DateTimeField()
    created_at = models.DateTimeField()

    def __unicode__(self):
        return self.title
