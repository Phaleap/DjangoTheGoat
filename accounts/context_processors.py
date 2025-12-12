def cart_context(request):
    cart = request.session.get('cart', {})
    
    total_items = sum(item['qty'] for item in cart.values())
    total_price = sum(item['qty'] * item['price'] for item in cart.values())

    return {
        'navbar_cart': cart,
        'navbar_cart_count': total_items,
        'navbar_cart_total': total_price,
    }
