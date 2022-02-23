# Generated by Django 4.0.2 on 2022-02-21 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sroll', models.IntegerField(max_length=2)),
                ('sname', models.CharField(max_length=20)),
                ('sclass', models.CharField(choices=[('6', 'VI'), ('7', 'VII')], max_length=1)),
                ('ssection', models.CharField(choices=[('p', 'P'), ('q', 'Q')], max_length=1)),
                ('sabsent', models.IntegerField(default=0)),
                ('sphone', models.CharField(max_length=11)),
                ('pradress', models.CharField(max_length=20)),
                ('pmadress', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='AbsentDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('absdate', models.DateField()),
                ('abstudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
    ]
