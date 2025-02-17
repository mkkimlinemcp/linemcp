from django.shortcuts import render, redirect, get_object_or_404
from .models import create_Artist_profile, album_genres, album_Category, test, rightholder_cr, Album, Track,Accounting_base
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
from django.conf import settings
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
    paginator = Paginator(artists.values('Artist_name', 'Artist_ID', 'Artist_image', 'category').order_by('id'),page_size)

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
    paginator = Paginator(rightholder.values('user_name','user_code','email','user_level').order_by('id'), page_size)

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
            right_data = data.get("rights")

            album_Categ = album_data.get("album_Categ", "")
            opendate = album_data.get("opendate", "")
            track_no = album_data.get("track_no", "")
            user_c = right_data.get("rightholder")
            user_ac = right_data.get("User_Fees")

            # 앨범 코드 작성
            last_album = Album.objects.last()
            num = last_album.id if last_album else 0  # None 방지

            if num is None:
                num = 0
            else:
                num -= 1

            # Album 객체 목록 가져오기
            album_list = list(Album.objects.values())

            if num < 0 or num >= len(album_list):  # 인덱스 유효성 체크
                code = "0001"
            else:
                code = album_list[num].get('album_code', "0001")

            # 코드 변환 로직
            if str(code) == "0" or not code:
                code = "0001"
            elif len(code) >= 7:
                code = code[7:]
                code = str(int(code) + 1).zfill(4)

            # 앨범 카테고리 변환
            album_Categ = album_Categ or "기타"
            tag_dict = {
                "정규": "03",
                "싱글": "01",
                "EP": "02"
            }
            tag = tag_dict.get(album_Categ, "04")

            # 개봉일 처리
            if opendate and len(opendate) >= 4:
                ddd = opendate[2:4]
            else:
                ddd = "00"

            # 최종 코드 조합
            ALBC = f"LA{ddd}{tag}-{code}"
            print(ALBC)  # 생성된 앨범 코드 출력

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

            # 트랙 코드 생성
            last_track = Track.objects.last()
            tnum = last_track.id if last_track else 0  # None 방지

            if tnum is None:
                tnum = 0
            else:
                tnum -= 1

            # Track 객체 목록 가져오기
            track_list = list(Track.objects.values())

            if tnum < 0 or tnum >= len(track_list):  # 인덱스 유효성 체크
                tcode = "0001"
            else:
                tcode = track_list[tnum].get('Track_code', "0001")

            # 코드 변환 로직
            if str(tcode) == "0" or not tcode:
                tcode = "0001"
            elif len(tcode) >= 8:
                tcode = tcode[8:]
                tcode = str(int(tcode) + 1).zfill(4)

            # 트랙 코드 기본 문자열 생성
            ttt = str(len(track_no))  # 정수를 문자열로 변환
            Track_code_bd = f"L{ddd}{tag}{ttt}-"

            # 트랙 코드 리스트 생성
            Track_code_list = []

            for j in range(len(track_no)):
                Track_code_list.append(Track_code_bd + tcode)
                tcode = str(int(tcode) + 1).zfill(4)  # 간단하게 변환

            alb_id = Album.objects.filter(album_code=ALBC).values_list('id', flat=True).first()

            # 트랙 저장
            for idx, track in enumerate(track_data):
                Track.objects.create(
                    album_id=alb_id,
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

            #정산정보 저장
                user_ac = float(user_ac) * 0.01
                com_ac = 1 - float(user_ac)

                user = rightholder_cr.objects.get(user_code=user_c)
                albums_list = user.albums
                if ALBC not in albums_list:
                    albums_list.append(ALBC)
                    user.albums = albums_list  # JSONField 업데이트
                    user.save()  # 변경사항 저장
                    return JsonResponse({
                        "message": "앨범이 성공적으로 저장되었습니다.",
                        "album_code": ALBC  # ✅ album_code를 응답 데이터에 포함
                    }, status=200)
                else:
                    return JsonResponse({"message": "이미 존재하는 앨범입니다.", "albums": user.albums}, status=400)
            
            Accounting_base.objects.create(
                Album_code = ALBC,
                rightholder_code = user_c,
                User_Fees = user_ac,
                company_fees = com_ac,
            )

            return JsonResponse({"message": "앨범과 트랙이 성공적으로 저장되었습니다!"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request method"}, status=400)

#아티스트 페이지 내용
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

#아티스트 저장 폼
def create_artist(request):

    num = create_Artist_profile.objects.last().id
    num = num - 1
    list = create_Artist_profile.objects.values()
    Artist_idf = list[num]['Artist_ID']
    Artist_idf = int(Artist_idf) + 1

    if request.method == 'POST':
        form = Artist_create_form(request.POST, request.FILES)
        if form.is_valid():
            create = form.save(commit=False)
            create.create_date = timezone.now()
            create.Artist_ID = Artist_idf

            if "Artist_image" in request.FILES:
                new_image = request.FILES["Artist_image"]
                new_image_name = f"{Artist_idf}.jpg"  # 파일명을 Artist_ID로 설정

                # Django의 ImageField 경로를 유지하기 위해 'Artist_images/' 생략
                create.Artist_image.save(new_image_name, new_image)

            create.save()
            return redirect('maincms:Artists')
    else:
        form = Artist_create_form()
    context = {'form' : form}
    return render(request, 'maincms/Artist_create.html', context)

#아티스트 디테일
def artist_detail(request, artist_id):
    """
    아티스트 디테일 내용 출력
    """
    artist = create_Artist_profile.objects.get(id=artist_id)
    context = {'artist_d' : artist}
    return render(request, 'maincms/artist_detail.html', context)

def artist_update(request, artist_id):
    """
    아티스트 정보 수정 (이전 이미지 삭제 후 새로운 이미지 저장)
    """
    artist = get_object_or_404(create_Artist_profile, id=artist_id)

    if request.method == "POST":
        artist.Artist_name = request.POST.get("Artist_name")
        artist.Artist_name_en = request.POST.get("Artist_name_en")
        artist.sex = request.POST.get("sex")
        artist.category = request.POST.get("category")
        artist.Apple_url = request.POST.get("Apple_url")
        artist.Spotify_ID = request.POST.get("Spotify_ID")
        artist.Melon_ID = request.POST.get("Melon_ID")
        artist.genie_url = request.POST.get("genie_url")
        artist.bugs_url = request.POST.get("bugs_url")
        artist.flo_url = request.POST.get("flo_url")
        artist.vibe_url = request.POST.get("vibe_url")
        artist.Youtube_ID = request.POST.get("Youtube_ID")
        artist.Artist_ID = request.POST.get("Artist_ID")

        # 새로운 이미지 업로드 시 처리
        if "Artist_image" in request.FILES:
            new_image = request.FILES["Artist_image"]
            new_image_name = f"{artist.Artist_ID}.jpg"

            # 기존 이미지 삭제
            if artist.Artist_image:
                old_image_path = str(artist.Artist_image)  # 저장된 경로 (Artist_images/파일명)
                if default_storage.exists(old_image_path):
                    default_storage.delete(old_image_path)

            # 새 이미지 저장 (upload_to='Artist_images'가 적용됨)
            artist.Artist_image.save(new_image_name, new_image)

        artist.save()
        return redirect("artist_detail", artist_id=artist.id)  # 수정 후 다시 상세 페이지로 이동

    return render(request, "maincms/artist_detail.html", {"artist_d": artist})

def artist_delete(request, artist_id):
    """
    아티스트 삭제 (이미지도 함께 삭제)
    """
    artist = get_object_or_404(create_Artist_profile, id=artist_id)

    if request.method == "POST":
        # 이미지 파일 삭제 (artist_images/ 폴더 내 파일 관리)
        if artist.Artist_image:
            image_path = str(artist.Artist_image)  # 저장된 경로 (Artist_images/파일명)
            if default_storage.exists(image_path):
                default_storage.delete(image_path)

        # 데이터 삭제
        artist.delete()
        return redirect("Artists")  # 삭제 후 리스트 페이지로 이동

    return render(request, "maincms/artist_detail.html", {"artist_d": artist})



#모달 출력 실패
#class ArtistCreateView(BSModalFormView):
    #template_name = 'maincms/Artist_create.html'
    #form_class = Artist_create_form
