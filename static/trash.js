

    // instantiate single modal form
// instantiate single modal form
document.addEventListener('DOMContentLoaded', (e) => {
  modalForm(document.getElementById('create_artist_btn'), {
    formURL: "{% url 'maincms:create_artist' %}"
  })
});


function showDiv() {
    var checkBox = document.getElementById("other_artist");
    var checkBox2 = document.getElementById("none_linem");
    var div = document.getElementById("in_artist");
    var div2 = document.getElementById("Albums");
    if (checkBox.checked == true){
        div.style.display = "block";
    } else {
       div.style.display = "none";
    }
    if (checkBox2.checked == true){
        div2.value = "NO";
        document.getElementById("Melon_ID").value = "none";
        document.getElementById("Apple_url").value = "none";
        document.getElementById("Spotify_ID").value = "none";
        document.getElementById("Youtube_ID").value = "none";
    } else {
        document.getElementById("Albums").value = "";
        document.getElementById("Melon_ID").value = "";
        document.getElementById("Apple_url").value = "";
        document.getElementById("Spotify_ID").value = "";
        document.getElementById("Youtube_ID").value = "";
    }
}

