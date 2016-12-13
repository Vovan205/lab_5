from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

data = {'orders': []}
for i in range(1, 9):
    data['orders'].append(
        {
            'id': i,
            'title': '{0}{1}'.format('Заказ №', i),
            'description': '123',
            'text': '456',
            'date': '28.11.2016'
        }
    )


def main_page(request):
    return render(request, 'orders.html', data)


class OrderView(View):
    def get(self, request, id):
        data_order = {
            'order': data['orders'][int(id)-1]
        }
        return render(request, 'order.html', data_order)
