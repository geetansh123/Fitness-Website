# Generated by Django 3.1.1 on 2020-11-08 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_newuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='newuser',
            name='weight',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]