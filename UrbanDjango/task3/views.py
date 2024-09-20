from django.shortcuts import render


def platform_view(request):
    return render(request, 'third_task/platform.html')


def games_view(request):
    games = {
        'Atomic Heart': 'купить',
        'Cyberpunk 2077': 'купить',
        'PayDay2': 'купить'
    }
    return render(request, 'third_task/games.html', {'games': games})


def cart_view(request):
    return render(request, 'third_task/cart.html')

