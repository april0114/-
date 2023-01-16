from django.shortcuts import render, redirect
from .models import Shop
# Create your views here.
def delete(request, spk):
    s = Shop.objects.get(id=spk)
    s.delete()
    return redirect("index")

def detail(request, spk):
    s = Shop.objects.get(id=spk)
    context = {
        "s" : s
    }
    return render(request, "shop/detail.html", context)


def index(request):
    s = Shop.objects.all()
    context = {
        "sset" : s
    }
    return render(request, "shop/index.html", context)

def create (request):
    if request.method == "POST":
        pn = request.POST.get("pname")
        pp = request.POST.get("pprice")
        pc = request.POST.get("pcon")
        Shop(name = pn, price = pp, content=pc, lieky = 0)
        return redirect("index")
    return render (request, "shop/create.html")


def update(request, spk):
    s = Shop.objects.get(id = spk)
    if request.method == "POST":
        pn = request.POST.get("pname")
        pp = request.POST.get("pprice")
        pc = request.POST.get("pcon")
        s.name,s.price,s.content = pn,pp,pc
        s.save()
        return redirect("detail",spk)
        context = {
            "s":s
        }
    return render(request, "shop/update.html")



