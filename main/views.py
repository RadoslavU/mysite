from django.shortcuts import render

from .forms import ContactMessageForm


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    status = None

    if request.method == 'POST':
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            status = 'success'
            form = ContactMessageForm()
    else:
        form = ContactMessageForm()

    return render(request, 'main/contact.html', {
        'form': form,
        'status': status,
    })