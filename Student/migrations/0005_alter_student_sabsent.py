# Generated by Django 4.0.2 on 2022-02-24 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0004_alter_student_sclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sabsent',
            field=models.IntegerField(null=True),
        ),
    ]