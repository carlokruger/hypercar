from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


class WelcomeView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('<h2>Welcome to the Hypercar Service!</h2>')


class MenuView(View):
    template_name = "tickets/menu.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

