from django import forms
from .models import Datas


# Create your forms here.
class DataForm(forms.ModelForm):

    class Meta:
        model = Datas
        fields = ("description",'file')