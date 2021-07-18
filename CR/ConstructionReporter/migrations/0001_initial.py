# Generated by Django 3.2 on 2021-07-14 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DefectStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LocationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type_name', models.CharField(max_length=200, unique=True)),
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
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_name', models.CharField(max_length=200)),
                ('location_admin', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('location_parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.location')),
                ('location_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ConstructionReporter.locationtype')),
                ('location_user_group', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'unique_together': {('location_name', 'location_parent')},
            },
        ),
        migrations.CreateModel(
            name='Defect',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defect_name', models.CharField(max_length=200)),
                ('defect_description', models.CharField(blank=True, max_length=200)),
                ('creation_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('defect_location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.location')),
                ('defect_respondent', models.ManyToManyField(to='auth.Group')),
                ('defect_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ConstructionReporter.defectstatus')),
                ('media_files', models.ManyToManyField(blank=True, to='ConstructionReporter.MediaFile')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
