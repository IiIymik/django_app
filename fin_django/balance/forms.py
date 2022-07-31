from .models import Transaction
from django.forms import ModelForm, MultipleChoiceField, TextInput, RadioSelect, DecimalField, CharField


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ["type", "category", "amount"]
        choices = [('credit', 'credit'), ('debet', 'debet')]
        type = MultipleChoiceField(widget=RadioSelect, choices=choices)
        amount = DecimalField(required=True),
        category = CharField(widget=TextInput(attrs={
                'class': 'form-control',
                   }))


