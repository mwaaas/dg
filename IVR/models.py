from django.db import models

from people.models import Person
from videos.models import Video
# Create your models here.
class VideosAdopted(models.Model):
       id = models.AutoField(primary_key=True)
       person = models.ForeignKey(Person)
       mobile_no = models.CharField(max_length=12, null=True)
       video = models.ForeignKey(Video)
       watch_at = models.DateTimeField(null=True)
       survey_at = models.DateTimeField(null=True)
       has_seen = models.BooleanField(default=True)
       has_adopted = models.BooleanField(default=True)
       recording_url = models.URLField(null=True, blank=True)
       s3url = models.URLField(null=True, blank=True)

