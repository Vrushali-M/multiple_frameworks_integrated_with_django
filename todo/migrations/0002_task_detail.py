# Generated by Django 3.0.5 on 2020-07-01 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='detail',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
