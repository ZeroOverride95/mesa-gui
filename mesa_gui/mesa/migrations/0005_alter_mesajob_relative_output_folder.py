# Generated by Django 4.2.4 on 2023-08-02 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0004_mesajob_relative_output_folder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mesajob',
            name='relative_output_folder',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
