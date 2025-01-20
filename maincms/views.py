from django.shortcuts import render, redirect
from .models import create_Artist_profile, album_genres, album_Category, test, rightholder_cr
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .forms import Artist_create_form, test_form,rightholder_cr_form
import json

# Create your views here.




def maincms_in(request):
    return render(request, 'maincms/index.html')

def increment_value(value):
    # 문자열에서 숫자와 문자 분리
    prefix = ''.join(filter(str.isalpha, value))  # 문자 부분 (A)
    number = ''.join(filter(str.isdigit, value))  # 숫자 부분 (10000001)

    # 숫자를 증가시키기
    incremented_number = int(number) + 1

    # 숫자를 다시 0으로 패딩하여 결합
    return f"{prefix}{incremented_number:08d}"

def rightholder_cr_view(request):
    num = rightholder_cr.objects.last().id
    num = num - 1
    list = rightholder_cr.objects.values()
    vv = list[num]['user_code']
    new_value = increment_value(vv)

    if request.method == 'POST':
        form = rightholder_cr_form(request.POST)
        if form.is_valid():
            create = form.save(commit=False)
            create.user_code = new_value
            create.save()
            return redirect('maincms:rightholder_cr')
    else:   
        form = rightholder_cr_form()
    context = {'form' : form}
    return render(request, 'maincms/rightholder_cr.html' ,context)

def rightholder_list_view(request):

    """
    목록 출력 + 검색 필드 선택 기능
    """
    query = request.GET.get('q', '')  # 검색어
    field = request.GET.get('field', 'user_name')  # 검색 필드 (기본값: user_name)

    # 유효한 필드인지 확인
    valid_fields = ['user_name', 'email']
    if field not in valid_fields:
        field = 'user_name'

    if query:
        # 검색 필드와 검색어로 필터링
        filter_kwargs = {f"{field}__icontains": query}
        rightholder_list = rightholder_cr.objects.filter(**filter_kwargs).order_by('-create_date')
    else:
        rightholder_list = rightholder_cr.objects.order_by('-create_date')

    context = { 'rightholder_list' : rightholder_list, 'query': query, 'field': field, 'valid_fields': valid_fields }
    return render(request, 'maincms/rightholder_list.html' ,context)

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
    목록 출력 + 검색 필드 선택 기능
    """
    query = request.GET.get('q', '')  # 검색어
    field = request.GET.get('field', 'Artist_name')  # 검색 필드 (기본값: Artist_name)

    # 유효한 필드인지 확인
    valid_fields = ['Artist_name', 'Artist_ID']
    if field not in valid_fields:
        field = 'Artist_name'

    if query:
        # 검색 필드와 검색어로 필터링
        filter_kwargs = {f"{field}__icontains": query}
        Artist_list = create_Artist_profile.objects.filter(**filter_kwargs).order_by('-create_date')
    else:
        Artist_list = create_Artist_profile.objects.order_by('-create_date')

    context = {'Artist_list': Artist_list, 'query': query, 'field': field, 'valid_fields': valid_fields}
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
