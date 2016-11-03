# coding: utf-8

from django import forms
from .models import Comment
from photos.models import Photo
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect


class CommentForm(forms.Form):
    comment = forms.CharField(max_length=1024, required=True, widget=forms.Textarea)

    def clean_comment(self):
        text = self.cleaned_data['comment']
        if text.isspace():
            raise forms.ValidationError(u'Empty string!')
        return text