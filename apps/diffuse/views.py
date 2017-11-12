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
        round1 = rounds[0]
    except IndexError:
        round1 = 0
    try:
        round2 = rounds[1]
    except IndexError:
        round2 = 0
    try:
        round3 = rounds[2]
    except IndexError:
        round3 = 0
    try:
        round4 = rounds[3]
    except IndexError:
        round4 = 0
    try:
        round5 = rounds[4]
    except IndexError:
        round5 = 0




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
    'round1' : round1,
    'round2' : round2,
    'round3' : round3,
    'round4' : round4,
    'round5' : round5,
    'players': playersname
    }
    print playersname
    # print jsondata
    return render(request, 'diffuse/history.html', context)
