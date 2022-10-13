from django import forms

class NewTaskForm(forms.Form):
    title = forms.CharField(label='Judul Task:', widget=forms.TextInput(attrs={'placeholder': 'Judul Task Baru', 'class':'form-control mx-3 my-2'}))
    description = forms.CharField(label="Deskripsi Task:", widget=forms.Textarea(attrs={'placeholder': 'Deskripsi Task Baru', 'class':'form-control mx-3 my-2'}))