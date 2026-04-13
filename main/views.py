from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    status = None
    errors = []
    name = ''
    email = ''
    message = ''

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        if not name:
            errors.append('Моля, въведете име.')
        if not email:
            errors.append('Моля, въведете email.')
        else:
            try:
                validate_email(email)
            except ValidationError:
                errors.append('Моля, въведете валиден email адрес.')
        if not message:
            errors.append('Моля, въведете съобщение.')

        if not errors:
            status = 'success'

    return render(request, 'main/contact.html', {
        'status': status,
        'errors': errors,
        'name': name,
        'email': email,
        'message': message,
    })