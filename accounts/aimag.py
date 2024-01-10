from django.shortcuts import render
from django.template import RequestContext
from mynewproject.settings import *
from django.shortcuts import redirect, render

def aimagSumJagsaalt(request):

    ctx = {}
    ctx, renderURL = initwMenu(request)

    if(renderURL != "/"):
        return redirect(renderURL)

    RequestContext["action"] = lookupDataAction["aimagsum"]
    r = requests.post(srvURL["lookup"],
                      data=json.dumps(requestJSON),
                      headers=requestHeader["JSON"],
                      )
    resultAimagSum = r.json()['data']
    
    context = {}
    ai = {}
    for negjAimag in resultAimagSum:
        negjAimagNer = negjAimag['aimagname']
        ai[negjAimagNer] = []
        for negjSum in negjAimag["sumduud"]:
            ai[negjAimagNer].append(negjSum["sumname"])
            
    context['data'] = ai    
    return render(request, "aimagSumJagsaalt.html", context)
#   aimagSumJagsaalt