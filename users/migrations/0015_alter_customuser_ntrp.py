# Generated by Django 3.2.14 on 2022-09-05 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20220905_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='ntrp',
            field=models.DecimalField(blank=True, decimal_places=1, default=None, max_digits=1),
        ),
    ]
