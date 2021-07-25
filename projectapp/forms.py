from django.forms import ModelForm
from django import forms


from projectapp.models import Project


class ProjectCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))
    project = forms.ModelChoiceField(queryset=Project.objects.all(), required=False)

    class Meta:
        model = Project
        fields = ['title', 'image', 'image2', 'image3', 'project', 'content']