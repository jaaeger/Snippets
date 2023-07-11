from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from .models import Snippet
from django.views.generic import DetailView, UpdateView, DeleteView


def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("redirect_url")
        return render(request, 'pages/add_snippet.html', {'form': form})


def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {
            'pagename': 'Добавление нового сниппета',
            'form': form
        }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index_page")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    snip = Snippet.objects.order_by('-id').filter(is_published=True)
    pagename = 'Просмотр сниппетов'
    return render(request, 'pages/view_snippets.html',  {'pagename': pagename, 'snip': snip})

def snippets_page_hidden(request):
    snip = Snippet.objects.order_by('-id')
    pagename = 'Просмотр сниппетов'
    return render(request, 'pages/view_snippets_hidden.html',  {'pagename': pagename, 'snip': snip})


class SnippetsDetailView(DetailView):
    model = Snippet
    template_name = 'pages/view_snip.html'
    context_object_name = 'snippet'

class SnippetsUpdateView(UpdateView):
    model = Snippet
    template_name = 'pages/add_snippet.html'
    form_class = SnippetForm

class SnippetsDeleteView(DeleteView):
    model = Snippet
    success_url = '/snippets/list/'
    template_name = 'pages/delete_snippet.html'