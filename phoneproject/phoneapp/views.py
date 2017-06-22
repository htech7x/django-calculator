from django import forms
from django.shortcuts import render

class MyForm(forms.Form):
    val1 = forms.IntegerField()
    val2 = forms.IntegerField()


def index(request):
    result = 'N/A'
    res = '0'

    if request.method == 'GET':
        form = MyForm()        
    else:  # request.method == 'POST'
        form = MyForm(request.POST)
        if form.is_valid():
            result = form.cleaned_data['val1'] + form.cleaned_data['val2']

    return render(request, 'index.html', {'form': form, 'result': result})
