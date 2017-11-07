from django.shortcuts import get_object_or_404
from products.models import Product


def cart_contents(request):
    """
    Makes the cart contents available in any template.
    """
    cart = request.session.get('cart', {})

    cart_items = {
        pk: {'quantity': quantity, 'product': get_object_or_404(Product, pk=pk)}
        for pk, quantity in cart.items()
    }
    product_count = sum(item['quantity'] for item in cart_items.values())
    total = sum(item['quantity'] * item['product'].price for item in cart_items.values())

    return {'cart_items': cart_items, 'total': total, 'product_count': product_count}
