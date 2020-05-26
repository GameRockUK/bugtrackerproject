from django.shortcuts import render, redirect, reverse

# Create your views here.


def view_cart(request):
    """A view to view the cart contents"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a multiple items to the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = cart.get(id, quantity)
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('index'))


def adjust_cart(request, id):
    """Adjust quantity of specified product"""
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
