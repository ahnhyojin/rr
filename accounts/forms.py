from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['userid','username','email','password','phonenumber']
        widgets = {
            'userid' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력해주세요.'}),
            'username' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'15자 이내로 입력해주세요.'}),
            'email': forms.EmailField(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.NumberInput(attrs={'class': 'from-control', 'placeholder':'숫자만 입력해주세요.'}),
        }
        labels={
            'userid': 'ID',
            'username': '이름',
            'email': '이메일',
            'password': '패스워드',
            'phonenumber': '전화번호'
        }

        def __init__(self, **args, **kwargs):
            super(UserForm,self).__init__(*args,**kwargs)
            self.fields['username'].widget.attrs['maxlength']=15
            self.fields['userid'].widget.attrs['maxlength']=15
            #숫자만 입력받기
            #html문서에 onkeydown='return onlyNumber(event)' onkeyup='removeChar(event)'
            
            