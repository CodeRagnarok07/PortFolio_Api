# Generated by Django 4.0.2 on 2022-08-12 04:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_skill_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='my_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='work',
            name='place',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
