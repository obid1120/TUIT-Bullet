# Generated by Django 5.0.4 on 2024-05-29 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_publications', '0005_papersmodel_paper_annotation_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='papersmodel',
            name='paper_reference',
        ),
        migrations.AddField(
            model_name='papersmodel',
            name='paper_reference',
            field=models.ManyToManyField(to='app_publications.referencesmodel'),
        ),
    ]