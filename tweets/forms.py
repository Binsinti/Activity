
from django import forms
from .models import Tweet

PROHIBITED_WORDS = ['shit', 'fuck', 'bobo']

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content', 'image']

    def clean_content(self):
        content = self.cleaned_data.get('content', '').lower()
        for word in PROHIBITED_WORDS:
            if word in content:
                raise forms.ValidationError(
                    f'The word "{word}" is not allowed in tweets.'
                )
        return self.cleaned_data['content']