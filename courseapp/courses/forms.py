from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(label='Kurs Başlığı', 
                            max_length=100, 
                            error_messages={'required': 'Lütfen kurs başlığını girin.'}, 
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Kurs başlığını girin'})
                            
                            )
    description = forms.CharField(label='Açıklama', 
                                  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Açıklama girin'})
                                  )
    imageUrl = forms.CharField(label='Resim URL', 
                               max_length=200, 
                               required=False, 
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Resim URL girin'})
                               )
    isActive = forms.BooleanField(label='Aktif', 
                                  required=False, 
                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
                                  )
    slug = forms.SlugField(label='Slug', 
                           max_length=100, 
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Slug girin'})
                           )

