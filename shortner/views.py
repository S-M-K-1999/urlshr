from django.http.response import HttpResponse
from .models import urls
from django.shortcuts import render,redirect
import uuid
# Create your views here.
def index(request):
    return render(request,'index.html')
def create(request):
    if request.method == 'POST':
            link = request.POST['link']
            uid = str(uuid.uuid4())[:5]
            new_url = urls(link = link,uid= uid)
            new_url.save()
            return HttpResponse(uid)
def go(request, pk):
    url_details = urls.objects.get(uid=pk)
    return redirect(url_details.link)