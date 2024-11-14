from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

# Home page
def index(request):
    return render(request, 'motor/index.html')

# Product list by category
def product_list(request, category):
    products = Product.objects.filter(category=category)
    return render(request, 'motor/product_list.html', {'products': products, 'category': category})

# Product detail and add to cart from detail view
def product_detail(request, product_id):
    print(f"Session Cart ID: {request.session.get('cart_id')}")
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        # Retrieve or create cart for the session
        cart = get_cart(request)

        # Add product to cart, updating quantity if already exists
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()

        return redirect('cart')
    return render(request, 'motor/product_detail.html', {'product': product})

# View cart contents
# def cart_view(request):
#     cart = get_cart(request)
#     return render(request, 'motor/cart.html', {'cart': cart})

# View cart contents
def cart_view(request):
    cart = get_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)  # Fetch items in the cart
    return render(request, 'motor/cart.html', {'cart': cart, 'cart_items': cart_items})


# Add product to cart directly from product list or other pages
def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        quantity = int(request.POST.get('quantity', 1))

        # Retrieve or create cart for the session
        cart = get_cart(request)

        # Add product to cart, updating quantity if already exists
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if created:
            cart_item.quantity = quantity
        else:
            cart_item.quantity += quantity
        cart_item.save()

        return redirect('cart')
    return redirect('product_detail', product_id=product_id)

# Remove item from cart
def remove_from_cart(request, item_id):
    if request.method == 'POST':
        cart = get_cart(request)

        # Remove item from cart if it exists
        cart_item = get_object_or_404(CartItem, id=item_id, cart=cart)
        cart_item.delete()

        # Refresh cart to ensure items are updated
        cart.refresh_from_db()

        # If the cart is now empty, remove cart_id from session
        if not cart.items.exists():
            del request.session['cart_id']
            request.session.modified = True # Ensure session changes are saved

        return redirect('cart')

# Helper function to get or create the cart from the session
def get_cart(request):
    cart_id = request.session.get('cart_id')
    if not cart_id:  # If there’s no cart_id in the session
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id  # Save the new cart ID to the session
    else:
        cart = Cart.objects.filter(id=cart_id).first()
        if not cart:  # If no cart found, create a new one
            cart = Cart.objects.create()
            request.session['cart_id'] = cart.id
    return cart
