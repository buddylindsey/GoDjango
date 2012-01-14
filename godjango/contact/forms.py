from django import forms

class FeedbackForm(forms.Form):
    email = forms.EmailField(label="Your Email")
    body = forms.CharField(label="Body",widget=forms.Textarea)
