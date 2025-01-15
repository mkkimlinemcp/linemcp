from django.shortcuts import render, redirect
from .models import create_Artist_profile, album_genres, album_Category, test
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import Artist_create_form, test_form


# Create your views here.
def maincms_in(request):
    return render(request, 'maincms/index.html')

@csrf_exempt
def test_go(request):
    print(request.GET)
    print(request.method)
    print(request.path)
    test_list = request.GET
    print(test_list)

    #if request.method == 'POST':
        #form = test_form(request.POST)
        #if form.is_valid():
            #test_list = form.save(commit=False)
            #test_list.save()
            #return redirect('maincms:test_test')
    #else:
        #form = test_form()
    #context = {'form' : form}
    print("ready")

    return render(request, 'maincms/test.html')


def create_album(request):
    genre_list = album_genres.objects.all()
    Category_list = album_Category.objects.all()
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
