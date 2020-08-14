from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render, redirect

current_id = 0
cars = {"change_oil": [], "inflate_tires": [], "diagnostic": []}
idx = 0


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


def pop_id():
    global cars
    if len(cars["change_oil"]) >= 1:
        return cars["change_oil"].pop(0)
    elif len(cars["change_oil"]) == 0 and len(cars["inflate_tires"]) > 1:
        return cars["inflate_tires"].pop(0)
    elif len(cars["change_oil"]) == 0 and len(cars["inflate_tires"]) == 0 and len(cars["diagnostic"]) > 1:
        return cars["diagnostic"].pop(0)
    else:
        return None


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


class ProcessingView(View):
    template_name4 = "tickets/processing.html"
    template_next = "tickets/next.html"

    def get(self, request, *args, **kwargs):
        global cars


        oil = len(cars["change_oil"])
        tires = len(cars["inflate_tires"])
        diag = len(cars["diagnostic"])

        return render(request, self.template_name4, {"change_oil": oil, "inflate_tires": tires, "diagnostic": diag})

    def post(self, request, *args, **kwargs):
        global idx
        idx = pop_id()
        return render(request, self.template_next)
        #return redirect(self.template_next)

class NextView(View):
    template_name5 = "tickets/next.html"

    def post(self, request, *args, **kwargs):
        global idx
        idx = pop_id()
        return render(request, self.template_name5, {"id": idx})

    def get(self, request, *args, **kwargs):
        global idx
        return render(request, self.template_name5, {"id": idx})

