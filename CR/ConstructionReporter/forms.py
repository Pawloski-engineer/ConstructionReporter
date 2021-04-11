from django import forms

from .models import Location, LocationType, Respondent #TODO add Defect

from django.contrib.auth.models import User


class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('location_name', 'location_type', 'location_parent', 'location_user_group', 'location_admin')


class LocationTypeForm(forms.ModelForm):
    class Meta:
        model = LocationType
        fields = ('location_type_name',)


# class DefectForm(forms.ModelForm):
#     class Meta:
#         model = Defect
#         fields = ('defect_name', 'defect_description', 'defect_status', 'defect_location', 'defect_respondent')


class RespondentForm(forms.ModelForm):
    class Meta:
        model = Respondent
        fields = ('respondent_name', 'phone', 'email')