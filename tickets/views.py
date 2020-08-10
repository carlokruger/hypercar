from django.http import HttpResponse
from django.views import View
from django.shortcuts import render


current_id = 0
cars = {"change_oil": [], "inflate_tires": [], "diagnostic": []}


def get_id(service):
    global current_id
    global cars
    current_id += 1
    cars[service].append(current_id)
    return current_id


def get_wait_time(service):
    global cars
    if service == "change_oil":
        return (len(cars[service]) - 1) * 2
    elif service == "inflate_tires":
        return (len(cars["change_oil"]) * 2) + ((len(cars[service]) - 1) * 5)
    elif service == "diagnostic":
        return (len(cars["change_oil"]) * 2) + (len(cars["inflate_tires"]) * 5) + ((len(cars[service]) - 1) * 30)

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
        id = get_id("change_oil")
        wait_time = get_wait_time("change_oil")
        return render(request, self.template_name1, {'id': id, 'minutes_to_wait': wait_time})


class InflateTiresView(View):
    template_name2 = "get_ticket/inflate_tires.html"

    def get(self, request, *args, **kwargs):
        id = get_id("inflate_tires")
        wait_time = get_wait_time("inflate_tires")
        return render(request, self.template_name2, {'id': id, 'minutes_to_wait': wait_time})


class DiagnosticView(View):
    template_name3 = "get_ticket/diagnostic.html"

    def get(self, request, *args, **kwargs):
        id = get_id("diagnostic")
        wait_time = get_wait_time("diagnostic")
        return render(request, self.template_name3, {'id': id, 'minutes_to_wait': wait_time})