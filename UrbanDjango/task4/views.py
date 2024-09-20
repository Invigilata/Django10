from django.shortcuts import render


def platform_view(request):
    return render(request, 'fourth_task/platform.html')


def games_view(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay2']
    return render(request, 'fourth_task/games.html', {'games': games})


def cart_view(request):
    return render(request, 'fourth_task/cart.html')

