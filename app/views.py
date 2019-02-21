from app.models import Book
from app.serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from rest_framework import renderers
import django_filters.rest_framework
from rest_framework import filters


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filter_backends = (filters.SearchFilter,)
    filter_backends = (filters.OrderingFilter,)

    # search_fields = ('name', 'title')
    # def get_queryset(self):
    #     # queryset = Book.objects.all()
    #     search = self.request.data.get('search')
    #     if search is not None:
    #         self.queryset = self.queryset.filter(book__context=search)
    #     return self.queryset
    @detail_route()
    def booklist(self, request, *args, **kwargs):
        book = Book.objects.filter(id=2)
        serializer = self.get_serializer(book, many=True)
        return Response(serializer.data)
    # @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # def highlight(self, request, *args, **kwargs):
    #     book = self.get_object()
    #     return Response(book.text)
