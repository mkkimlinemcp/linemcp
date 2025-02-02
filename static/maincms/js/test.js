$(document).on("click", "#album_add", function () {
    let zip = new JSZip(); // ZIP 객체 초기화

    $(".song_file").each(function () {
        let fileInput = $(this)[0]; // 현재 input
        if (fileInput.files.length === 0) return; // 파일이 없으면 건너뜀

        let file = fileInput.files[0]; // 선택한 파일 객체
        let fileExtension = file.name.split('.').pop(); // 확장자 추출

        // 🔥 현재 파일이 있는 테이블 행에서 필요한 정보 가져오기
        let row = $(this).closest("tr");
        let songTitle = row.find(".song-title").val().trim() || "untitled"; // 곡 제목
        let artistName = row.find(".song-artist").val().trim() || "unknown"; // 아티스트 이름

        let newFileName = `${artistName} - ${songTitle}.${fileExtension}`; // 변경된 파일명

        // 파일을 zip에 추가하기 위해 FileReader 사용
        let fileReader = new FileReader();
        fileReader.readAsArrayBuffer(file);
        fileReader.onload = function () {
            zip.file(newFileName, fileReader.result); // 압축 파일에 추가

            // 모든 파일을 추가한 후 ZIP 생성 & 다운로드
            if (Object.keys(zip.files).length === $(".song_file").length) {
                zip.generateAsync({ type: "blob" }).then(function (blob) {
                    let url = URL.createObjectURL(blob);
                    let a = document.createElement("a");
                    a.href = url;
                    a.download = "compressed_files.zip"; // ZIP 파일명 지정
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                    URL.revokeObjectURL(url);
                });
            }
        };
    });
});
