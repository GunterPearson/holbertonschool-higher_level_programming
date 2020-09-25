$('document').ready(function () {
  $('INPUT#btn_translate').click(hello);
  $('INPUT#language_code').focus(function () {
    $(this).keydown(function (event) {
      if (event.which == 13) {
        hello();
      }
    });
  });
});

function hello () {
  $.get('https://www.fourtonfish.com/hellosalut/?lang=' + $('INPUT#language_code').val(), function (data) {
    $('DIV#hello').empty();
    $('DIV#hello').append(data.hello);
  });
}
