from rest_framework import serializers
from .models import Book
from django.contrib.auth.models import User

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'name',
            'author',
            'description',
            'price',
            'genre',
            'publication_date'
        ]
        extra_kwargs = {
            'id': {'read_only': True},
            'author': {'read_only': True},
            'genre': {'read_only': True},
            'publication_date': {'read_only': True},
        }
        