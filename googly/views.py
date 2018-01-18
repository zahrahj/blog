from django.http import JsonResponse
import requests 
from django.shortcuts import render

# Create your views here.
def place_search(request):
	key = "AIzaSyDJRkkgzicdVP3xrAZ0m48U5rSmm_XHtKI" 
	search = "Starbucks"
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key=%s&query=%s&region=kw"%(key, search)

	next_page_token = request.GET.get('next_page')
	if next_page_token:
		url += "&pagetoken=%s"%(next_page_token)



	response = requests.get(url).json()

	context = {
	"response": response
	}


	return render(request, 'place_search.html', context)

def place_detail(request):
	key = "AIzaSyDJRkkgzicdVP3xrAZ0m48U5rSmm_XHtKI" 
	place_id = request.GET.get('place_id')
	url = "https://maps.googleapis.com/maps/api/place/details/json?key=%s&placeid=%s"%(key, place_id)

	
	response = requests.get(url).json()

	context = {
	"response": response
	}
	

	return render(request, 'place_detail.html', context)
