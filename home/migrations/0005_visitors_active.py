# Generated by Django 3.2.10 on 2021-12-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_visitors_leaving_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='visitors',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]