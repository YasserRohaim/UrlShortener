from django.shortcuts import render, redirect
import uuid
from .models import LinksMapper


def shorten (request):
    if request.method=="GET":
        return render(request, "home.html")
    if request.method=="POST":
        url= request.POST["long_url"]
        short_url=str(uuid.uuid4())[:10]
        new_link=LinksMapper(link=url,short=short_url)
        new_link.save()
        context={"short_url":short_url}
        return render(request, "home.html",context)
        
def go(request,short_url):
    link_object=LinksMapper.objects.get(short=short_url)
    long_url= link_object.link
    return redirect(long_url)
