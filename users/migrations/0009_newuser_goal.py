# Generated by Django 3.1.1 on 2020-11-18 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20201110_1205'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='goal',
            field=models.CharField(choices=[('Lean', 'Lean'), ('Bulky', 'Bulky'), ('Improve Strength', 'Improve Strength'), ('Improve Endurance', 'Improve Endurance'), ('Improve Flexibility', 'Improve Flexibility'), ('Basic Fitness', 'Basic Fitness')], default='Basic Fitness', max_length=30),
        ),
    ]
