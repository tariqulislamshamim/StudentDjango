# Generated by Django 4.0.2 on 2022-02-25 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_alter_student_sabsent'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['sroll']},
        ),
    ]
