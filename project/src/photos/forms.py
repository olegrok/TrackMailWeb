# coding: utf-8

from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, label=u'Поиск по сайту', required=False)