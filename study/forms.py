from django.forms import ModelForm, Textarea
from .models import DailyNote

class DailyNoteForm(ModelForm):
    class Meta:
        model = DailyNote
        fields = ('come_status', 'homework_complete', 'homework_status', 'contents', 'test1', 'test1_content', 'test2', 'test2_content', 'test3', 'test3_content', 'note')
        widgets = {
            'note' : Textarea(attrs={'cols': 80, 'rows': 20}),
        }
