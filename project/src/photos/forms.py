# coding: utf-8

from django import forms
from comments.models import Comment
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect
from .models import Photo


class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, label=u'Поиск по сайту', required=False)
    sort = forms.TypedChoiceField(empty_value='-pub_date', required=False,
                                  choices=[('-pub_date', u'По убыванию'), ('pub_date', u'По возрастанию')],
                                  label=u'Сортировать по')





