from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea,max_length=100)

    # def clean_message(self): #Django’s form system automatically looks for any method whose name starts with clean_ and ends with the name of a field. If any such method exists, it’s called during validation
    #     message = self.cleaned_data['message']
    #     num_words = len(message.split())
    #     if num_words < 4:
    #         raise forms.ValidationError("Not enough words!")
    #     return message
