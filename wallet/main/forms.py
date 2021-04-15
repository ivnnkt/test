from django.forms import ModelForm
from .models import Wallet, Transactions


#
#     def clean_age(self):
#         data = self.cleaned_data['age']
#
#         #Проверка возраста
#         if data < 18:
#             raise ValidationError('Вам должно быть больше чем 18 лет')
#
#         return data


class WalletForm(ModelForm):

    class Meta:
        model = Wallet
        fields = (
            'name',
        )


class TransactionsForm(ModelForm):

    class Meta:
        model = Transactions
        fields = (
            'wallet',
            'amount',
            'transaction_type',
            'description',
        )
