from django.shortcuts import render, redirect
from MainApp.forms import SnippetForm
from .models import Snippet
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .models import Profile


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request,
                                  'pages/index.html')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'pages/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            # Create the user profile
            Profile.objects.create(user=new_user)
            return render(request,
                          'pages/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'pages/register.html',
                  {'user_form': user_form})


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
            'form': form,
        }
        return render(request, 'pages/add_snippet.html', context)

    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect("index_page")
        return render(request, 'pages/add_snippet.html', {'form': form})


def snippets_page(request):
    snip = Snippet.objects.order_by('-id').filter(is_published=True).filter(private=False)
    pagename = 'Просмотр сниппетов'
    return render(request, 'pages/view_snippets.html',  {'pagename': pagename, 'snip': snip})


def snippets_page_hidden(request):
    snip = Snippet.objects.order_by('-id').filter(private=False)
    pagename = 'Просмотр сниппетов'
    return render(request, 'pages/view_snippets_hidden.html',  {'pagename': pagename, 'snip': snip})


def my_snippets_page(request):
    snip = Snippet.objects.order_by('-id').filter(is_published=True).filter(author=request.user).filter(private=False)
    pagename = 'Просмотр моих сниппетов'
    return render(request, 'pages/view_my_snippets.html',  {'pagename': pagename, 'snip': snip})


def my_snippets_page_hidden(request):
    snip = Snippet.objects.order_by('-id').filter(author=request.user).filter(private=False)
    pagename = 'Просмотр моих сниппетов'
    return render(request, 'pages/view_my_snippets_hidden.html',  {'pagename': pagename, 'snip': snip})


def my_snippets_page_private(request):
    snip = Snippet.objects.order_by('-id').filter(author=request.user).filter(is_published=True)
    pagename = 'Просмотр моих сниппетов'
    return render(request, 'pages/view_my_snippets_private.html',  {'pagename': pagename, 'snip': snip})


def my_snippets_page_hidden_private(request):
    snip = Snippet.objects.order_by('-id').filter(author=request.user)
    pagename = 'Просмотр моих сниппетов'
    return render(request, 'pages/view_my_snippets_hidden_private.html',  {'pagename': pagename, 'snip': snip})


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
