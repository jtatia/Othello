import time
from django.http import Http404, HttpResponseRedirect, HttpResponse, JsonResponse
from .models import Game
from django.shortcuts import render
import threading
# Create your views here.


def index(request):
    val  = 'main/index.html'
    context = {}
    return render(request,val,context)

def about(request):
    val  = 'main/about.html'
    context = {}
    return render(request,val,context)


def joingame(request):
    try:
        game = Game.objects.get(token=request.POST['token'])
        if(game.count<=2):
            game.count=game.count+1
            game.player=2
            game.save()
            timer(game.token)
            return render(request, 'main/game.html', {'game': game})
        else:
            return render(request,'main/error.html',{})
    except game.DoesNotExist:
        return render(request, 'main/error.html', {})


def newgame(request):
    game = Game.objects.create()
    token = game.token
    game.count+=1
    game.save()
    return HttpResponseRedirect('/main/game/'+str(token))


def game(request,token):
    try:
        game = Game.objects.get(token=token)
        if game.count>=2:
            return render(request,'main/error.html',{})
        else:
            game.count = game.count+1
            game.save()
            return render(request, 'main/game.html', {'game': game})
    except Game.DoesNotExist:
        raise Http404("No Such Game exists")
    return render(request,'main/game.html',{'game': game})

def update_board(request):
    board=request.POST['gameboard']
    token=request.POST['token']
    turn=request.POST['turn']
    gameEnd=request.POST['gameEnd']
    game = Game.objects.get(token=token)
    game.gameboard = board
    game.gameEnd=gameEnd
    game.timer=21
    game.turn=turn
    game.save()
    return HttpResponse('success')

def refresh(request):
     token=request.GET['token']
     game=Game.objects.get(token=token)
     dict={'gameboard':game.gameboard,'turn':game.turn,'timer':game.timer,'gameEnd':game.gameEnd}
     return JsonResponse(dict)

def run(token):
    while True:
        game = Game.objects.get(token=token)
        if game.timer<=0:
            game.timer=20
            if game.turn==1:
                game.turn=2
            else:
                game.turn=1
        game.timer=game.timer-1
        time.sleep(1)
        game1 = Game.objects.get(token=token)
        if(game1.timer!=21):
            game.save()
        else:
            game1.timer=19
            game1.save()

def timer(token):
    t1 = threading.Thread(target=run,args=(token,))
    t1.start();
