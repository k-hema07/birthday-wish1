from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from . import content as c


def lock(request):
    if request.session.get('ok'):
        return redirect('wish')
    error = False
    if request.method == 'POST':
        if request.POST.get('password', '').strip() == c.PASSWORD:
            request.session['ok'] = True
            return redirect('wish')
        error = True
    return render(request, 'lock.html', {'c': c, 'error': error})


def wish(request):
    if not request.session.get('ok'):
        return redirect('lock')
    return render(request, 'wish.html', {'c': c})


def logout(request):
    request.session.flush()
    return redirect('lock')


def sw(request):
    path = settings.BASE_DIR / 'static' / 'sw.js'
    resp = HttpResponse(path.read_text(encoding='utf-8'), content_type='application/javascript')
    resp['Service-Worker-Allowed'] = '/'
    resp['Cache-Control'] = 'no-cache'
    return resp
