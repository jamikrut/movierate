# Generated by Django 4.2.5 on 2023-10-01 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
