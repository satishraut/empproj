# Generated by Django 2.1.5 on 2019-02-09 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0004_village'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Village',
        ),
        migrations.AddField(
            model_name='employee',
            name='country',
            field=models.CharField(default='Checking', max_length=20),
        ),
    ]