# Generated by Django 3.2.14 on 2022-09-05 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_customuser_ntrp2'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.TextField(default=None),
        ),
    ]
