# Generated by Django 5.0.2 on 2024-03-14 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]