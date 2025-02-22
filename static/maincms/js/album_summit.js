$(document).on("click", "#album_add", function (e) {
    e.preventDefault(); // 기본 폼 제출 방지

    
    let albumData = {
        album_title: $("input[name='album_title']").val(),
        album_title_en: $("input[name='album_title_en']").val(),
        album_artist: $("input[name='album_artist']").val(),
        album_genre: $("select[name='album_genre']").val(),
        album_Categ: $("select[name='album_Categ']").val(),
        album_country: $("select[name='album_country']").val(),
        startdate: $("input[name='startdate']").val(),
        opendate: $("input[name='opendate']").val(),
        service_time: $("select[name='service_time']").val(),
        album_copyright: $("input[name='album_copyright']").val(),
        album_publish: $("input[name='album_publish']").val(),
        service_area: $("select[name='service_area']").val(),
        excluded: $("input[name='excluded']").val(),
        service_lang: $("select[name='service_lang']").val(),
        UPC_code: $("input[name='UPC']").val(),
        UCI_code: $("input[name='UCI']").val(),
        YT_service: $("select[name='YT_service']").val(),
        main_artist_id: $("#album_artist_id_roll").val(),
        with_main_artist: $("#album_with_artist_roll").val(),
        feat_main_artist: $("#album_feat_artist_roll").val(),
        album_code: $("input[name='albumcode']").val(),
        status: "등록",
    };
    let artistData = {
        main_artist_id: $("#album_artist_id_roll").val(),
        with_main_artist_id: $("#album_with_artist_id_roll").val(),
        feat_main_artist_id: $("#album_feat_artist_id_roll").val(),
    }
    let rightData = {
        rightholder: $("input[name='rightholder_code']").val(),
        User_Fees : $("input[name='allocation_rate']").val(),
    };
        
    let trackData = [];
    // 각 디스크/트랙의 첫 번째 <tr>을 기준으로 순회
    $("#result-table tbody").find("tr:nth-child(odd)").each(function () { 
        let basicRow = $(this);  // 첫 번째 <tr> (disk_no, track_no 포함)
        let detailRow = basicRow.next();  // 두 번째 <tr> (나머지 정보 포함)

        let track = {
            disk_no: basicRow.find("input[name='disk_no[]']").val() || "",
            track_no: basicRow.find("input[name='track_no[]']").val() || "",
            song_title: detailRow.find("input[name='song_title[]']").val() || "",
            song_artist: detailRow.find("input[name='song_artist[]']").val() || "",
            track_code: detailRow.find("input[name='track_code[]']").val() || "",
            track_genre: detailRow.find("select[name='track_genre[]']").val() || "",
            track_lang: detailRow.find("select[name='track_lang[]']").val() || "",
            title_song: detailRow.find("input[name='title_song[]']").is(":checked") ? "Yes" : "No",
            adult: detailRow.find("input[name='adult[]']").is(":checked") ? "Yes" : "No",
            tr_opendate: detailRow.find("input[name='tr_opendate[]']").val() || "",
            track_length: detailRow.find("input[name='track_length[]']").val() || "",
            lyricist: detailRow.find("input[name='lyricist[]']").val() || "",
            composer: detailRow.find("input[name='composer[]']").val() || "",
            arranger: detailRow.find("input[name='arranger[]']").val() || "",
            with_artist: detailRow.find("input[name='with_artist[]']").val() || "",
            featured: detailRow.find("input[name='featured[]']").val() || "",
            ISRC: detailRow.find("input[name='isrc[]']").val() || "",
            UCI: detailRow.find("input[name='uci[]']").val() || "",
        };

        trackData.push(track);
    });

    $.ajax({
        type: "POST",
        url: "save_album/",  // Django URL
        data: JSON.stringify({ album: albumData, tracks: trackData, rights: rightData, artists: artistData}),
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCSRFToken() // CSRF 토큰 설정 (아래 함수 참고)
        },
        success: function (response) {
            alert("앨범과 트랙이 성공적으로 저장되었습니다!");
            $("input[name='album_code']").val(response.album_code);
        },
        error: function (error) {
            console.log(error);
            alert("저장 중 오류가 발생했습니다.");
        }
    });
});

// CSRF 토큰 가져오기
function getCSRFToken() {
    return document.cookie.match(/csrftoken=([^ ;]+)/)[1];
}
