from django.views import generic
from .models import Wallet, Transactions
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import WalletForm, TransactionsForm
from django.http import HttpResponseRedirect, HttpResponse


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

    def get_context_data(self, **kwargs):
        obj = self.object
        context = super(WalletDetailView, self).get_context_data(**kwargs)
        context['transactions'] = Transactions.objects.filter(wallet=obj.id)
        return context


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
        if obj.transaction_type == 'plus':
            wallet.balance += obj.amount
            wallet.save()
            self.object = form.save()
        else:
            if obj.amount > wallet.balance:
                return HttpResponse('<h1>На счете кошелька недостаточно средств!</h1>')
            else:
                wallet.balance -= obj.amount
                wallet.save()
                self.object = form.save()
        return HttpResponseRedirect('/wallets')


class TransactionDeleteView(LoginRequiredMixin, generic.DeleteView):
    """Страница удаления транзакции
    """
    model = Transactions
    template_name = 'main/transaction_del.html'
    success_url = '/wallets'
