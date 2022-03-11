from django.core.validators import FileExtensionValidator
from django.db import models
import os

# Create your models here.


class Datas(models.Model):
    description = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/",
                            validators=[FileExtensionValidator(['jpg',"mp4","gif"])])

    def extension(self):
        name, extension = os.path.splitext(self.file.name)
        print(name, extension)
        return extension
