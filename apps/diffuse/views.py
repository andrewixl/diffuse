from django.shortcuts import render
import urllib2
import json

def index(request):
   return render(request, 'diffuse/index.html')

def view(request):
	return render(request, 'diffuse/view.html')

def home(request, game_id):
	return render(request, 'diffuse/home.html')

def diffuse(request, game_id):
	return render(request, 'diffuse/diffuse.html')

def history(request, game_id):
    response = urllib2.urlopen('http://b5b1e790.ngrok.io/api/ActiveGame')
    data = json.load(response)

    jsondata = {}
    for key, value in data.items():
        jsondata[key] = value

    rounds = jsondata['roundStatus']
    print rounds is str
    context = {
    # 'bombcode' : jsondata['code'],
    # 'spies' : jsondata['spies'],
    # 'players' : jsondata['players'],
    # #'bombExplodeTime' : jsondata['bombExplodeTime'],
    # 'badTeam' : jsondata['badTeam'],
    # 'defuser' : jsondata['defuser'],
    # 'goodTeam' : jsondata['goodTeam'],
    # 'round' : jsondata['round'],
    # 'gameID' : jsondata['gameID'],
    # 'roundStatus' : jsondata['roundStatus'],
    #'round1' : rounds[1]
    }
    # print jsondata
    return render(request, 'diffuse/history.html', context)
