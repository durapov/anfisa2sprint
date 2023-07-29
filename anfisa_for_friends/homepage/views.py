from django.shortcuts import render

from ice_cream.models import IceCream

def index(request):
#    template = 'homepage/index.html'
#    return render(request, template)

    template_name = 'homepage/index.html'
# Запрос:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        is_published=True, 
        is_on_main=True,
        category__is_published=True        
        )



# Возьмём нужное. А ненужное не возьмём:
#   ice_cream_list = IceCream.objects.values('id', 'title', 'description')
#    IceCream.objects.filter(is_on_main__exact=True)
# ммодификатор exact используется по умолчанию,
# можно его не указывать.
# Так тоже сработает:
#    IceCream.objects.filter(is_on_main=True)
# Оба варианта приведут к одинаковому результату, 
# но второй читается проще, поэтому так все и пишут. 

 # Заключаем вызов методов в скобки
    # (это стандартный способ переноса длинных строк в Python);
    # каждый вызов пишем с новой строки, так проще читать код:
 #   ice_cream_list = IceCream.objects.values(
 #           'id', 'title', 'description'
        # Верни только те объекты, у которых в поле is_on_main указано True:
 #       )

    # Полученный из БД QuerySet передаём в словарь контекста:
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template_name, context) 