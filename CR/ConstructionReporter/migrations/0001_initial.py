# Generated by Django 3.2 on 2021-04-11 16:32

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
            name='DefectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MediaFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media_file', models.FileField(upload_to='media_files/')),
                ('media_type', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('respondent_name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_group_name', models.CharField(max_length=200)),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('location_type', models.CharField(max_length=200)),
                ('location_admin', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('location_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.location')),
                ('location_user_group', models.ManyToManyField(to='ConstructionReporter.UserGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_name', models.CharField(max_length=200)),
                ('defect_description', models.CharField(max_length=200)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('defect_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.location')),
                ('defect_respondent', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ConstructionReporter.respondent')),
                ('defect_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.defectstatus')),
                ('media_files', models.ManyToManyField(to='ConstructionReporter.MediaFile')),
                ('reporter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
