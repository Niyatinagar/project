# Generated by Django 5.0.2 on 2024-03-19 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0009_alter_course_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In review'), ('published', 'Published')], default='draft', max_length=25),
        ),
    ]
