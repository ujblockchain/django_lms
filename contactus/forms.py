from django import forms

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Enter your Fullname", max_length=100, required=True, error_messages={
        "required": "Fullname is required",
        "max_length": "Fullname characters is too long"
    })
    email = forms.EmailField(label="Email Address", error_messages={
        "required": "Email field is required"
    })
    
    level = forms.IntegerField(label="Study Level", min_value=100, max_value=700)
    comment = forms.CharField(label="Comment/Query", widget=forms.Textarea, max_length=200)
    
    # screenshot = forms.FileField(label="Screenshot", required=False)
    
    
    screenshot = forms.ImageField(label="Screenshot", required=False)
    