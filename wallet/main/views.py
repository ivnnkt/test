from django.shortcuts import render


def index(request):
    """Главная страница. Выводится список товаров,
    цена если turn_on_block = True, и пример работы фильтра revers_string.
    """
    # prod = Product.objects.all()

    return render(
        request,
        'main/index.html',
        {
            # 'prod': prod,
        }
    )
