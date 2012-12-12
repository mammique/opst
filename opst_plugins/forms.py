from django import forms


class SearchBoxForm(forms.Form):

    q = forms.CharField(max_length=128)
