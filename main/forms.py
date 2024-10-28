from .models import Review
from django.forms import ModelForm,TextInput, Textarea

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['company', 'review']

        widgets = {
            'company': TextInput(attrs={
                "class": "form-control",
                "placeholder": "Название компании",
                "style": "color:#9400D3;"
            }),
            'review': Textarea(attrs={
                "class": "form-control",
                "placeholder": "Отзыв",
                "style": "color:#9400D3;margin-top:5%;margin-bottom:5%;"
            }),

        }