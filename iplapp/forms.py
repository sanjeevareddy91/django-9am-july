from django.forms import ModelForm,Form
from .models import Team_Info
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class Team_InfoModelForm(ModelForm):
    class Meta:
        model = Team_Info
        fields = "__all__"
        # fields = ('team_name',"nick_name") # will give only 2 fields which are specified. 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('team_name', css_class='form-group col-md-4 mb-0'),
                Column('nick_name', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            'team_logo',
            Row(
                Column('captain_name', css_class='form-group col-md-4 mb-0'),
                Column('started_year', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Save')
        )