from django.db import models
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class LocationType(models.Model):
    location_type_name = models.CharField(max_length=200)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['location_type_name'], name='location_unique_name'),
        ]

    def __str__(self):
        return self.location_type_name


class Location(models.Model):
    location_name = models.CharField(max_length=200)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT)
    location_parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    location_user_group = models.ManyToManyField(Group)
    location_admin = models.ManyToManyField(User)

    def __str__(self):
        return self.location_name


class MediaFile(models.Model):
    media_file = models.FileField(upload_to='media_files/')
    media_type = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.media_file


class DefectStatus(models.Model):
    defect_status = models.CharField(max_length=200)

    def __str__(self):
        return self.defect_status


class Defect(models.Model):
    defect_name = models.CharField(max_length=200)
    defect_description = models.CharField(max_length=200)
    defect_status = models.ForeignKey(DefectStatus, on_delete=models.CASCADE)    #TODO make it so that user decides which one to choose
    defect_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # defect_respondent = models.ManyToManyField(Group, blank=True, null=True)
    defect_respondent = models.ForeignKey(Group, on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    media_files = models.ManyToManyField(MediaFile, blank=True)
    reporter = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    # test if defect needs to possess a photo
    # test photo size
    # relations - adding staircase to non-existing building
    # negative tests - to check if tests work


class LocationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LocationType
        fields = ['location_type_name']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)




class LocationSerializer(serializers.HyperlinkedModelSerializer):
    # location_name = LocationNameSerializer(many=False, read_only=True)
    location_type = LocationTypeSerializer(many=False, read_only=True)
    location_parent = serializers.PrimaryKeyRelatedField(read_only=True)
    location_admin = UserSerializer(many=True, read_only=True)
    location_user_group = GroupSerializer(many=True, read_only=True)

    # location_user_group = serializers.PrimaryKeyRelatedField(read_only=True)


    class Meta:
        model = Location
        fields = ['location_name', 'location_type', 'location_parent', 'location_admin', 'location_user_group']
        # lookup_field = 'group__name'


class DefectStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DefectStatus
        fields = ['defect_status']


class DefectSerializer(serializers.HyperlinkedModelSerializer):
    defect_status = DefectStatusSerializer(many=False, read_only=True)
    defect_location = LocationSerializer(many=False, read_only=True)
    defect_respondent = GroupSerializer(many=True, read_only=True)

    class Meta:
        model = Defect
        fields = ['defect_respondent', 'defect_status', 'defect_location', 'defect_name', 'defect_description', 'defect_respondent', ]

