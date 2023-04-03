from rest_framework import routers
from .views import BooksViewSet

library_router = routers.DefaultRouter()

library_router.register('books', BooksViewSet)
