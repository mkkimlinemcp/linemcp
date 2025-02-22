$(document).ready(function () {
    $("#generate").click(function () {
        const outerLoop = parseInt($("#disc_total_num").val());
        const innerLoop = parseInt($("#track_total_num").val());

        if (isNaN(outerLoop) || isNaN(innerLoop) || outerLoop <= 0 || innerLoop <= 0) {
            alert("두 숫자를 1 이상의 값으로 입력하세요.");
            return;
        }
        if (outerLoop == 1) {
            $("#result-table tbody").remove();
        }
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
                                <div class="label-field"><i class="bi bi-check check"></i>곡 아티스트</div><input class="form-tr song-artist" type="text" name="song_artist[]" data-modal="modal2" data-target="artist_view_${outerLoop}_${i}">
                            </div>
                            <div class="info-field">
                                <div class="label-field"><i class="bi bi-check check"></i>트랙 장르</div>                
                                <select class="form-select-sm track_genre" name="track_genre[]" style="width: 203px;">
                                    <option selected>선택하세요</option>
                                    <option value="POP">POP</option>
                                    <option value="Dance">Dance</option>
                                    <option value="Hiphop">Hiphop</option>
                                    <option value="Newage">Newage</option>
                                    <option value="Indie pop">Indie pop</option>
                                    <option value="Indie">Indie</option>
                                    <option value="Indie Rock">Indie Rock</option>
                                    <option value="Indie Folk">Indie Folk</option>
                                    <option value="Folk">Folk</option>
                                    <option value="World">World</option>
                                    <option value="OST">OST</option>
                                    <option value="Trot">Trot</option>
                                    <option value="Instrumental">Instrumental</option>
                                </select>
                                <div class="label-field"><i class="bi bi-check check"></i>서비스 언어</div>
                                <select class="form-select-sm service-lang" name="track_lang[]" style="width: 203px;">
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
                                <div class="label-field"><i class="bi bi-check check"></i>곡코드</div><input class="form-tr" type="text" name="track_code[]">
                            </div>
                            <div class="info-field">
                                <div class="label-field lab"><i class="bi bi-check check"></i>음원추가</div><input class="form-control form-control-sm song_file" id="song_file[]" type="file" style="width:250px;"><input class="form-tr track_length" type="text" name="track_length[]"style="width:80px;"><input class="form-control form-control-sm" id="lyric_file[]" type="file"style="width:230px;">
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
                        <div class="info-field"><div class="label-field"><i class="bi bi-check"></i>uci</div><input class="form-control form-control-sm col" type="text" name="uci[]"></div>
                    </div>
                </th>
                <th class="text-center">
                    <div class="info-field-column">
                        <a class='btn btn-danger btn-sm delete-btn'>트랙 삭제</a>
                    </div>
                </th>
            </tr>`);
            tbody.append(row);
        }

        // 결과 테이블에 추가
        $("#result-table").append(tbody);
        $("#generate").text("디스크 추가");
        addup = parseInt(outerLoop) + 1;
        $("#disc_total_num").val(addup);
        $(document).ready(function () {
            // 실시간 변경 시 상위 값 갱신 (동적 요소까지 포함)
            $(document).on("input", ".song-title", function () {
                const targetId = $(this).data("target");
                $("#" + targetId).text($(this).val());
            });
        
            $(document).on("input", ".song-artist", function () {
                const targetId = $(this).data("target");
                $("#" + targetId).text($(this).val());
            });
        });
    
    });
    //트랙삭제
    $(document).on("click", ".delete-btn", function() {
        $(this).closest("tr").prev("tr").addBack().remove();
    });
    //상세 숨기기 보이기
    $(document).on("click", ".icon", function() {
        let targetId = $(this).data("target"); // data-target 속성 값 가져오기
        let detailRow = $("#" + targetId); // 해당하는 <tr> 찾기
    
        detailRow.stop().slideToggle(300); // 부드럽게 슬라이드 업/다운 (300ms)
    
        // 아이콘 회전 애니메이션
        $(this).toggleClass("rotated");
    });
    // 오디오 파일 길이 계산
    $(document).on("change", ".song_file", function () {
        const fileInput = this;
        const file = fileInput.files[0];

        if (file) {
            const audio = new Audio();
            const objectURL = URL.createObjectURL(file);

            audio.src = objectURL;
            audio.addEventListener("loadedmetadata", () => {
                const duration = audio.duration;
                const formattedTime = formatTime(duration);

                $(fileInput).siblings(".track_length").val(formattedTime);
                URL.revokeObjectURL(objectURL);
            });
        }
    });

    function formatTime(seconds) {
        const hours = Math.floor(seconds / 3600);
        const minutes = Math.floor((seconds % 3600) / 60);
        const secs = Math.floor(seconds % 60);

        return `${hours.toString().padStart(2, "0")}:` +
               `${minutes.toString().padStart(2, "0")}:` +
               `${secs.toString().padStart(2, "0")}`;
    }
});
