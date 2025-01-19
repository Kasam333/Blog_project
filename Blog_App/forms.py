from django import forms
from .models import *

choice = Category.objects.all().values_list("name", "name")
choice_list = list(choice)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author', 'title', 'title_description', 'body', 'category', 'post_image')

        widgets = {
            'author' : forms.Select(attrs={'class': 'form-control', 'placeholder' : 'Username', 'id' : 'elder', 'value' : ''}),
            'title' : forms.TextInput(attrs={'class':'form-contro;', 'placeholder': 'Title'}),
            'title_description' : forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Title Description'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control', 'placeholder': 'Content'}),
            'category' : forms.Select(choices= choice_list, attrs={'class': 'form-control'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_description', 'body')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_description' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class' : 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

        widgets = {
            'body': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Category name'})
        }