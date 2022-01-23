from django.shortcuts import render
from django.shortcuts import get_object_or_404

from .models import Accommodation
# from .models import ListOfCountries


def main(request):
    '''Главная страница'''
    # context =
    return render(request, 'mainapp/index.html')


def accommodations(request):
    '''Страница со списком всех продуктов'''
    title = 'размещение'

    list_of_accommodations = Accommodation.objects.filter(is_active=True)

    content = {
        'title': title,
        'list_of_accommodations': list_of_accommodations,
    }

    return render(request, 'mainapp/accommodations.html', content)


def accommodation(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'accommodation': get_object_or_404(Accommodation, pk=pk),
    }

    return render(request, 'mainapp/accommodation_details.html', content)
