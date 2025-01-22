// Function to open the modal and fetch data with optional query
function openModal(url, inputId) {

    // Function to fetch data and update modal content
    function fetchData(query = '') {
        $.get(url, { q: query }, function(response) {
            const data = response.data;
            $('#ar_fi_table').empty();
            if (data.length === 0) {
                $('#ar_fi_table').append('<p>No results found.</p>');
            } else {
                data.forEach(item => {
                    $('#ar_fi_table').append(`
                        <tr class="modal-item" data-value="${item.name || item.Artist_name}">
                            ${item.name || item.Albums}: ${item.value || item.Artist_name}
                        </tr>
                    `);
                });

                // Click event to select value
                $('.modal-item').on('click', function() {
                    const value = $(this).data('value');
                    $(inputId).val(value);
                    $('#modal').hide();
                });
            }
        });
    }

    // Initial fetch (without query)
    fetchData();

    // Search input keyup event
    $('#search-input').on('keyup', function() {
        const query = $(this).val();
        fetchData(query);
    });
}

// Button B click
$('#button-b').on('click', function() {
    openModal('/fetch-b-data/', '#input-b');
});

// Close modal
$('#close-modal').on('click', function() {
    $('#modal').hide();
    $('#search-input').off('keyup');  // Clean up event listener
});

    $(document).ready(function () {
        // Show modal when text input is clicked
        $('#album_artist').on('click', function () {
            openModal('maincms/artist_find/', '#album_artist');
          $('#aritst_find').fadeIn(); // Use fadeIn for a smooth effect
        });
  
        // Hide modal when close button is clicked
        $('.close-btn').on('click', function () {
          $('#aritst_find').fadeOut(); // Use fadeOut for a smooth effect
        });
  
        // Close modal when clicking outside the content
        $(window).on('click', function (e) {
          if ($(e.target).is('#myModal')) {
            $('#aritst_find').fadeOut();
          }
        });
      });