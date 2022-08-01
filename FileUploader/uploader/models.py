from django.db import models
from django.contrib.auth.models import User
# Create your models here.
import os

types_choices = (
('txt' , 'متن') ,
('img' , 'تصویر') ,
('other' , 'دیگر') ,
)

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext
def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    final_name = f"IMG-{instance.user.id}{ext}"
    return f"{final_name}"

class UploadedFile(models.Model):
	user = models.ForeignKey(User , on_delete = models.CASCADE)
	file = models.FileField(upload_to=upload_image_path , blank=True , null=True)
	type = models.CharField(choices = types_choices , max_length = 15)
	size = models.CharField(max_length = 100 , verbose_name = 'Size (MB)')

	# a define for remove Object in MINIO
