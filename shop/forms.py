from shop.models import Feedback
from django import forms


class FeedbackForm(forms.ModelForm):
    text = forms.TextInput()
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=Feedback.RATE_CHOICES)

    class Meta:
        model = Feedback
        fields = ['rating', 'text']
