# coding: utf-8

from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(max_length=30, label=u'Поиск по сайту', required=False)
    sort = forms.TypedChoiceField(empty_value='-pub_date', required=False,
                                  choices=[('-pub_date', u'По убыванию'), ('pub_date', u'По возрастанию')],
                                  label=u'Сортировать по')