from django import forms


class Registeration(forms.Form):
  first_name = forms.CharField()
  last_name = forms.CharField()
  age = forms.IntegerField()
  email = forms.EmailField()
  city = forms.CharField()
  
class Login(forms.Form):
  email = forms.EmailField()
  password = forms.CharField()  
  
  