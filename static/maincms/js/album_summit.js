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
        status: "등록",
    };

    let trackData = [];
    $("#result-table tbody").each(function () {
        let row = $(this);
        let track = {
            disk_no: row.find("input[name='disk_no[]']").val(),
            track_no: row.find("input[name='track_no[]']").val(),
            song_title: row.find("input[name='song_title[]']").val(),
            song_artist: row.find("input[name='song_artist[]']").val(),
            track_genre: row.find("select[name='track_genre[]']").val(),
            track_lang: row.find("select[name='track_lang[]']").val(),
            title_song: row.find("input[name='title_song[]']").is(":checked") ? "Yes" : "No",
            adult: row.find("input[name='adult[]']").is(":checked") ? "Yes" : "No",
            tr_opendate: row.find("input[name='tr_opendate[]']").val(),
            track_length: row.find("input[name='track_length[]']").val(),
            lyricist: row.find("input[name='lyricist[]']").val(),
            composer: row.find("input[name='composer[]']").val(),
            arranger: row.find("input[name='arranger[]']").val(),
            with_artist: row.find("input[name='with_artist[]']").val(),
            featured: row.find("input[name='featured[]']").val(),
            ISRC: row.find("input[name='isrc[]']").val(),
        };
        trackData.push(track);
    });

    $.ajax({
        type: "POST",
        url: "save_album/",  // Django URL
        data: JSON.stringify({ album: albumData, tracks: trackData }),
        contentType: "application/json",
        headers: {
            "X-CSRFToken": getCSRFToken() // CSRF 토큰 설정 (아래 함수 참고)
        },
        success: function (response) {
            alert("앨범과 트랙이 성공적으로 저장되었습니다!");
            location.reload(); // 페이지 새로고침
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
