# Generated by Django 3.1.7 on 2021-03-28 03:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0002_topic_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_by',
            field=models.ForeignKey(null=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
            preserve_default=1,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_dt',
            field=models.DateTimeField(null=1),
            preserve_default=1,
        ),
    ]