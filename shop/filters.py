import operator
from functools import reduce

import django_filters
from django import forms
from django.db.models import Q

from shop.models import Order, Address, Author, Book, Bookauthor, Color, Cover, Feedback, Genre, Material, Payment, \
    Publisher


class BookFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr="icontains", label="Название")
    author = django_filters.CharFilter(method='filter_by_author', label="Автор")

    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte', label="Цена",
                                             widget=forms.NumberInput)
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte', label="", widget=forms.NumberInput)

    AV_CHOICES = (
        (1, "В наличии"),
        (0, "Нет в наличии")

    )
    available = django_filters.ChoiceFilter(field_name='available', label="В наличии", choices=AV_CHOICES)

    SALE_CHOICES = (
        (1, "Со скидкой"),
        (0, "Без скидки")

    )
    sale = django_filters.ChoiceFilter(method='filter_by_sale', label="Скидка", choices=SALE_CHOICES)

    id_genre = django_filters.ModelChoiceFilter(
        label="Жанр",
        queryset=Genre.objects.all()
    )

    id_publisher = django_filters.ModelChoiceFilter(
        label="Издательство",
        queryset=Publisher.objects.all()
    )

    id_cover__id_color = django_filters.ModelChoiceFilter(
        label="Цвет",
        queryset=Color.objects.all()
    )

    id_cover__id_material = django_filters.ModelChoiceFilter(
        label="Тип обложки",
        queryset=Material.objects.all()
    )

    year__gte = django_filters.NumberFilter(field_name='year', lookup_expr='gte', label="Год издания",
                                            widget=forms.NumberInput)
    year__lte = django_filters.NumberFilter(field_name='year', lookup_expr='lte', label="", widget=forms.NumberInput)

    class Meta:
        model = Book
        fields = []

    def filter_by_author(self, queryset, name, value):
        lookups = ['bookauthor__id_author__last_name', 'bookauthor__id_author__first_name',
                   'bookauthor__id_author__second_name']
        val = value.split(sep=" ")
        or_queries = []
        for each_val in val:
            or_queries += [Q(**{lookup: each_val}) for lookup in lookups]
        return queryset.filter(reduce(operator.or_, or_queries))

    def filter_by_sale(self, queryset, name, value):
        if int(value) > 0:
            return queryset.filter(sale__gt=0)
        else:
            return queryset.filter(sale=0)
