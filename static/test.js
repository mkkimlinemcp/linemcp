$(document).ready(function () {
    $("#generate").click(function () {
        const outerLoop = parseInt($("#disc_total_num").val());
        const innerLoop = parseInt($("#track_total_num").val());

        if (isNaN(outerLoop) || isNaN(innerLoop) || outerLoop <= 0 || innerLoop <= 0) {
            alert("두 숫자를 1 이상의 값으로 입력하세요.");
            return;
        }

        $("#result-table tbody").remove();
        let j = 1;
        const tbody = $("<tbody></tbody>").attr("id", `${outerLoop}_${j}`);

        let currentInnerLoop = innerLoop;
        for (let i = 1; i <= currentInnerLoop; i++) {
            // 여기에서 원하는 코드를 추가하세요 (ex: 데이터 처리, UI 생성 등)
            const row = $(`<tr>
                <th class='text-center' ><input class="form-ck" type="number" id="disk_no_${outerLoop}" name="disk_no[]" style="width: 31px;" value="${outerLoop}"></div></th>
                <th class='text-center' ><input class="form-ck" type="number" id="track_no_${i}" name="track_no[]" style="width: 31px;" value="${i}"></div></th>
                <th class='text-center' id="song_title_view_${outerLoop}_${i}"></th>
                <th class='text-center' id="artist_view_${outerLoop}_${i}"></th>
                <th class='text-center'><i class="bi bi-chevron-up icon" data-target="detail_${outerLoop}_${i}"></i></td>
            </tr>
            <tr id="detail_${outerLoop}_${i}">
                <th colspan='3'>
                    <div class="info-field">
                        <div class="info-field-column">
                            <div class="info-field">
                                <div class="label-field"><i class="bi bi-check check"></i>곡 제목</div><input class="form-tr song-title" type="text" name="song_title[]"  data-target="song_title_view_${outerLoop}_${i}">
                                <div class="label-field"><i class="bi bi-check check"></i>곡 아티스트</div><input class="form-tr song-artist" type="text" name="song_artist[]" data-target="artist_view_${outerLoop}_${i}">
                            </div>
                            <div class="info-field">
                                <div class="label-field"><i class="bi bi-check check"></i>트랙 장르</div>                
                                <select class="form-select-sm track_genre" name="track_genre[]" style="width: 203px;">
                                    <option selected>선택하세요</option>
                                    {% for g in genre_list %}
                                    <option value="{{ g.genres }}">{{ g.genres }}</td>
                                    {% endfor %}
                                </select>
                                <div class="label-field"><i class="bi bi-check check"></i>서비스 언어</div>
                                <select class="form-select-sm" name="track_lang[]" style="width: 203px;">
                                    <option selected>선택하세요</option>
                                    <option value="한국어">한국어</option>
                                    <option value="영어">영어</option>
                                    <option value="일본어">일본어</option>
                                </select>
                            </div>
                            <div class="info-field">
                                <div class="label-field"><i class="bi bi-check check"></i>오픈일</div><input class="form-tr datepicker" type="text" name="tr_opendate[]">
                                <div class="label-field"><i class="bi bi-check check"></i>ISRC</div><input class="form-tr" type="text" name="isrc[]">
                            </div>
                            <div class="info-field jf-item">
                                <div class="label-field lab-sm"><i class="bi bi-check"></i>대표곡</div><input class="form-check-input" type="checkbox" value="" name="title_song[]">
                                <div class="label-field lab-sm"><i class="bi bi-check"></i>성인</div><input class="form-check-input" type="checkbox" value="" name="adult[]">
                            </div>
                            <div class="info-field">
                                <div class="label-field lab-sm"><i class="bi bi-check check"></i>음원추가</div><input class="form-control form-control-sm" id="song_file[]" type="file"><input class="form-check-input" type="checkbox" value="" id="track_time" name="track_time[]">
                            </div>
                        </div>
                    </div>
                </th>
                <th>
                    <div class="info-field-column jf-item">
                        <div class="info-field"><div class="label-field"><i class="bi bi-check"></i>작사가</div><input class="form-control form-control-sm col" type="text" name="lyricist[]"></div>
                        <div class="info-field"><div class="label-field"><i class="bi bi-check check"></i>작곡가</div><input class="form-control form-control-sm col" type="text" name="composer[]"></div>
                        <div class="info-field"><div class="label-field"><i class="bi bi-check check"></i>편곡가</div><input class="form-control form-control-sm col" type="text" name="arranger[]"></div>
                        <div class="info-field"><div class="label-field"><i class="bi bi-check"></i>참여아티스트</div><input class="form-control form-control-sm col" type="text" name="with_artist[]"></div>
                        <div class="info-field"><div class="label-field"><i class="bi bi-check"></i>피쳐링아티스트</div><input class="form-control form-control-sm col" type="text" name="featured[]"></div>
                    </div>
                </th>
                <th class="text-center">
                    <div class="info-field-column">
                        <a class='btn btn-danger btn-sm'>트랙 삭제</a>
                    </div>
                </th>
            </tr>`);
            tbody.append(row);
        }

        // 결과 테이블에 추가
        $("#result-table").append(tbody);


    
    });
});