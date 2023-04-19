from django.forms import ModelForm, Textarea, NumberInput
from .models import Review


class ReviewForm(ModelForm):
    # readonly = ('user', 'review')

    class Meta:
        model = Review
        fields = ['featured']

    # def __init__(self, *arg, **kwargs):
    #     super(ReviewForm, self).__init__(*arg, **kwargs)
    #     for x in self.readonly:
    #         self.fields[x].widget.attrs['disabled'] = 'disabled'

    widgets = {
        # 'review': Textarea(
        #     attrs={'cols': '80', 'rows': '3',
        #            'class': 'form-control'}
        # ),
        'featured': NumberInput(
            attrs={'min': '1', 'max': '2'}
        )
    }
