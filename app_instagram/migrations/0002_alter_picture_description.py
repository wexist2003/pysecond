# Generated by Django 5.0.2 on 2024-02-27 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='description',
            field=models.CharField(max_length=150),
        ),
    ]