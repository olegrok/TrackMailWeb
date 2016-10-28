# coding: utf-8

from django import forms

class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1024, widget=forms.Textarea)

    def clean_text(self):
        text = self.cleaned_data['comment']
        if text.isspace():
            raise forms.ValidationError(u'Empty string!')