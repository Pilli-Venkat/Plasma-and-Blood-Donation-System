# Generated by Django 4.0.1 on 2022-02-10 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_donate_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='city',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donate',
            name='district',
            field=models.CharField(default=None, max_length=250),
            preserve_default=False,
        ),
    ]
