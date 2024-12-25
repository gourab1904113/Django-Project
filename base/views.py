from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

posts= [

    {'id':1, 'name':'Tution1'},
    {'id':2, 'name': 'Tution2'},
    {'id':3, 'name': 'Tution3'},
]

rooms=[
      {'id':1, 'type':'Big'},
      {'id':2, 'type': "small"},
      {'id':3, 'type': "mid"},
]




def home(request):
    return render(request, 'base/Home.html',{'posts':posts})
def room(request):
    return render(request, 'base/Room.html',{'rooms':rooms})

def post(request):
    return render(request, 'base/Post.html')