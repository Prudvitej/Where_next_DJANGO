from django import forms

class BookingForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile = forms.CharField(max_length=15)
    from_location = forms.CharField(max_length=100)
    to_location = forms.CharField(max_length=100)
    date = forms.DateField(widget=forms.SelectDateWidget())
    members = forms.IntegerField()
