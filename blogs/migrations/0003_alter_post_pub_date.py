# Generated by Django 4.1.3 on 2022-11-13 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_category_series_post_author_post_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 13, 19, 32, 55, 544990, tzinfo=datetime.timezone.utc), verbose_name='publish date'),
        ),
    ]
