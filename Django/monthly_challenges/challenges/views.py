from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def january(request):
    return HttpResponse("This works!")



def february(request):
    return HttpResponse("This is Febrero") 



def dynamic(request, month):
    monthResponses = {
        "january": "This is January!",
        "february": "This is February!",
        "march": "This is March!",
        "april": "This is April!",
        "may": "This is May!",
        "june": "This is June!",
        "july": "This is July!",
        "august": "This is August!",
        "september": "This is September!",
        "october": "This is October!",
        "november": "This is November!",
        "december": "This is December!"
    }
    if month.lower() in monthResponses:
        response = monthResponses[month.lower()]
    else:
        return HttpResponse("Invalid month!")  # Handle invalid month input
    return HttpResponse(response)  # Return the response for the month

