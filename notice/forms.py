from django import forms

from notice.models import Notice


class NoticeForm(forms.ModelForm):
    class Meta:
        model = Notice
        fields = '__all__'
