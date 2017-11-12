from django.shortcuts import render, redirect, HttpResponse
import urllib2
import json
from .models import Player
# from urllib import request

def index(request):
   return render(request, 'diffuse/index.html')

def view(request):
	return render(request, 'diffuse/view.html')

def home(request, game_id):
	return render(request, 'diffuse/home.html')

def diffuse(request, game_id):
	return render(request, 'diffuse/diffuse.html')

def privacy(request):
	return render(request, 'diffuse/privacy.html')

def gotogame(request):
    game_id = request.POST.get('gameid')
    return redirect('/'+ game_id + '/history')

def history(request, game_id):
    try:
        response = urllib2.urlopen('http://ec2-34-211-226-74.us-west-2.compute.amazonaws.com/api/ActiveGame')
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
            response = urllib2.urlopen('http://ec2-34-211-226-74.us-west-2.compute.amazonaws.com/api/History')
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
        for x in playersarray:
            name = Player.objects.get(player_name = x['discordUsername'])
            name.player_points = x['score']
            name.save()
    except Player.DoesNotExist:
        for x in playersarray:
            user = Player.objects.createPlayer(x['discordUsername'], x['score'])


    try:
        round1 = rounds[0]
        round1triesnums = round1['tryStatus']
        round1tries = round1['tryNum']
        if round1tries > 3:
            round1win = 'Bad Won'
        else:
            round1win = 'Good Won'
        for x in range(0, len(round1triesnums)):
            if round1triesnums[x] == 1:
                round1triesnums[x] = 'Bomb Defused'
            elif round1triesnums[x] == 2:
                round1triesnums[x] = 'Bomb Exploded'
            elif round1triesnums[x] == 0:
                round1win = 'Round Has Not Started'
                round1triesnums[x] = 'Round Has Not Started'
    except IndexError:
        round1win = 'Round Has Not Started'
        round1triesnums = ['Round Has Not Started','Round Has Not Started','Round Has Not Started']

    try:
        round2 = rounds[1]
        round2triesnums = round2['tryStatus']
        round2tries = round2['tryNum']
        if round2tries > 3:
            round2win = 'Bad Won'
        else:
            round2win = 'Good Won'
        for x in range(0, len(round2triesnums)):
            if round2triesnums[x] == 1:
                round2triesnums[x] = 'Bomb Defused'
            elif round2triesnums[x] == 2:
                round2triesnums[x] = 'Bomb Exploded'
            elif round2triesnums[x] == 0:
                round2win = 'Round Has Not Started'
                round2triesnums[x] = 'Round Has Not Started'
    except IndexError:
        round2win = 'Round Has Not Started'
        round2triesnums = ['Round Has Not Started','Round Has Not Started','Round Has Not Started']

    try:
        round3 = rounds[2]
        round3triesnums = round3['tryStatus']
        round3tries = round3['tryNum']
        if round3tries > 3:
            round3win = 'Bad Won'
        else:
            round3win = 'Good Won'
        for x in range(0, len(round3triesnums)):
            if round3triesnums[x] == 1:
                round3triesnums[x] = 'Bomb Defused'
            elif round3triesnums[x] == 2:
                round3triesnums[x] = 'Bomb Exploded'
            elif round3triesnums[x] == 0:
                round3win = 'Round Has Not Started'
                round3triesnums[x] = 'Round Has Not Started'
    except IndexError:
        round3win = 'Round Has Not Started'
        round3triesnums = ['Round Has Not Started','Round Has Not Started','Round Has Not Started']

    try:
        round4 = rounds[3]
        round4triesnums = round4['tryStatus']
        round4tries = round4['tryNum']
        if round4tries > 3:
            round4win = 'Bad Won'
        else:
            round4win = 'Good Won'
        for x in range(0, len(round4triesnums)):
            if round4triesnums[x] == 1:
                round4triesnums[x] = 'Bomb Defused'
            elif round4triesnums[x] == 2:
                round4triesnums[x] = 'Bomb Exploded'
            elif round4triesnums[x] == 0:
                round4win = 'Round Has Not Started'
                round4triesnums[x] = 'Round Has Not Started'
    except IndexError:
        round4win = 'Round Has Not Started'
        round4triesnums = ['Round Has Not Started','Round Has Not Started','Round Has Not Started']

    players = Player.objects.all().order_by('-player_points')
    context = {
    'round1' : round1win,
    'round1tries' : round1triesnums,

    'round2' : round2win,
    'round2tries' : round2triesnums,

    'round3' : round3win,
    'round3tries' : round3triesnums,

    'round4' : round4win,
    'round4tries' : round4triesnums,

    'players':players,
    # 'players': playersname
    }
    # print jsondata
    return render(request, 'diffuse/history.html', context)
