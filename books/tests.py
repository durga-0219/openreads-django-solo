from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Author, Book, Order

class BookTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.superuser = User.objects.create_superuser(username='admin', password='adminpass')

        self.author = Author.objects.create(name='Test Author')
        self.book = Book.objects.create(title='Test Book', author=self.author, year=2020, price=20.00)

    def test_book_list_view_redirects_for_guest(self):
        response = self.client.get(reverse('book_list'))
        self.assertRedirects(response, '/login/?next=/')

    def test_book_list_view_logged_in(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Book')

    def test_add_to_cart(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('add_to_cart', args=[self.book.pk]))
        self.assertRedirects(response, reverse('book_list'))
        session = self.client.session
        self.assertIn(str(self.book.pk), session.get('cart', {}))

    def test_place_order_from_cart(self):
        self.client.login(username='testuser', password='testpass')
        session = self.client.session
        session['cart'] = {str(self.book.pk): 2}
        session.save()

        response = self.client.post(reverse('place_order_from_cart'))
        self.assertRedirects(response, reverse('order_success'))

        orders = Order.objects.filter(user=self.user, book=self.book)
        self.assertEqual(orders.count(), 2)

    def test_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        })
        self.assertRedirects(response, reverse('book_list'))
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_cart_quantity_increase_and_decrease(self):
        self.client.login(username='testuser', password='testpass')
        self.client.get(reverse('add_to_cart', args=[self.book.pk]))
        self.client.post(reverse('increase_quantity', args=[self.book.pk]))
        session = self.client.session
        self.assertEqual(session['cart'][str(self.book.pk)], 2)
        self.client.post(reverse('decrease_quantity', args=[self.book.pk]))
        session = self.client.session
        self.assertEqual(session['cart'][str(self.book.pk)], 1)

    def test_cart_clears_after_order(self):
        self.client.login(username='testuser', password='testpass')
        session = self.client.session
        session['cart'] = {str(self.book.pk): 1}
        session.save()
        self.client.post(reverse('place_order_from_cart'))
        session = self.client.session
        self.assertEqual(session['cart'], {})

    def test_admin_add_book(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('add_book'), {
            'title': 'Admin Added Book',
            'author': 'Admin Author',
            'year': 2022,
            'price': 35.00
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Book.objects.filter(title='Admin Added Book').exists())

    def test_admin_update_book_price(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('update_book_price', args=[self.book.pk]), {
            'price': 99.99
        })
        self.assertEqual(response.status_code, 302)
        self.book.refresh_from_db()
        self.assertEqual(float(self.book.price), 99.99)

    def test_admin_delete_book(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('delete_book', args=[self.book.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Book.objects.filter(pk=self.book.pk).exists())
