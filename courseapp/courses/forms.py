from django import forms
from django.forms import TextInput, Textarea, CheckboxInput, SelectMultiple
from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(label='Kurs Başlığı', 
#                             max_length=100, 
#                             error_messages={'required': 'Lütfen kurs başlığını girin.'}, 
#                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurs başlığını girin'})
                            
#                             )
#     description = forms.CharField(label='Açıklama', 
#                                   widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama girin'})
#                                   )
#     imageUrl = forms.CharField(label='Resim URL', 
#                                max_length=200, 
#                                required=False, 
#                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resim URL girin'})
#                                )
#     isActive = forms.BooleanField(label='Aktif', 
#                                   required=False, 
#                                   widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
#                                   )
#     slug = forms.SlugField(label='Slug', 
#                            max_length=100, 
#                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug girin'})
#                            )


class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'imageUrl', 'isActive', 'slug']
        labels = {
            'title': 'Kurs Başlığı',
            'description': 'Açıklama',
            'imageUrl': 'Resim URL',
            'isActive': 'Aktif',
            'slug': 'Slug',
        }
        error_messages = {
            'title': {
                'required': 'Lütfen kurs başlığını girin.',
            },
            'description': {
                'required': 'Lütfen açıklamayı girin.',
            },
            'imageUrl': {
                'required': 'Lütfen resim URL\'sini girin.',
            },
            'slug': {
                'required': 'Lütfen slug\'ı girin.',
            },
        }
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurs başlığını girin'}),
            'description': Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama girin'}),
            'imageUrl': TextInput(attrs={'class': 'form-control', 'placeholder': 'Resim URL girin'}),
            'isActive': CheckboxInput(attrs={'class': 'form-check-input'}),
            'slug': TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug girin'}),
        }

        