$(document).ready(function () {
    $("#generate").click(function () {
        const outerLoop = parseInt($("#outer-loop").val());
        const innerLoop = parseInt($("#inner-loop").val());

        if (isNaN(outerLoop) || isNaN(innerLoop) || outerLoop <= 0 || innerLoop <= 0) {
            alert("두 숫자를 1 이상의 값으로 입력하세요.");
            return;
        }

        $("#result-table tbody").remove();

        for (let i = 1; i <= outerLoop; i++) {
            const tbody = $("<tbody></tbody>").attr("id", `tbody-${i}`);

            // 사용자 입력 받기 (2 이상일 때 무조건 물어보기)
            let currentInnerLoop = innerLoop;
            if (currentInnerLoop >= 2) {
                const userValue = prompt(`반복 ${i}일 때 사용할 두 번째 숫자를 입력하세요 (기존 값: ${currentInnerLoop}):`);
                if (!isNaN(userValue) && userValue > 0) {
                    currentInnerLoop = parseInt(userValue); // 입력된 값으로 갱신
                } else {
                    alert("유효한 숫자를 입력하지 않아 기본값을 사용합니다.");
                }
            }

            for (let j = 1; j <= currentInnerLoop; j++) {
                // 여기에서 원하는 코드를 추가하세요 (ex: 데이터 처리, UI 생성 등)
                const row = $(`<tr>
                    <th class='text-center' id="disk_no">
                        <input class="form-ck" type="number" name="album_title" style="width: 31px;">
                    </th>
                </tr>`);
                tbody.append(row);
            }

            // 결과 테이블에 추가
            $("#result-table").append(tbody);
        }
    });
});