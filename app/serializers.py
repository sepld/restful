from rest_framework import serializers
from models import Book


# HyperlinkedModelSerializer
class BookSerializer(serializers.ModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name='book-highlight', format='html')
    class Meta:
        model = Book
        fields = ('url', 'id', 'name', 'title', 'text')
