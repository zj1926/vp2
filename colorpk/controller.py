from django.http import JsonResponse
import json
import colorpk.cache_storage as cache
from colorpk.models.db import User, UserLike
from colorpk.models.auth import getUrl
import uuid
from datetime import timezone, datetime

def toggleLike(request, id):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    cache.like(id)
    return JsonResponse({
        "color": id
    })

def createColor(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)
    return JsonResponse({
        "error": False
    })

def getUser(request):
    userInfo = request.session.get('user', None)
    if userInfo:
        updateLastLogin(userInfo)

    return JsonResponse({
        "user": request.session.get('user', None)
    })

def generateUrl(request):
    # request.session.flush()  ## not sync db cleanup
    state = str(uuid.uuid4())
    request.session['state'] = state
    request.session['user'] = None
    return JsonResponse({
        "wb": getUrl('wb', state),
        "fb": getUrl('fb', state),
        "gg": getUrl('gg', state),
        "gh": getUrl('gh', state),
    })

## ========
## Private Function Def
## ========

def updateLastLogin(info):
    User.objects.filter(oauth=info['oauth'], oauthid=info['id']).update(lastlogin = datetime.now(timezone.utc))