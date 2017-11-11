from django.shortcuts import render

def index(request):
   return render(request, 'diffuse/index.html')

def home(request, game_id):
	return render(request, 'diffuse/home.html')

def diffuse(request, game_id):
	return render(request, 'diffuse/diffuse.html')

def history(request, game_id):
	return render(request, 'diffuse/history.html')
