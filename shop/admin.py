from django.contrib import admin

from shop.models import Orderbook, Address, Author, Book, Bookauthor, Color, Cover, Feedback, Genre, Material, \
    Payment, Publisher, Order


class AddressAdmin(admin.ModelAdmin):
    list_display = ['city', 'street', 'house_number']
    list_filter = ['city']


admin.site.register(Address, AddressAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'second_name']


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'stock', 'available', 'sale']
    list_filter = ['available']
    list_editable = ['stock', 'available', 'sale']
    search_fields = ['title']

admin.site.register(Book, BookAdmin)


class BookauthorAdmin(admin.ModelAdmin):
    list_display = ['id_book', 'id_author']


admin.site.register(Bookauthor, BookauthorAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['color']


admin.site.register(Color, ColorAdmin)


class CoverAdmin(admin.ModelAdmin):
    list_display = ['id_material', 'id_color']


admin.site.register(Cover, CoverAdmin)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_book', 'rating']
    list_filter = ['id_user']


admin.site.register(Feedback, FeedbackAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ['genre']


admin.site.register(Genre, GenreAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ['material']


admin.site.register(Material, MaterialAdmin)


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payment']


admin.site.register(Payment, PaymentAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'city']
    list_filter = ['country', 'city']


admin.site.register(Publisher, PublisherAdmin)


class OrderbookAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'id_book', 'quantity', 'is_ordered']
    list_filter = ['id_user']


admin.site.register(Orderbook, OrderbookAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id_order', 'id_user', 'ordered_at', 'is_ordered', 'is_bought']
    list_filter = ['id_user']
    list_editable = ['is_bought']


admin.site.register(Order, OrderAdmin)
