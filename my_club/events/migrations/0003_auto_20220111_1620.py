# Generated by Django 3.2 on 2022-01-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_venue_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='phone',
            field=models.CharField(blank=True, max_length=25, verbose_name='Contact Number'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='web',
            field=models.URLField(blank=True, verbose_name='Website Address'),
        ),
    ]
