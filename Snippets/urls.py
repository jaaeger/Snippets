from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index_page'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list/', views.snippets_page, name='snippets_page'),
    path('snippets/list/<int:pk>', views.SnippetsDetailView.as_view(), name='snippet_detail'),
    path('snippets/list/<int:pk>/update', views.SnippetsUpdateView.as_view(), name='snippet_update'),
    path('snippets/list/<int:pk>/delete', views.SnippetsDeleteView.as_view(), name='snippet_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
