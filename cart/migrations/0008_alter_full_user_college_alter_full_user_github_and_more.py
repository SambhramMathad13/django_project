# Generated by Django 4.2.6 on 2023-11-04 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0007_full_user_github'),
    ]

    operations = [
        migrations.AlterField(
            model_name='full_user',
            name='college',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='full_user',
            name='github',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='full_user',
            name='sem',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
