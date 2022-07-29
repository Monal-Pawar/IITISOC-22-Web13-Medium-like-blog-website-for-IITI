# Generated by Django 4.0.5 on 2022-07-21 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0002_remove_category_add_date_remove_category_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='add_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
