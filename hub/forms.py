from django import forms


class ItemUpdateForm(forms.Form):
    name = forms.CharField(max_length=75)
    description = forms.TextInput()
    quantity = forms.IntegerField()
    link = forms.URLField(required=False)
    icon = forms.IntegerField()


class ItemForm(forms.Form):
    name = forms.CharField(max_length=75)
    description = forms.TextInput()
    quantity = forms.IntegerField()
    link = forms.URLField(required=False)
    icon = forms.IntegerField()
