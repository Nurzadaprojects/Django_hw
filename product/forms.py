from django import forms

from product.models import Product, Review

class ProductForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    image = forms.ImageField()

    def clean_title(self):
        title = self.cleaned_data['title']
        if "python" in title.lower():
            # raise Exception("Python is not allowed")
            raise forms.ValidationError("Python is not allowed")

        return title.capitalize()



    # def clean_content(self):
    #     content = self.cleaned_data['content']
    #     if "django" in content.lower():
    #         raise forms.ValidationError("Django is not allowed")
    #
    #     return content
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     title = cleaned_data.get['title']
    #     content = cleaned_data.get['content']
    #
    #     if title and content:
    #         if title.lower() == content.lower():
    #             raise forms.ValidationError("Title and content must be different")
    #
    #     return cleaned_data

class ProductForm2(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['rate']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title']
        labels = {
            'title': 'Review'
        }

        widgets = {
            'title': forms.Textarea(attrs={'class': 'form-control'})
        }
