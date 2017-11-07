from django import template

register = template.Library()


@register.filter(name='quantity_in_cart')
def quantity_in_cart(item_pk, cart_items):
    item_in_cart = cart_items.get(str(item_pk))
    if item_in_cart:
        return item_in_cart['quantity']
    return 0
