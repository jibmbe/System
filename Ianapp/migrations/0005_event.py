# Generated by Django 4.2.7 on 2023-11-26 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ianapp', '0004_alter_place_distance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]