from rest_framework import routers
from django.urls import path, include

from .api import BookViewSet
from .views import *

router = routers.DefaultRouter()
router.register(r'book', BookViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/document/book/all', getAllBooks, name='get-all-books'),
    path('api/document/book/create', createBook, name='create-book'),
    path('api/document/book/update/<int:id>', updateBook, name='update-book'),
    path('api/document/book/filter/', getBookWithFilter, name='write-in-excel'),
    path('api/document/book/writeInExcel/',
         writeInExcel, name='get-books-with-filter'),
    path('api/document/book/domCode/<str:domCode>',
         getBookByDomCode, name='get-by-domCode'),
]
