from django.shortcuts import render,redirect
from .models import Board,Reply
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    pg = request.GET.get("page",1)
    s = Board.objects.all()
    pag = Paginator(s,10)

    #paginoator(A,B) A레코드들, B단위
    #Board의 레코드들을 10개씩 끊어서 페이징을 해주는 친구 pag생성 
    obj = pag.get_page(pg)

    context = {
        "sset":obj
    }
    return render(request, "board/index.html", context)


def detail(request, spk):
    s = Board.objects.get(id = spk)
    r = s.reply_set.all()
    context = {
        "s":s,
        "rset":r
    }
    return render(request, "board/detail.html",context)

def create(request):
    if request.method == "POST":
        ps = request.POST.get("psubject")
        pc = request.POST.get("pcon")
        pw = request.POST.get("pwriter")
        Board(subject= ps, content = pc, writer = pw).save()
        return redirect("index")
    return render( request, "board/create.html")

def update(request, spk):
    s = Board.objects.get(id = spk)
    if request.method == "POST":
        ps = request.POST.get("psubject")
        pc = request.POST.get("pcon")
        pw = request.POST.get("pwriter")
        s.subject,s.content,s.writer = ps,pc,pw
        s.save()
        return redirect("detail", spk)
    context = {
        "s": s
    }
    return render(request,"board/update.html",context)

def delete (request, spk):
    s = Board.objects.get(id = spk)
    s.delete()
    return redirect("index")

def creply(request, spk):
    b = Board.objects.get(id = spk)
    r = request.POST.get("rep")
    c = request.POST.get("com")
    Reply(board = b, replyer=r, comment= c)
    return redirect("detail",spk)

def dreply(request, spk, bpk):
    r = Reply.objects.get(id = spk)
    r.delete()
    return redirect("detail", bpk)

