from django.shortcuts import render
from gptliaotian.newinteract import liaotianya
from gptliaotian.newinteract import randompersonality
# Create your views here.
def testchuanshu(request):
    list = [{"name": 'good', 'password': 'python'}, {'name': 'learning', 'password': 'django'}]
    return render(request, 'warehouse/furniture.html',{'form':list})

def index(request):
    return render(request, 'jQueryBg/index.html',)

def sheji(request):
    return render(request, 'inputCss/index.html', )

def liaotian(request):
    personality = randompersonality()
    return render(request, 'chat/index.html',{'personality':personality})

def shejiliaotian(request):
    personality=[]
    personality.append(request.GET.get("personality1"))
    personality.append(request.GET.get("personality2"))
    personality.append(request.GET.get("personality3"))
    personality.append(request.GET.get("personality4"))
    personality.append(request.GET.get("personality5"))
    dialoglist = []
    return render(request, 'chat/index.html',{'personality':personality,'dialoglist':dialoglist})

def shengchengduihua(request):
    inputreply = request.GET.get("message-to-send")
    personality = request.GET.get("personality")
    personalitylist=eval(personality)
    history=request.GET.get("history")
    historylist = []
    dialoglist = []
    if len(history)>0:
        dialoglist=eval(history)
        for ij in dialoglist:
            historylist.append(ij["dialog1"])
            historylist.append(ij["dialog2"])

    response=liaotianya(personalitylist,historylist,inputreply)
    item={"time":"","dialog1":inputreply,"dialog2":response}
    dialoglist.append(item)
    #personality=''
    #liaotianya()
    return render(request, 'chat/index.html',{'personality':personalitylist,'dialoglist':dialoglist})
