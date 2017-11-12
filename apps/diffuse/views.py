from django.shortcuts import render, redirect
import urllib2
import json
# from urllib import request

def index(request):
   return render(request, 'diffuse/index.html')

def view(request):
	return render(request, 'diffuse/view.html')

def home(request, game_id):
	return render(request, 'diffuse/home.html')

def diffuse(request, game_id):
	return render(request, 'diffuse/diffuse.html')

def gotogame(request):
    game_id = request.POST.get('gameid')
    return redirect('/'+ game_id + '/history')

def history(request, game_id):
    try:
        response = urllib2.urlopen('http://b5b1e790.ngrok.io/api/ActiveGame')
        data = json.load(response)

        jsondata = {}
        for key, value in data.items():
            jsondata[key] = value

        rounds = []
        rounds = jsondata['rounds']

        playersarray = []
        playersarray = jsondata['players']

        playersname = {}
        for x in playersarray:
            playersname[x['discordUsername']] = x['score']
    except ValueError:
        response = urllib2.urlopen('http://b5b1e790.ngrok.io/api/History')
        data = json.load(response)

        jsondata = {}
        for key, value in data.items():
            jsondata[key] = value

        rounds = []
        rounds = jsondata['rounds']

        playersarray = []
        playersarray = jsondata['players']

        playersname = {}
        for x in playersarray:
            playersname[x['discordUsername']] = x['score']




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
    'round1' : rounds[0],
    # 'round2' : rounds[1],
    # 'round3' : rounds[2],
    # 'round4' : rounds[3],
    # 'round5' : rounds[4],
    'players': playersname
    }
    print playersname
    # print jsondata
    return render(request, 'diffuse/history.html', context)
