from django import forms
from steal_destination.main.models import Destination, Blog, Post, PostImage, Comments


class CreateDestinationForm(forms.ModelForm):

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        # получаваме дестиация инстацията, не отива към базата
        destination = super().save(commit=False)
        destination.user = self.user
        if commit:
            destination.save()
        return destination

    class Meta:
        model = Destination
        fields = ('country_name', 'venue_name', 'type', 'description', 'image')
        widgets = {
            'country_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Country's Name",
                }
            ),
            'venue_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter Venue's Name",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': "Enter description",
                    'row': 5
                }
            ),

        }


class EditDestinationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Destination
        fields = ('country_name', 'venue_name', 'type', 'description', 'image')


class CommentForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        # получаваме дестиация инстацията, не отива към базата
        comment = super().save(commit=False)
        comment.user = self.user
        if commit:
            comment.save()
        return comment

    class Meta:
        model = Comments
        fields = ('name', 'body',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment'}),
        }


# class EditCommentForm(forms.ModelForm):
#     def __init__(self, user, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.user = user
#
#     class Meta:
#         model = Comments
#         fields = ('name', 'body',)
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
#             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your comment'}),
#         }


class BlogForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        # получаваме дестиация инстацията, не отива към базата
        article = super().save(commit=False)
        article.user = self.user
        if commit:
            article.save()
        return article

    class Meta:
        model = Blog
        fields = ('article_name', 'description', 'image',)
        widgets = {
            'article_name': forms.TextInput(
                attrs={
                    'placeholder': "Enter article's Name",
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': "Enter description",
                    'row': 5
                }
            ),

        }


class EditArticleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Blog
        fields = ('article_name', 'description', 'image',)
