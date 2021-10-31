/*<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>*/

{
  'use strict';

  $('.good').on('click', function() {
    const problem_pk = $(this).data('id')
    console.log($('#likeNum_' + problem_pk).val())
    console.log('#likeNum_' + problem_pk)
  })

  $('.like_button').on('click', function(e) {
    const problem_pk = $(this).data('id')
    e.preventDefault();
    $.ajax({
      'url':$(this).prop('action'),
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