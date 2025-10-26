from django import forms

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label="Example Name")
    description = forms.CharField(widget=forms.Textarea, label="Description")
