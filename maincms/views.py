from django.shortcuts import render, redirect
from .models import create_Artist_profile, album_genres, album_Category, test, rightholder_cr, Album, Track
from django.http import HttpResponse
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from .forms import Artist_create_form, test_form,rightholder_cr_form,Create_album_form
from django.db.models import Q 
from django.core.paginator import Paginator
import json
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os

# Create your views here.

def get_artist_profiles(request):
    # 페이지 번호와 페이지 크기 받아오기
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    search_query = request.GET.get('search', '').strip().lower()  # 검색어 가져오기

    # 아티스트 데이터 필터링
    artists = create_Artist_profile.objects.all()

    if search_query:
        artists = artists.filter(
            Q(Artist_name__icontains=search_query) |  # 이름에 검색어 포함
            Q(Artist_name_en__icontains=search_query)  # 영어 이름에 검색어 포함
        )

    # 페이징 처리
    paginator = Paginator(artists.values('Artist_name','Artist_ID','Artist_image','category'), page_size)

    try:
        artists_page = paginator.page(page)
    except Exception as e:
        return JsonResponse({'error': 'Invalid page'}, status=400)

    # 데이터와 페이지 정보를 반환
    return JsonResponse({
        'artists': list(artists_page.object_list),
        'has_next': artists_page.has_next(),
        'has_previous': artists_page.has_previous(),
        'current_page': artists_page.number,
        'total_pages': paginator.num_pages,
    })

def get_rightholder_profiles(request):
    # 페이지 번호와 페이지 크기 받아오기
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)
    search_query = request.GET.get('search', '').strip().lower()  # 검색어 가져오기

    # 권리자 데이터 필터링
    rightholder = rightholder_cr.objects.all()

    if search_query:
        rightholder = rightholder.filter(
            Q(user_name__icontains=search_query) |  # 이름에 검색어 포함
            Q(email__icontains=search_query)  # 이메일에 검색어 포함
        )

    # 페이징 처리
    paginator = Paginator(rightholder.values('user_name','user_code','email','user_level'), page_size)

    try:
        rightholder_page = paginator.page(page)
    except Exception as e:
        return JsonResponse({'error': 'Invalid page'}, status=400)

    # 데이터와 페이지 정보를 반환
    return JsonResponse({
        'rightholders': list(rightholder_page.object_list),
        'has_next': rightholder_page.has_next(),
        'has_previous': rightholder_page.has_previous(),
        'current_page': rightholder_page.number,
        'total_pages': paginator.num_pages,
    })

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

# 앨범 등록 기능 개발 중
@csrf_exempt
def create_album(request):
        
    return render(request, 'maincms/album_create.html')


@csrf_exempt
def save_album(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # JSON 데이터 파싱
            album_data = data.get("album")
            track_data = data.get("tracks", [])

            album_Categ = album_data.get("album_Categ", "")
            opendate = album_data.get("opendate", "")
            track_no = album_data.get("track_no", "")

            #앨범코드 작성
            num = Album.objects.last().id
            num = num - 1
            list = Album.objects.values()
            code = list[num]['album_code']

            if code == 0:
                code = "0001"
            else:
                code = code[7:]
                code = int(code) + 1
                code = str(code)
                code = "{0:0>4}".format(code)

            if album_Categ == "정규":
                tag = "03"
            elif album_Categ == "싱글":
                tag = "01"
            elif album_Categ == "EP":
                tag = "02"
            else:
                tag = "04"
            ddd = opendate[2:4]
            ALBC = "LA" + ddd + tag + "-" + code

            # 앨범 저장
            album = Album.objects.create(
                album_code=ALBC,  # 자동 코드 생성
                album_title=album_data["album_title"],
                album_title_en=album_data["album_title_en"],
                album_artist=album_data["album_artist"],
                album_genre=album_data["album_genre"],
                album_Categ=album_data["album_Categ"],
                album_country=album_data["album_country"],
                startdate=album_data["startdate"],
                opendate=album_data["opendate"],
                service_time=album_data["service_time"],
                album_copyright=album_data["album_copyright"],
                album_publish=album_data["album_publish"],
                service_area=album_data["service_area"],
                excluded=album_data["excluded"],
                service_lang=album_data["service_lang"],
                UPC_code=album_data["UPC_code"],
                UCI_code=album_data["UCI_code"],
                YT_service=album_data["YT_service"],
                status=album_data["status"],
            )

            #트랙코드 생성
            tnum = Track.objects.last().id
            tnum = tnum - 1
            tlist = Track.objects.values()
            tcode = tlist[num]['Track_code']
            if tcode == 0:
                tcode = "0001"
            else:
                tcode = tcode[8:]
                tcode = int(tcode) + 1
                tcode = str(tcode)
                tcode = "{0:0>4}".format(tcode)

            ttt = len(track_no)
            Track_code_bd = "L" + ddd + tag + ttt +"-"
            Track_code_list = []

            for j in range(len(track_no)):
                Track_code_list.append(Track_code_bd + tcode)
                tcode = int(tcode) + 1
                tcode = str(tcode)
                tcode = "{0:0>4}".format(tcode)

            # 트랙 저장
            for idx, track in enumerate(track_data):
                Track.objects.create(
                    album=album,
                    disk_no=int(track["disk_no"]),
                    track_no=int(track["track_no"]),
                    track_code=Track_code_list[idx],  # ✅ 각 트랙에 개별적인 코드 할당
                    song_title=track["song_title"],
                    song_artist=track["song_artist"],
                    track_genre=track["track_genre"],
                    track_lang=track["track_lang"],
                    title_song=track["title_song"],
                    adult=track["adult"],
                    tr_opendate=track["tr_opendate"],
                    track_length=track["track_length"],
                    lyricist=track["lyricist"],
                    composer=track["composer"],
                    arranger=track["arranger"],
                    with_artist=track["with_artist"],
                    featured=track["featured"],
                    ISRC=track["ISRC"],
                )

            return JsonResponse({"message": "앨범과 트랙이 성공적으로 저장되었습니다!"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)


#아티스트 리스트
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


#아티스트 저장 폼 임
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

            # 이미지 파일이 있는 경우 파일명 변경 처리
            if 'Artist_image' in request.FILES:
                uploaded_image = request.FILES['Artist_image']
                new_filename = f"{Aritist_idf}.jpg"

                # 기존 저장 경로를 유지하면서 파일명 변경
                uploaded_image.name = new_filename  # 파일명만 변경

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
