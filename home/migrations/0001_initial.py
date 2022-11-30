# Generated by Django 3.2.10 on 2021-12-22 07:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitee', models.CharField(max_length=200)),
                ('visitor', models.CharField(max_length=200)),
                ('motif', models.TextField(blank=True, null=True)),
                ('checked_in', models.BooleanField(default=False)),
                ('checked_out', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('leaving_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'order_with_respect_to': 'visitor',
            },
        ),
    ]