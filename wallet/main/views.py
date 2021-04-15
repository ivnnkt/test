from django.views import generic
from .models import Wallet, Transactions
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WalletForm, TransactionsForm
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError


class WalletListView(LoginRequiredMixin, generic.ListView):
    """Полный список кошельков.
    """
    model = Wallet
    template_name = 'main/wallets.html'


class WalletDetailView(LoginRequiredMixin, generic.DetailView):
    """Страница кошелька
    """
    model = Wallet
    template_name = 'main/wallet.html'


class WalletCreateView(LoginRequiredMixin, generic.CreateView):
    """Страница добавления кошелька
    """
    model = Wallet
    form_class = WalletForm
    success_url = '/wallets'


class WalletUpdaitView(LoginRequiredMixin, generic.UpdateView):
    """Страница редактирования кошелька
    """
    model = Wallet
    form_class = WalletForm
    template_name = 'main/wallet_edit.html'
    success_url = '/wallets'


class WalletDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Страница удаления кошелька
    """
    model = Wallet
    template_name = 'main/wallet_del.html'
    success_url = '/wallets'


class TransactionListView(LoginRequiredMixin, generic.ListView):
    """Страница истории всех транзакций
    """
    model = Transactions
    template_name = 'main/transactions.html'


class TransactionCreateView(LoginRequiredMixin, generic.CreateView):
    """Страница создания транзакции
    """
    model = Transactions
    form_class = TransactionsForm
    success_url = '/wallets'

    def form_valid(self, form):
        obj = form.instance
        wallet = Wallet.objects.get(name=obj.wallet)
        if obj.transaction_type=='plus':
            wallet.balance += obj.amount
            wallet.save()
            self.object = form.save()
        else:
            if obj.amount > wallet.balance:
                raise ValidationError('На счете кошелька недостаточно средств!')
            else:
                wallet.balance -= obj.amount
                wallet.save()
                self.object = form.save()
        return HttpResponseRedirect('/wallets')
