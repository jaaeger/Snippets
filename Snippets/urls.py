from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index_page'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.snippets_page, name='snippets_page'),
    path('snippets/1', views.snippet, name='snippet'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
