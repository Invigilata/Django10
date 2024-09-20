from django.shortcuts import render
from .forms import UserRegister


def sign_up_by_html(request):
    users = ['Vasya', 'Petya', 'Masha']
    info = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif int(age) < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['message'] = f'Приветствуем, {username}!'
            return render(request, 'fifth_task/registration_page.html', info)

    return render(request, 'fifth_task/registration_page.html', info)


def sign_up_by_django(request):
    form = UserRegister(request.POST or None)
    users = ['Vasya', 'Petya', 'Masha']
    info = {'form': form}

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        repeat_password = form.cleaned_data['repeat_password']
        age = form.cleaned_data['age']

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        else:
            info['message'] = f'Приветствуем, {username}!'
            return render(request, 'fifth_task/registration_page.html', info)

    return render(request, 'fifth_task/registration_page.html', info)
