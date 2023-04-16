from django import forms

class uploadPageForm(forms.Form):
    print('inside froms')
    path = forms.CharField
    # file = forms.FileField