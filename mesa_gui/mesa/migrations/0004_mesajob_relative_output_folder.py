# Generated by Django 4.2.4 on 2023-08-02 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesa', '0003_alter_mesajob_finished_at_alter_mesajob_started_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='mesajob',
            name='relative_output_folder',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
