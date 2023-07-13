from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from MainApp import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_page, name='index_page'),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list/', views.snippets_page, name='snippets_page'),
    path('snippets/list_hidden/', views.snippets_page_hidden, name='snippets_page_hidden'),
    path('snippets/list/<int:pk>', views.SnippetsDetailView.as_view(), name='snippet_detail'),
    path('snippets/list/<int:pk>/update', views.SnippetsUpdateView.as_view(), name='snippet_update'),
    path('snippets/list/<int:pk>/delete', views.SnippetsDeleteView.as_view(), name='snippet_delete'),
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/index.html'), name='logout'),
    path('snippets/my_list/', views.my_snippets_page, name='my_snippets_page'),
    path('snippets/my_list_hidden/', views.my_snippets_page_hidden, name='my_snippets_page_hidden'),
    path('snippets/my_list_private/', views.my_snippets_page_private, name='my_snippets_page_private'),
    path('snippets/my_list_hidden_private/', views.my_snippets_page_hidden_private, name='my_snippets_page_hidden_private'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
