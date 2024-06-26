# Generated by Django 5.0.4 on 2024-05-27 04:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_publications', '0002_alter_publicationsmodel_pub_file_uz'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicationsmodel',
            name='pub_file_en',
        ),
        migrations.RemoveField(
            model_name='publicationsmodel',
            name='pub_file_ru',
        ),
        migrations.RemoveField(
            model_name='publicationsmodel',
            name='pub_file_uz',
        ),
        migrations.CreateModel(
            name='PublicationFilesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('pub_file_uz', models.FileField(null=True, upload_to='static/pub_file/')),
                ('pub_file_en', models.FileField(null=True, upload_to='static/pub_file/')),
                ('pub_file_ru', models.FileField(null=True, upload_to='static/pub_file/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pub_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_publications.publicationsmodel')),
            ],
            options={
                'db_table': 'pub_files',
            },
        ),
    ]
