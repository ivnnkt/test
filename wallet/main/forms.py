from django.forms import ModelForm
from .models import Wallet, Transactions


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
