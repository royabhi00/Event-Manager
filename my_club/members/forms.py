from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms


class RegisterUserForm(UserCreationForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
	

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(RegisterUserForm, self).__init__(*args, **kwargs)
        
        # THIS IS THE SAME THINK AS ABOVE IN email, first_name, last_name
        #THIS IS IN DJANGO DOC 
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['class'] = 'form-control'

class ChangePasswordForm(PasswordChangeForm):

	class Meta:
		model = User
		fields = ('old_password','new_password1','new_password2')

	def __init__(self, *args, **kwargs):
		super(ChangePasswordForm, self).__init__(*args, **kwargs)
        
        # THIS IS THE SAME THINK AS ABOVE IN email, first_name, last_name
        #THIS IS IN DJANGO DOC 
		self.fields['old_password'].widget.attrs['class'] = 'form-control'
		self.fields['new_password1'].widget.attrs['class'] = 'form-control'
		self.fields['new_password2'].widget.attrs['class'] = 'form-control'