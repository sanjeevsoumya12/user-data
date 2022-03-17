from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User 
import os
import subprocess
# Create your models here.

class Datas(models.Model):
    description = models.CharField(max_length=100)
    # user_name = models.TextField()
    uploder = models.ForeignKey(User,default = None, on_delete=models.CASCADE)

    file = models.FileField(upload_to="documents/",
                            validators=[FileExtensionValidator(['jpg',"mp4","gif"])])
    # file = models.FileField(upload_to= get_upload_path,
    #                         validators=[FileExtensionValidator(['jpg',"mp4","gif"])])
    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        print(name, extension)
        return extension

    def save(self,*args,**kwargs):
        # self.user_name = () # here in to add to get current_user
        video_input_path="media/"+self.file.url
        image_output_path='documents'+f'{self.id}'+'.png'
        time = '00:00:00.000'
        subprocess.call(['ffmpeg', '-i',video_input_path, '-ss', '00:00:01.000', '-vframes', '1', image_output_path])
        super().save(*args,**kwargs) 