from django.db import models


class Wallet(models.Model):
    """Модель Кошелёк.

    Название -- Произвольное название для кошелька/счета.

    Баланс -- Поле отображающее остаток в кошельке/на счете,
    по умолчанию 0, не может редактироваться на прямую, только
    через транзакции.
    """
    name = models.CharField(verbose_name="Название", max_length=250)
    balance = models.DecimalField(
        verbose_name="Баланс",
        max_digits=11,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name


class Transactions(models.Model):
    """Модель Транзакции.

    Кошелёк -- поле для указания кошелька к которому относится транзакция,
    используется для фильтрации при выводе истории транзакций по кошельку,
    и при создании транзакции.

    Сумма -- поле для указания суммы пополнения либо списания.

    Тип транзакции -- вполе для выбора типа транзакции "Пополнение" или
    "Списание", по умолчанию - "Списание".

    Описание -- поле для краткого описания транзакции, обязательное
    для заполнения.

    Дата -- при создании транзакции дата заполняется автоматически.
    """
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.CASCADE,
        verbose_name="Кошелёк"
    )
    amount = models.DecimalField(
        verbose_name="Сумма",
        max_digits=11,
        decimal_places=2,
    )
    transaction_type = models.CharField(
        verbose_name="Тип транзакции",
        max_length=5,
        choices=[('plus', 'Пополнение'), ('minus', 'Списание')],
        default='minus',
    )
    description = models.CharField(
        verbose_name="Описание",
        max_length=300,
        blank=False,
    )
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.description


