# Generated by Django 3.2.5 on 2021-07-12 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landingpage', '0003_landing_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='landing',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
