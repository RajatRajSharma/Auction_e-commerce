# Generated by Django 4.2.7 on 2023-11-13 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='imageUrl',
            field=models.CharField(default='default_image_url', max_length=1000),
        ),
        migrations.RemoveField(
            model_name='listing',
            name='image_url',
        ),
    ]

