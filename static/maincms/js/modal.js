$(document).ready(function () {
    const artistModal = $('#artistModal');
    const artistList = $('#artistList');
    const artistSearch = $('#artistSearch');
    const searchButton = $('#searchButton'); // 검색 버튼
  
    let currentPage = 1; // 현재 페이지 번호
    let pageSize = 10; // 페이지 크기
    let searchQuery = ''; // 검색어 저장
  
    // 모달 열기
    $('#album_artist').on('click', function () {
      artistModal.fadeIn();
      loadArtists(); // 데이터 로드
    });
  
    // 데이터 로드 함수
    function loadArtists() {
      const url = `api/artists/?page=${currentPage}&page_size=${pageSize}&search=${searchQuery}`;
      $.getJSON(url, function (data) {
        artistList.empty(); // 기존 목록 초기화
        if (data.error) {
          alert(data.error);
          return;
        }
        data.artists.forEach(artist => {
            const artistImage = artist.Artist_image ? artist.Artist_image : "Artist_images/user_image_none.png"; // 이미지가 없으면 기본 이미지 사용
            artistList.append(
              `<li class="list-group-item artist-item" data-id="${artist.Artist_ID}">
                <div><img src="http://localhost:8000/media/${artistImage}" style="width: 30px;" height="30px;"></div>
                <div>${artist.Artist_name}</div>
                <div>${artist.Artist_ID}</div>
                <div>${artist.category}</div>
              </li>`
            );
          });
          
  
          // 페이지네이션 업데이트
          updatePagination(data.current_page, data.total_pages);
        });
      }

      // 페이지네이션 버튼 업데이트 함수
      function updatePagination(currentPage, totalPages) {
        const pagination = $('#pagination');
        pagination.empty(); // 기존 버튼 초기화

        // 이전 버튼 추가
        pagination.append(
          `<li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
            <a class="page-link" href="#" aria-label="Previous" data-page="${currentPage - 1}">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>`
        );

        // 페이지 번호 버튼 추가
        for (let i = 1; i <= totalPages; i++) {
          pagination.append(
            `<li class="page-item ${i === currentPage ? 'active' : ''}">
              <a class="page-link" href="#" data-page="${i}">${i}</a>
            </li>`
          );
        }

        // 다음 버튼 추가
        pagination.append(
          `<li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
            <a class="page-link" href="#" aria-label="Next" data-page="${currentPage + 1}">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>`
        );

        // 페이지네이션 클릭 이벤트
        pagination.find('a').on('click', function (e) {
          e.preventDefault();
          const page = $(this).data('page');
          if (page && page !== currentPage) {
            currentPage = page;
            loadArtists(); // 새로운 페이지 로드
          }
        });
      }

      // 검색 버튼 클릭 이벤트
      searchButton.on('click', function () {
        searchQuery = artistSearch.val().trim().toLowerCase(); // 검색어 가져오기
        currentPage = 1; // 검색 시 첫 페이지로 이동
        loadArtists(); // 데이터 다시 로드
      });
    // 모달 닫기
    $('#closeModal').on('click', function () {
      artistModal.fadeOut();
    });
  
    // 모달 외부 클릭 시 닫기
    $(window).on('click', function (e) {
      if ($(e.target).is(artistModal)) {
        artistModal.fadeOut();
      }
    });
  
    // 아티스트 선택
    artistList.on('click', '.artist-item', function () {
        const artistName = $(this).find('div:nth-child(2)').text().trim(); // 두 번째 <div>에서 텍스트 추출
        const artistID = $(this).data('id'); // data-id에서 ID 추출
        $('#album_artist').val(`${artistName}`); // input에 아티스트 이름 설정
        artistModal.fadeOut();
     });
  });
  