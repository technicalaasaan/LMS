"""LMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from library.urls import library_router
from library.views import home, logout, Cards, add_book, BookCreateView, login, BookListView, BookDetailView, BookUpdateView, BookDeleteView, Home


urlpatterns = [
    path('', Home.as_view()),
    path('card/', Cards.as_view(), name='cards'),
    path('add', BookCreateView.as_view()),
    path('book/', BookListView.as_view()),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('books/', add_book),
    path('book/<pk>/', BookDetailView.as_view()),
    path('book/<pk>/update', BookUpdateView.as_view()),
    path('book/<pk>/delete', BookDeleteView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(library_router.urls))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)