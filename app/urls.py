from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from app import views

router = DefaultRouter()
router.register(r'books', views.BookViewSet, 'book')

urlpatterns = [
    url(r'^', include(router.urls))
]
