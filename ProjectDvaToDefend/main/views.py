from django.shortcuts import render, redirect, get_object_or_404
from main.models import Famous_Persons
from .forms import DopContForm, EmailForm, Famous_Persons_Form
from django.views.generic import DetailView, UpdateView, DeleteView
from .forms import NewUserForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import LoginForm
from django.http import HttpResponse
from django.core.mail import send_mail




def index(request):
    return render(request, 'main/index.html')


def filling(request):
    error_message = ''

    if request.method == 'POST':
        form = Famous_Persons_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/recordings')
        else:
            error = 'Форма заполнена некорректно'


    form = Famous_Persons_Form()

    data = {
        'form': form,
        'error_message': error_message
    }

    return render(request, 'main/filling.html', data)

def dopcontent(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dopcontent')


    form = EmailForm()

    data = {
        'form': form
    }
    return render(request, 'main/dopcontent.html', data)

def dopcontent_fill(request):
    if request.method == 'POST':
        dopcont_form = DopContForm(request.POST)
        if dopcont_form.is_valid():
            dopcont_form.save()
            return redirect('/dopcontent')


    dopcont_form = DopContForm()

    data = {
        'form': dopcont_form,
    }

    return render(request, 'main/dopcontent_fill.html', data)

    
def recordings(request):
    persons = Famous_Persons.objects.all()
    return render(request, 'main/recordings.html', {'persons': persons})

class filling_DetailView(DetailView):
    model = Famous_Persons
    template_name = 'main/details_view.html'
    context_object_name = 'famous_persons'

# Для добавления slug
def show_post(request, post_slug):
    post = get_object_or_404(Famous_Persons, slug = post_slug)
    context = {'post':post}
    return render(request, 'main/post.html', context=context)


class filling_UpdateView(UpdateView):
    model = Famous_Persons
    template_name = 'main/filling.html'

    form_class = Famous_Persons_Form

class filling_DeleteView(DeleteView):
    model = Famous_Persons
    template_name = 'main/filling_delete.html'
    success_url = '/recordings'

def zona(request):
    return render(request, 'main/zona.html')



def iitu(request):
    return render(request, 'main/iitu.html')

def iitu2(request):
    return render(request, 'main/iitu2.html')

def iitu3(request):
    return render(request, 'main/iitu3.html')

def iitu4(request):
    return render(request, 'main/iitu4.html')



def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			messages.success(request, "Registration successful." )
			return redirect('/login')
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, template_name="main/register.html", context={"register_form":form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})

def sendler(request):
    send_mail('Django email', 
    'Привет, данное письмо было отправлено с помощью Django',
    '',
    [''],
    fail_silently=False)
    return render(request, 'main/sendler.html')