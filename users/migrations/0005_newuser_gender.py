# Generated by Django 3.1.1 on 2020-11-08 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20201108_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True),
        ),
    ]