from django.views import View
from django.views.generic import ListView, DetailView, TemplateView
from django.conf import settings
from django.http import JsonResponse

import stripe

from .models import Item


stripe.api_key = 'sk_test_51OZ7YYIrdHa24etgJLNgTgzefXNAVn4GG65uGsMDZ7FGQXwXzs3FCnKNrqaBukOLty4GgN7F4LIzple3RHuy4PMu00unuN1XvI'


class SuccessView(TemplateView):
    """Class for view success template"""
    template_name = 'products/success.html'


class CancelView(TemplateView):
    """Class for view cancel template"""
    template_name = 'products/cancel.html'


class ProductView(DetailView):
    """Class for view one item"""
    model = Item
    template_name = 'products/detail_product.html'
    context_object_name = 'product_item'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['pk_test_51OZ7YYIrdHa24etg9yEHj16yNdaAqgAmALRZ96OGaXXbRm9Koa1oM0pPYbH8qop7UHK3OyPqmP7X8ZG8BsrFXab800LMrNZKq9'] = 'pk_test_51OZ7YYIrdHa24etg9yEHj16yNdaAqgAmALRZ96OGaXXbRm9Koa1oM0pPYbH8qop7UHK3OyPqmP7X8ZG8BsrFXab800LMrNZKq9'
        return context


class HomeProductsView(ListView):
    """Class for view all items"""
    model = Item
    template_name = 'products/home.html'
    context_object_name = 'products'


class CreateCheckoutSessionView(View):
    """Class for create checkout session"""
    def get(self, request, *args, **kwargs):
        """function to return session id"""
        product_id = self.kwargs['pk']
        product = Item.objects.get(pk=product_id)
        domain = 'http://localhost:8000'
        session = stripe.checkout.Session.create(
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': product.name,
                    },
                    'unit_amount': product.price * 100,
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=domain + '/success/',
            cancel_url=domain + '/cancel/',
        )

        return JsonResponse({'id': session.id})
