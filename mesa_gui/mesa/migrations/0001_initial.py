# Generated by Django 4.2.4 on 2023-08-01 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('domain_fqdn', models.CharField(max_length=255)),
                ('domain_controller', models.CharField(max_length=255)),
                ('domain_user', models.CharField(max_length=255)),
                ('domain_password', models.CharField(max_length=255)),
                ('neo4j_user', models.CharField(max_length=255)),
                ('neo4j_password', models.CharField(max_length=255)),
            ],
        ),
    ]
