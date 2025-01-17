from django.shortcuts import render, redirect
from .models import create_Artist_profile, album_genres, album_Category, test
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import Artist_create_form, test_form
import json

# Create your views here.
def maincms_in(request):
    return render(request, 'maincms/index.html')

@csrf_exempt
def test_go(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data['test1'])
        print(type(data))
        form = test_form()
        try_test = form.save(commit=False)
        try_test.test1 = data['test1']
        try_test.test2 = data['test2']
        try_test.test3 = data['test3']
        try_test.test4 = data['test4']
        try_test.test5 = data['test5']
        try_test.test6 = data['test6']
        try_test.test7 = data['test7']
        try_test.save()
        
    return render(request, 'maincms/test.html')


def create_album(request):
    genre_list = album_genres.objects.all()
    Category_list = album_Category.objects.all()
    print(genre_list)
    print(type(genre_list))
    context = { 'genre_list' : genre_list, 'Category_list' : Category_list }
    return render(request, 'maincms/album_create.html', context)

def Artists(request):
    """
    목록출력
    """
    Artist_list = create_Artist_profile.objects.order_by('-create_date')
    context = { 'Artist_list' : Artist_list }
    return render(request, 'maincms/Artist_list.html', context)

def create_artist(request):

    num = create_Artist_profile.objects.last().id
    num = num - 1
    list = create_Artist_profile.objects.values()
    Aritist_idf = list[num]['Artist_ID']
    Aritist_idf = int(Aritist_idf) + 1

    if request.method == 'POST':
        form = Artist_create_form(request.POST, request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            create.create_date = timezone.now()
            create.Artist_ID = Aritist_idf
            create.save()
            return redirect('maincms:Artists')
    else:
        form = Artist_create_form()
    context = {'form' : form}
    return render(request, 'maincms/Artist_create.html', context)


#모달 출력 실패
#class ArtistCreateView(BSModalFormView):
    #template_name = 'maincms/Artist_create.html'
    #form_class = Artist_create_form
