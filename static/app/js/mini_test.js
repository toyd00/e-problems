
{
  'use strict';

  $('.like_button').on('click', function(e) {
    if (e){
      e.preventDefault();
    }
    const problem_pk = $(this).data('id');

    $.ajax({
      'url': $(this).prop('action'),
      'type': $(this).prop('method'),
      'data': {
        'like_num': $('#likeCount_' + problem_pk).text(),
      },
      'dataType': 'json',
    })
    .done(function(response){
      $('#likeCount_' + problem_pk).text(response.like_count);
      $('#button_' + problem_pk).text(response.button);
    });
  });
}