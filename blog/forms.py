from django import forms

class Login(forms.Form):
    nome = forms.CharField(max_length = 200, label= "nome")
    email = forms.EmailField(label="email", max_length=200, required= True)