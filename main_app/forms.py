from django.forms import ModelForm
from .models import Feeding

#ModelForms go below
class FeedingForm(ModelForm):
    class Meta:
        model = Feeding
        fields = ['date', 'meal']