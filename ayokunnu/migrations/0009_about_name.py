# Generated by Django 5.0.6 on 2025-01-09 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayokunnu', '0008_image_gallery_img_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='name',
            field=models.TextField(default='AY_REACT'),
        ),
    ]
