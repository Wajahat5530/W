from django.contrib import admin
from django.urls import path
from news.views import sports, home,business,entertainment

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),          # home page
    path('sports/', sports,name='sports'),  # sports page
    path('business/', business,name='business'),
    path('entertainment/',entertainment,name='entertainment')
]