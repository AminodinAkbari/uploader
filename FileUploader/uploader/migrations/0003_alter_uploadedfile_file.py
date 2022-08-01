# Generated by Django 4.0.6 on 2022-08-01 10:54

from django.db import migrations, models
import uploader.models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0002_uploadedfile_file_alter_uploadedfile_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedfile',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=uploader.models.upload_image_path),
        ),
    ]
