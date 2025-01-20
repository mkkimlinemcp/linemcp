$("#album_add").click(function() {
    const formData = new FormData();
    formData.append('album_title',$("input[name='album_title']").val());
    formData.append('album_title_en',$("input[name='album_title_en']").val());
    formData.append('album_artist',$("input[name='album_artist']").val());
    formData.append('album_genre',$("input[name='album_genre']").val());
    formData.append('album_Categ',$("input[name='album_Categ']").val());
    formData.append('album_country',$("input[name='album_country']").val());
    formData.append('startdate',$("input[name='startdate']").val());
    formData.append('opendate',$("input[name='opendate']").val());
    formData.append('service_time',$("input[name='service_time']").val());
    formData.append('album_copyright',$("input[name='album_copyright']").val());
    formData.append('album_publish',$("input[name='album_publish']").val());
    formData.append('service_area',$("input[name='service_area']").val());
    formData.append('excluded',$("input[name='excluded']").val());
    formData.append('service_lang',$("input[name='service_lang']").val());
    formData.append('UPC',$("input[name='UPC']").val());
    formData.append('UCI',$("input[name='UCI']").val());
    formData.append('YT_service',$("input[name='YT_service']").val());
    formData.append('status','등록');

    document.querySelectorAll('input[name="disk_no[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="track_no[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });

    document.querySelectorAll('input[name="song_title[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="song_artist[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="track_genre[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="track_lang[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="adult[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="tr_opendate[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="lyricist[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="composer[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="arranger[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="with_artist[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="featured[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });
    document.querySelectorAll('input[name="isrc[]"]').forEach(function(input) {
        formData.append('track_name[]', input.value);
    });

        // FormData의 내용을 출력하기
    for (let pair of formData.entries()) {
        console.log(pair[0] + ': ' + pair[5]);
    }

    $.ajax({
        url: 'http://localhost:8000/maincms/album_create.html',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        success: function (response) {
            console.log('Album and tracks saved successfully:', response);
        },
        error: function (error) {
            console.error('Error:', error);
        }
    });

});