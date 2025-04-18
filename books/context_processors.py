def cart_count(request):
    cart = request.session.get('cart', {})
    if isinstance(cart, dict):
        return {'cart_count': sum(cart.values())}
    elif isinstance(cart, list):  # legacy support
        return {'cart_count': len(cart)}
    return {'cart_count': 0}
