from django.shortcuts import render, redirect, reverse, get_object_or_404


def view_cart(request):
    """A view that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, item_pk):
    """Add a quantity of the specified product to the cart"""
    cart = request.session.get('cart', {})

    new_quantity = int(request.POST['quantity'])
    old_quantity = cart.get(item_pk, 0)

    cart[item_pk] = new_quantity + old_quantity

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, item_pk):
    """Adjust the quantity of the specified product to the specified amount"""
    new_quantity = int(request.POST['quantity'])
    cart = request.session.get('cart', {})

    if new_quantity > 0:
        cart[item_pk] = new_quantity
    else:
        del cart[item_pk]

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
