from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_katalog = CatalogItem.objects.all()
    context = {
    'list_barang': data_katalog,
    'nama': 'Yeira',
    'id': '2106751726'
    }
    return render(request, "katalog.html", context)

