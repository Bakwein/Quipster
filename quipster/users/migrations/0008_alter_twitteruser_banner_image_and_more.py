# Generated by Django 5.0.4 on 2024-05-12 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_twitteruser_banner_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='twitteruser',
            name='banner_image',
            field=models.ImageField(blank=True, null=True, upload_to='banner_images/'),
        ),
        migrations.AlterField(
            model_name='twitteruser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pictures/'),
        ),
    ]
