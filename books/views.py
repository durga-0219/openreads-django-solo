from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth.models import User
from .models import Book, Order, Author
from .forms import CustomUserCreationForm
import matplotlib.pyplot as plt
import io
import base64
from collections import Counter
import csv

# ---------- Custom Login ----------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('custom_admin_dashboard')
            return redirect('book_list')
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
    year_query = request.GET.get('year')
    books = Book.objects.all()
    if title_query:
        books = books.filter(title=title_query)
    if author_query:
        books = books.filter(author__name=author_query)
    if year_query:
        books = books.filter(year=year_query)
    all_titles = Book.objects.values_list('title', flat=True).distinct()
    all_authors = Book.objects.values_list('author__name', flat=True).distinct()
    all_years = Book.objects.values_list('year', flat=True).distinct()
    return render(request, 'books/book_list.html', {
        'books': books,
        'all_titles': all_titles,
        'all_authors': all_authors,
        'all_years': sorted(all_years, reverse=True),
    })


# ---------- Book Detail ----------
@login_required
def book_detail(request, pk):
    storage = messages.get_messages(request)
    list(storage)
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


# ---------- Cart Management ----------
@login_required
def add_to_cart(request, pk):
    cart = request.session.get('cart', {})
    cart[str(pk)] = cart.get(str(pk), 0) + 1
    request.session['cart'] = cart
    return redirect('book_list')

@login_required
def view_cart(request):
    cart = request.session.get('cart', {})
    if isinstance(cart, list):
        cart = {str(pk): cart.count(pk) for pk in cart}
        request.session['cart'] = cart
    if not cart:
        return render(request, 'books/cart.html', {'cart_data': {}, 'total_amount': 0})
    book_ids = [int(pk) for pk in cart.keys()]
    books = Book.objects.filter(pk__in=book_ids)
    cart_data = {book: cart[str(book.pk)] for book in books}
    total_amount = sum(book.price * quantity for book, quantity in cart_data.items())
    return render(request, 'books/cart.html', {'cart_data': cart_data, 'total_amount': total_amount})

@login_required
def place_order_from_cart(request):
    cart = request.session.get('cart', {})
    books = Book.objects.filter(pk__in=map(int, cart.keys()))
    for book in books:
        for _ in range(cart[str(book.pk)]):
            Order.objects.create(user=request.user, book=book)
    request.session['cart'] = {}
    return redirect('order_success')

@login_required
def place_order(request, pk):
    book = get_object_or_404(Book, pk=pk)
    Order.objects.create(user=request.user, book=book)
    messages.success(request, "Your order for this book has been placed!")
    return redirect('book_detail', pk=pk)

@login_required
def order_success(request):
    return render(request, 'books/order_success.html')

@login_required
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    cart.pop(str(pk), None)
    request.session['cart'] = cart
    return redirect('view_cart')

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
    if str(pk) in cart:
        cart[str(pk)] -= 1
        if cart[str(pk)] <= 0:
            del cart[str(pk)]
    request.session['cart'] = cart
    return redirect('view_cart')

@login_required
def reset_cart(request):
    request.session['cart'] = {}
    return HttpResponse("Cart has been reset. You can now safely go back.")


# ---------- Admin Dashboard ----------
@login_required
def custom_admin_dashboard(request):
    if not request.user.is_superuser:
        return redirect('book_list')

    total_books = Book.objects.count()
    total_users = User.objects.count()
    total_orders = Order.objects.count()

    order_counts = Counter(order.book.title for order in Order.objects.all())
    top_titles = list(order_counts.keys())[:10]
    top_counts = list(order_counts.values())[:10]

    plt.figure(figsize=(10, 6))
    plt.barh(top_titles, top_counts, color='purple')
    plt.xlabel("Orders")
    plt.title("Top Ordered Books")
    plt.tight_layout()
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    chart_data = base64.b64encode(buffer.getvalue()).decode()
    buffer.close()

    all_titles = Book.objects.values_list('title', flat=True).distinct()
    all_authors = Book.objects.values_list('author__name', flat=True).distinct()
    all_years = Book.objects.values_list('year', flat=True).distinct()

    selected_title = request.GET.get('title')
    selected_author = request.GET.get('author')
    selected_year = request.GET.get('year')

    books = Book.objects.all()
    if selected_title:
        books = books.filter(title=selected_title)
    if selected_author:
        books = books.filter(author__name=selected_author)
    if selected_year:
        books = books.filter(year=selected_year)

    return render(request, 'books/custom_admin_dashboard.html', {
        'total_books': total_books,
        'total_users': total_users,
        'total_orders': total_orders,
        'chart': f'data:image/png;base64,{chart_data}',
        'books': books,
        'all_titles': all_titles,
        'all_authors': all_authors,
        'all_years': sorted(all_years, reverse=True),
        'selected_title': selected_title,
        'selected_author': selected_author,
        'selected_year': selected_year,
    })


# ---------- Admin Book Management ----------
@login_required
def update_book_price(request, pk):
    if not request.user.is_superuser:
        return redirect('book_list')
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        new_price = request.POST.get('price')
        if new_price:
            try:
                book.price = float(new_price)
                book.save()
                messages.success(request, f"Updated price for {book.title}")
            except ValueError:
                messages.error(request, "Invalid price entered.")
        return redirect('custom_admin_dashboard')
    return render(request, 'books/update_book_price.html', {'book': book})


@login_required
def add_book(request):
    if not request.user.is_superuser:
        return redirect('book_list')
    if request.method == 'POST':
        data = request.POST
        author, _ = Author.objects.get_or_create(name=data.get('author'))
        Book.objects.create(
            title=data.get('title'),
            author=author,
            year=data.get('year'),
            price=data.get('price'),
            image_url=data.get('image_url'),
            description=data.get('description'),
            isbn=data.get('isbn'),
            publisher=data.get('publisher'),
            rating=data.get('rating') or 4
        )
        messages.success(request, "Book added successfully.")
        return redirect('custom_admin_dashboard')
    return render(request, 'books/add_book.html')


@login_required
def delete_book(request, pk):
    if not request.user.is_superuser:
        return redirect('book_list')
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    messages.success(request, f"{book.title} has been deleted.")
    return redirect('custom_admin_dashboard')


# ---------- Export CSV ----------
@login_required
def export_books_csv(request):
    if not request.user.is_superuser:
        return HttpResponse("Unauthorized", status=403)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Year', 'Price'])
    for book in Book.objects.all():
        writer.writerow([book.title, book.author.name, book.year, book.price])
    return response

@login_required
def export_filtered_books_csv(request):
    if not request.user.is_superuser:
        return HttpResponse("Unauthorized", status=403)

    title = request.GET.get('title')
    author = request.GET.get('author')
    year = request.GET.get('year')

    books = Book.objects.all()
    if title:
        books = books.filter(title=title)
    if author:
        books = books.filter(author__name=author)
    if year:
        books = books.filter(year=year)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="filtered_books.csv"'
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Year', 'Price'])
    for book in books:
        writer.writerow([book.title, book.author.name, book.year, book.price])
    return response

@login_required
def admin_user_list(request):
    if not request.user.is_superuser:
        return redirect('book_list')
    users = User.objects.all()
    return render(request, 'books/user_list.html', {'users': users})


@login_required
def admin_order_list(request):
    if not request.user.is_superuser:
        return redirect('book_list')
    orders = Order.objects.all().select_related('user', 'book')
    return render(request, 'books/order_list.html', {'orders': orders})


@login_required
def admin_book_list(request):
    if not request.user.is_superuser:
        return redirect('book_list')
    books = Book.objects.all()
    return render(request, 'books/admin_book_list.html', {'books': books})



