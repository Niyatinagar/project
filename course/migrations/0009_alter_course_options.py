# Generated by Django 5.0.2 on 2024-03-19 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_course_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ('-created_at',)},
        ),
    ]
