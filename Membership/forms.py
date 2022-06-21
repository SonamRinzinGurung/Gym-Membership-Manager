from django import forms
from django.forms import  NumberInput, TextInput, EmailInput, ModelForm

from .models import User, Membership,Members


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','personal_address','date_of_birth','phone_number', 'gender','gym_name', 'gym_location', 'gym_phone','password']
        style = 'max-width: 300px;'
        widgets = {
            'username': TextInput(attrs={
                 'class':'form-control',
                'style': style,
                'placeholder': 'Username'
            }),
            'first_name': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'First Name',
            }),
            
            'last_name': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Last Name',
            }),
            
            'email': EmailInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Email',
            }),
            
            'personal_address': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Personal Address',
            }),
            
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date', 
                'class':'form-control', 
                'style': style, 
                'placeholder': 'Date of Birth'}),
                 
                 
            'phone_number': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Phone Number',
            }),
            
            'gender': forms.Select(choices=(("Male","Male"),("Female","Female"),("Other","Other")),
                                   attrs={
                                       'class':'form-control','style': style}),
                                        
            
            
            'gym_name': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Gym Name',
            }),
            
            'gym_location': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Gym Address',
            }),
            
            'gym_phone': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Gym Phone Number',
            }),
            
            'password': forms.PasswordInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Password',
            })
            
        }
    
    
class MembershipForm(ModelForm):
    class Meta:
        model = Membership
        fields = ['membership_type', 'membership_duration', 'membership_price']
        style = 'max-width: 300px;'
        widgets = {
            'membership_type':TextInput(attrs={
               'class':'form-control',
               'style': style,
               'placeholder': 'Membership Type',
            }),
            'membership_duration':TextInput(attrs={
               'class':'form-control',
               'style': style,
               'placeholder': 'Membership Duration',
            }),
            'membership_price':NumberInput(attrs={
               'class':'form-control',
               'style': style,
               'placeholder': 'Membership Price',
            }),
        }
        
        
class MemberForm(ModelForm):
    
    class Meta:
        model = Members
        fields = ['first_name', 'last_name','email', 'phone_number', 'age', 'gender','address', 'membership','validity']
        
        membership = forms.ModelChoiceField(queryset=Membership.objects.all(), to_field_name="membership_type", empty_label=None)

        style = 'max-width: 300px;'
        widgets = {
            'first_name':TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'First Name',
            }),
            'last_name': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Last Name',
            }),
            
            'email': EmailInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Email',
            }),
            
            'phone_number': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Phone Number',
            }),
            'age': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Age',
            }),
            'gender': forms.Select(choices=(("Male","Male"),("Female","Female"),("Other","Other")),
                                attrs={
                                    'class':'form-control','style': style}),
                
            'address': TextInput(attrs={
                'class':'form-control',
                'style': style,
                'placeholder': 'Address',
            }),            
            
            'validity': forms.DateInput(attrs={
                'type': 'date', 
                'class':'form-control', 
                'style': style, 
                'placeholder': 'Membership Validity'}),
            
        }
        
        
class SearchForm(forms.Form):
    search = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'Search Member',
    }))
    
        