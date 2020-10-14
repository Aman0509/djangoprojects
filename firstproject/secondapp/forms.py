from django import forms

class UserRegistrationForm(forms.Form):
    gen = [('male', 'MALE'), ('female', 'FEMALE'), ('unknown', 'DECLINE TO ANSWER')]
    firstName = forms.CharField()
    lastName = forms.CharField()
    email = forms.CharField()  # email is defined as Charfield just to demonstrate the form validation. However, you
    # normally define email field like this email = forms.EmailField()
    gender = forms.CharField(widget=forms.Select(choices=gen))
    password = forms.CharField(widget=forms.PasswordInput)
    aadhar = forms.IntegerField()
    resume = forms.FileField()
    feedback = forms.CharField(widget=forms.Textarea, required=False)  # making this field as optional

    def clean(self):
        '''
        Defining only single clean method where you can perform validation for any field together
        '''
        user_cleaned_data = super().clean()
        inputfirstName = self.cleaned_data['firstName']
        if len(inputfirstName) > 20:
            raise forms.ValidationError('Max limit reached!')
        inputemail = self.cleaned_data['email']
        if inputemail.find('@') == -1:
            raise forms.ValidationError('Invalid email')


'''    
    def clean_firstName(self):
        inputfirstName = self.cleaned_data['firstName']
        if len(inputfirstName) > 20:
            raise forms.ValidationError('Max limit reached!')
        return inputfirstName

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        if inputemail.find('@') == -1:
            raise forms.ValidationError('Invalid email')
        return inputemail

'''