from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
from rest_framework.exceptions import ValidationError

class BookFilter(filters.FilterSet):
    book_genre = filters.CharFilter(field_name='genre', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['genre']

class BookList(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter

class BookDetails(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer