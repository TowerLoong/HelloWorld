from django.shortcuts import render
from django.views import generic

from django.http import HttpResponse


def index(request):
    return HttpResponse("Tao Hello, world. You're at the main index!!!")


# 暫定ポータル画面へ移動
class Home(generic.TemplateView):
    template_name = 'main/home.html'

    def get(self, request, *args, **kwargs):
        context = super(Home, self).get_context_data()
        context.update({'my_message': 'Welcome to my site'})
        return render(request, 'main/home.html', context)
