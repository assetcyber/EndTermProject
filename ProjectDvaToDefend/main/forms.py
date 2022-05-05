from email.mime import image
from logging import PlaceHolder
from turtle import textinput, title
from .models import Dopcont, Email, Famous_Persons
from django.forms import ModelForm, TextInput, Textarea
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Famous_Persons_Form(ModelForm):
    class Meta:
        model = Famous_Persons
        fields = ['name', 'biography', 'author_of_publication']

        widgets = {
            'name': TextInput(attrs={
                'class': 'Luboiclass',
                'placeholder': 'Имя личности'
            }),
           'biography': Textarea(attrs={
                'rows':6, 'cols':22,
                'class': 'textareacl',
                'placeholder': 'Напишите о биографии личности'
            }),
            'author_of_publication': TextInput(attrs={
                'class': 'Luboiclass',
                'placeholder': 'Введите ваше имя'
            })
        }
        
class EmailForm(ModelForm):
    class Meta:
        model = Email
        fields = ['email']
        
        widgets = {
            'email': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email'
    })
        }

class DopContForm(ModelForm):
    class Meta:
        model = Dopcont
        fields = ['title', 'content']

        widgets = {
            'title': TextInput(attrs={
                'class': 'abo',
                'placeholder': 'Название статьи'
            }),
            'content': Textarea(attrs={
                'placeholder': 'Название статьи',
                'class': 'abo'
            })
        }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
    
	class Meta:
		model = User
		fields = ("username", "first_name","last_name","date_joined", "email", "password1", "password2")


	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = {'username', 'password'}