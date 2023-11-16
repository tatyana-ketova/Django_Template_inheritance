from django import forms


class FormName(forms.Form):
    login = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    mobile = forms.IntegerField()
