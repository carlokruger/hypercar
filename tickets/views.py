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


class ChangeOilView(View):
    template_name1 = "get_ticket/change_oil.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name1)


class InflateTiresView(View):
    template_name2 = "get_ticket/inflate_tires.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name2)


class DiagnosticView(View):
    template_name3 = "get_ticket/diagnostic.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name3)