from django.shortcuts import render


def func_view(request):
    return render(request, 'second_task/func_template.html')


from django.views import View


class ClassView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')

