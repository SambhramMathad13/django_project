# Generated by Django 4.2.6 on 2023-11-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0011_projects_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.ImageField(null=True, upload_to='proj_imgs'),
        ),
    ]