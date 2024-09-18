from django import forms
from .models import Flight
from datetime import datetime


class AdminLoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_id', 'dep_airport', 'dep_date', 'dep_time', 'arr_airport', 'arr_date', 'arr_time']

    def clean_dep_date(self):
        dep_date = self.cleaned_data.get('dep_date')
        if dep_date < datetime.today().date():
            raise forms.ValidationError("Departure date cannot be in the past.")
        return dep_date

    def clean_arr_date(self):
        dep_date = self.cleaned_data.get('dep_date')
        arr_date = self.cleaned_data.get('arr_date')
        if arr_date < dep_date:
            raise forms.ValidationError("Arrival date cannot be before departure date.")
        return arr_date

    def clean(self):
        cleaned_data = super().clean()
        dep_time = cleaned_data.get('dep_time')
        arr_time = cleaned_data.get('arr_time')
        dep_date = cleaned_data.get('dep_date')
        arr_date = cleaned_data.get('arr_date')

        if dep_date == arr_date and dep_time >= arr_time:
            raise forms.ValidationError("Arrival time must be after departure time for the same day.")
        return cleaned_data
