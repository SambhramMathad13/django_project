# Generated by Django 4.2.6 on 2023-12-11 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0012_alter_projects_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='info',
            field=models.TextField(default='sam,sid--188,158--.--.--abcd'),
            preserve_default=False,
        ),
    ]
