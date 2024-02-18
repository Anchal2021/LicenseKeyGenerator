from django.template import loader
from django.shortcuts import get_object_or_404
# Create your views here.
from django.http import HttpResponse,JsonResponse
from .Logic import KeyGenerator
from datetime import datetime

def home(request):
    template = loader.get_template('home.html') # getting our template
    return HttpResponse(template.render())       # rendering the template in HttpResponse

def generateKey(request):
    date=datetime.strptime(request.GET["expiry"], "%Y-%m-%d")
    key = KeyGenerator.KeyGenrator()
    generatedKey = key.GenerateKey(request.GET["software"],expiry_date=date)
    years,months,days = key.DaysConversionIntoMonthsAndYears(key.GetExpiryDays(generatedKey))
    return JsonResponse({'key': generatedKey, "years": years, "months": months, "days": days})