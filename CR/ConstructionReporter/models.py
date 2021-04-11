from django.db import models
from django.contrib.auth.models import User

class DefectStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class LocationType(models.Model):
    location_type_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_type_name

class UserGroup(models.Model):
    user_group_name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User)
    # user_group_admin = models.ManyToManyField(User)

    def __str__(self):
        return self.location_name


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_type = models.CharField(max_length=200)
    location_parent = models.ForeignKey('self', on_delete=models.CASCADE)
    location_user_group = models.ManyToManyField(UserGroup)
    location_admin = models.ManyToManyField(User)

    def __str__(self):
        return self.location_name

class Respondent(models.Model):
    respondent_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.respondent_name

class MediaFile(models.Model):
    media_file = models.FileField(upload_to='media_files/')
    media_type = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media_file

class Defect(models.Model):
    defect_name = models.CharField(max_length=200)
    defect_description = models.CharField(max_length=200)
    defect_status = models.ForeignKey(DefectStatus, on_delete=models.CASCADE)
    defect_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    defect_respondent = models.ForeignKey(Respondent, on_delete=models.PROTECT)
    creation_date = models.DateTimeField('date created')
    media_files = models.ManyToManyField(MediaFile)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT)



    # test if defect needs to possess a photo
    # test photo size
    # relations - adding staircase to non-existing building
    # negative tests - to check if tests work

    #
    # operations = [
    #     migrations.AddField(
    #         model_name='defect',
    #         name='defect_status',
    #         field=models.CharField(choices=[('Unrepaired', 'Unrepaired'), ('Repaired', 'Repaired')], default='Unrepaired', max_length=10),
    #     ),
    # ]
