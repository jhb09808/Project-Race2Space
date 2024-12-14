from django import forms
from .models import Discussion, Reply

class DiscussionForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Discussion
        fields = ['subject', 'message', 'name']

class ReplyForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Reply
        fields = ['message', 'name']
