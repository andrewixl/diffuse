from django.shortcuts import render, redirect, HttpResponse
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
        print "Entered Into History"
        try:
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
        except IndexError:
            return HttpResponse("No Availible Data")

    try:
        round1win = rounds[0]
    except IndexError:
        round1win = 0
    try:
        round2win = rounds[1]
    except IndexError:
        round2win = 0
    try:
        round3win = rounds[2]
    except IndexError:
        round3win = 0
    try:
        round4win = rounds[3]
    except IndexError:
        round4win = 0




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
    'round1' : round1win,
    'round2' : round2win,
    'round3' : round3win,
    'round4' : round4win,
    'players': playersname
    }
    print playersname
    # print jsondata
    return render(request, 'diffuse/history.html', context)
