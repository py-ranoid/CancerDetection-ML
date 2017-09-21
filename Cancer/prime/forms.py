from django import forms

class NameForm(forms.Form):
    #your_name : First Name
    your_name = forms.CharField(label=' First Name ',max_length=100)
    last_name = forms.CharField(label='  Last Name  ',max_length=100)
    doc_id = forms.CharField(label=' Registered ID  ',max_length=100)
    salary = forms.IntegerField(label=' Salary         ')
