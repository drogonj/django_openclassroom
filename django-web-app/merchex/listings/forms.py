from django import forms
from listings.models import Band, Contact

class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = '__all__'
        # exclude = ('active', 'official_homepage') Pour exclure certains champs d'un formulaire

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, max_length=50)
    email = forms.EmailField()
    message = forms.CharField(max_length=1000)