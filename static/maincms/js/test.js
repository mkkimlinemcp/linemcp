// 각 모달을 초기화하는 공통 함수
function setupModal(modalId, modelEndpoint, options = {}) {
    const modal = $(`#${modalId}`);
    const searchInput = modal.find('input[type="text"]');
    const searchButton = modal.find('button');
    const list = modal.find('.artist-list');
    const pagination = modal.find('.pagination');
    let currentPage = 1;
    let searchQuery = '';
    let targetInput = null; // 클릭한 input 요소를 추적
  
    // 데이터 로드 함수
    function loadData() {
      const url = `api/${modelEndpoint}/?page=${currentPage}&search=${searchQuery}`;
      $.getJSON(url, function (data) {
        list.empty();
        if (data.error) {
          alert(data.error);
          return;
        }
  
        // 리스트 업데이트
        if (options.updateList) {
          options.updateList(data, list);
        } else {
          data.artists.forEach(artist => {
            const image = artist.image || "Artist_images/user_image_none.png";
            list.append(
              `<li class="list-group-item artist-item" data-id="${artist.Artist_ID}">
                <div><img src="http://localhost:8000/media/${image}" style="width: 30px;" height="30px;"></div>
                <div>${artist.Artist_name}</div>
                <div>${artist.Artist_ID}</div>
                <div>${artist.category}</div>
              </li>`
            );
          });
        }
  
        // 페이지네이션 업데이트
        updatePagination(data.current_page, data.total_pages);
      });
    }
  
    // 페이지네이션 생성
    function updatePagination(currentPage, totalPages) {
      pagination.empty();
      pagination.append(
        `<li class="page-item ${currentPage === 1 ? 'disabled' : ''}">
          <a class="page-link" href="#" data-page="${currentPage - 1}">&laquo;</a>
        </li>`
      );
  
      for (let i = 1; i <= totalPages; i++) {
        pagination.append(
          `<li class="page-item ${i === currentPage ? 'active' : ''}">
            <a class="page-link" href="#" data-page="${i}">${i}</a>
          </li>`
        );
      }
  
      pagination.append(
        `<li class="page-item ${currentPage === totalPages ? 'disabled' : ''}">
          <a class="page-link" href="#" data-page="${currentPage + 1}">&raquo;</a>
        </li>`
      );
  
      pagination.find('a').on('click', function (e) {
        e.preventDefault();
        const page = $(this).data('page');
        if (page && page !== currentPage) {
          currentPage = page;
          loadData();
        }
      });
    }
  
    // 검색 버튼 클릭 이벤트
    searchButton.on('click', function () {
      searchQuery = searchInput.val();
      currentPage = 1; // 검색 시 첫 페이지로 이동
      loadData();
    });
  
    // 리스트 아이템 클릭 이벤트
    list.on('click', '.artist-item', function () {
      const itemName = $(this).find('div:nth-child(2)').text().trim();
      const itemId = $(this).data('id');
  
      // 선택한 값(targetInput)에 결과 설정
      if (targetInput) {
        targetInput.val(`${itemName}`);
      }
      modal.fadeOut(); // 모달 닫기
    });
  
    // input 클릭으로 모달 열기
    $(`[data-modal="${modalId}"]`).on('click', function () {
      targetInput = $(this); // 클릭한 input 요소 저장
      modal.fadeIn(); // 모달 열기
      loadData(); // 데이터 로드
    });
  
    // 초기 데이터 로드
    loadData();
  }
  
  // 모달 초기화
  setupModal('modal1', 'artists'); // 모달1: artists 데이터
  setupModal('modal2', 'artists');  // 모달2: albums 데이터
  setupModal('modal3', 'rightholder', {
    updateList: (data, list) => {
      // 모달3 전용 리스트 렌더링
      data.rightholders.forEach(rightholder => {
        const image = rightholder.profile_image || "default_image.png";
        list.append(
          `<li class="list-group-item artist-item" data-id="${rightholder.user_code}">
          <div>${rightholder.user_name}</div>
          <div>${rightholder.user_code}</div>
          <div>${rightholder.email}</div>
          <div>${rightholder.user_level}</div>
        </li>`
        );
      });
    }
  });
  