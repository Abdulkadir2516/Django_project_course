from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField(max_length=200, required=False)  # Dosya yükleme için ImageField kullanılır
    isActive = forms.BooleanField(required=False)  # Checkbox için BooleanField kullanılır
    slug = forms.SlugField(max_length=100)

