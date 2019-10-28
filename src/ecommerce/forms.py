from django import forms


class ContactForm(forms.Form):

    fullname = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "id": "full_name"
        }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Your email"

            }))
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={

                "class": "form-control",
                "placeholder": "Your message"

            }))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        print(email)
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "name": "username"
        }
    ))
    password = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "type": "password",
            "name": "password"
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            "class": "form-control",
            "name": "username"
        }))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            "class": "form-control",
            "placeholder": "Your email"

        }))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            "class": "form-control",
            "type": "password",
            "name": "password"
        }))
    password2 = forms.CharField(label='Confirm pass', widget=forms.PasswordInput(attrs={
        "class": "form-control",
        "type": "password",
        "name": "password"
    }))

    def clean(self):
        data = self.cleaned_data
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password2')
        username = self.cleaned_data.get('username')
        if pass1 != pass2:
            raise forms.ValidationError(f'{username} Sifreler eyni deyil ala!')
        return data
