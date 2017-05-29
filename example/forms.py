from django import forms
from example.models import GiftList


class GiftListForm(forms.ModelForm):
    class Meta:
        model = GiftList
        exclude = ('modified', )
        # fields = ()
        # fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if 'curse' in name.lower():
            raise forms.ValidationError('You cannot use forbidden words')

        # Always return the cleaned.data, whether you have changed it ot not.
        return name