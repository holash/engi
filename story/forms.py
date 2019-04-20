from django import forms

from .models import Post, Comment, Reply

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title','category','photo_post', 'content',)
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'content',)

class ReplyForm(forms.ModelForm):

    class Meta:
        model = Reply
        fields = ('author', 'content',)