# Generated by Django 4.0.2 on 2022-02-24 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0002_alter_student_sphone_alter_student_sroll'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sclass',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='student',
            name='ssection',
            field=models.CharField(max_length=1),
        ),
    ]
