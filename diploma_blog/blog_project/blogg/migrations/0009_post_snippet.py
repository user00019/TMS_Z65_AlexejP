# Generated by Django 4.0.5 on 2022-06-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogg', '0008_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='Click Link Above To Read', max_length=200, null=True),
        ),
    ]
