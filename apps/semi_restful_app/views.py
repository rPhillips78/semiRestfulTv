from django.shortcuts import render, redirect
from .models import *

def index(request):
    all_shows = Show.objects.all()
    context = {
        'all_shows': all_shows
    }
    return render(request, 'semi_restful_app/index.html', context)

def process(request):
    Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release'], description=request.POST['desc'])
    last_show = Show.objects.last()
    return redirect('/shows/' + str(last_show.id))

def new_show(request):
    return render(request, 'semi_restful_app/process.html')


def show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'semi_restful_app/show.html', context)

def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'semi_restful_app/edit.html', context)

def process_edit(request, show_id):
    show_edit = Show.objects.get(id=show_id)
    show_edit.title = request.POST['title']
    show_edit.network = request.POST['network']
    show_edit.release_date = request.POST['release']
    show_edit.description = request.POST['desc']
    show_edit.save()
    return redirect('/shows/' + str(show_id))

def destroy(request, show_id):
    show_gone = Show.objects.get(id=show_id)
    show_gone.delete()
    return redirect('/shows')
