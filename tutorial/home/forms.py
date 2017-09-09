from django import forms

class HomeForm(forms.Form):
    post = forms.CharField()  #html에서 할 수 있지만 form으로 이런식으로 하는게 더 안전하다. 
