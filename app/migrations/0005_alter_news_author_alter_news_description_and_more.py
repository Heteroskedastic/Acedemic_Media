# Generated by Django 4.0 on 2021-12-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_news_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='publishedAt',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='source',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]