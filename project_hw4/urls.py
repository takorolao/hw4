from django.contrib import admin
from django.urls import path
from landing.views import AboutView, HomeView, ContactsView, IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', AboutView.as_view(), name='about-page'),
    path('home/', HomeView.as_view(), name='home-page'),
    path('contacts/', ContactsView.as_view(), name='contacts-page'),
    path('', IndexView.as_view(), name='index-page'),
]



