from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm  # 👈 import the custom form


from .models import Book, Order
import matplotlib.pyplot as plt
import io
import urllib, base64
from collections import Counter


# ---------- Custom Login ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            next_url = request.GET.get('next') or reverse('book_list')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'books/login.html')


# ---------- Registration ----------
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('book_list')
        else:
            messages.error(request, "Please fix the errors below.")
    else:
        form = CustomUserCreationForm()

    return render(request, 'books/register.html', {'form': form})



# ---------- Book List + Filters ----------
@login_required
def book_list(request):
    title_query = request.GET.get('title')
    author_query = request.GET.get('author')

    books = Book.objects.all()
    if title_query:
        books = books.filter(title__icontains=title_query)
    if author_query:
        books = books.filter(author__name__icontains=author_query)

    all_titles = Book.objects.values_list('title', flat=True).distinct()
    all_authors = Book.objects.values_list('author__name', flat=True).distinct()

    return render(request, 'books/book_list.html', {
        'books': books,
        'all_titles': all_titles,
        'all_authors': all_authors,
    })


# ---------- Book Detail ----------
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


# ---------- Add to Cart ----------
@login_required
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    messages.success(request, "Book added to cart.")
    return redirect('book_list')


# ---------- View Cart ----------
@login_required
def view_cart(request):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):  # Legacy support
        new_cart = {}
        for pk in cart:
            pk_str = str(pk)
            new_cart[pk_str] = new_cart.get(pk_str, 0) + 1
        cart = new_cart
        request.session['cart'] = cart

    if not cart:
        return render(request, 'books/cart.html', {'cart_data': {}})

    book_ids = [int(pk) for pk in cart.keys()]
    books = Book.objects.filter(pk__in=book_ids)
    cart_data = {book: cart[str(book.pk)] for book in books}

    return render(request, 'books/cart.html', {'cart_data': cart_data})


# ---------- Place Order from Cart ----------
@login_required
def place_order_from_cart(request):
    cart = request.session.get('cart', {})
    book_ids = [int(pk) for pk in cart.keys()]
    books = Book.objects.filter(pk__in=book_ids)

    for book in books:
        quantity = cart[str(book.pk)]
        for _ in range(quantity):
            Order.objects.create(user=request.user, book=book)

    request.session['cart'] = {}  # Clear cart
    return redirect('order_success')


# ---------- Place Single Order ----------
@login_required
def place_order(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Order.objects.create(user=request.user, book=book)
    messages.success(request, "Your order for this book has been placed!")
    return redirect('book_detail', pk=pk)


# ---------- Order Success Page ----------
@login_required
def order_success(request):
    return render(request, 'books/order_success.html')


# ---------- Remove Entire Book from Cart ----------
@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    pk_str = str(pk)

    if pk_str in cart:
        del cart[pk_str]
        request.session['cart'] = cart
        messages.success(request, "Book removed from cart.")
    return redirect('view_cart')


# ---------- Increase/Decrease Quantity ----------
@require_POST
@login_required
def increase_quantity(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')


@require_POST
@login_required
def decrease_quantity(request, pk):
    cart = request.session.get('cart', {})
    pk_str = str(pk)

    if pk_str in cart:
        if cart[pk_str] > 1:
            cart[pk_str] -= 1
        else:
            del cart[pk_str]

    request.session['cart'] = cart
    return redirect('view_cart')


# ---------- Admin Dashboard ----------
@staff_member_required
def admin_dashboard(request):
    orders = Order.objects.all()
    order_counts = Counter(order.book.title for order in orders)

    titles = list(order_counts.keys())[:10]
    counts = list(order_counts.values())[:10]

    plt.figure(figsize=(10, 6))
    plt.barh(titles, counts, color='#7209b7')
    plt.xlabel("Number of Orders")
    plt.title("Top Ordered Books")
    plt.tight_layout()

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    chart_url = base64.b64encode(image_png).decode('utf-8')
    chart_uri = f'data:image/png;base64,{chart_url}'

    return render(request, 'books/admin_dashboard.html', {'chart': chart_uri})


# ---------- Reset Cart (for dev) ----------
@login_required
def reset_cart(request):
    request.session['cart'] = {}
    return HttpResponse("Cart has been reset. You can now safely go back.")
