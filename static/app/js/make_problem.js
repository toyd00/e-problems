{
  'use strict';
  $(document).on('click', '.add', function(event) {
    if (event) {
      event.preventDefault();
    }
    const empty_form_count = $('.problem-form').length;
    const empty_form = $('#empty-form').clone(true);
    const form_set = $('#form-set')
      .clone(true)
      .attr({
        id: `form-set-${empty_form_count + 1}`,
        class: 'form-set',
      })
    console.log(form_set)
    empty_form
      .attr({
        id: `form-${empty_form_count + 1}`,
        class: 'problem-form',
      })
      .html(empty_form.html().replace(/__prefix__/g, empty_form_count))
      .appendTo(form_set);

    $('#remove-button')
      .clone(true)
      .attr({
        id: `remove-${empty_form_count + 1}`,
        class: 'remove',
        'data-id': `${empty_form_count + 1}`
      })
      .appendTo(form_set);

    $('#answer-button')
      .clone(true)
      .attr({
        id: `answer-${empty_form_count + 1}`,
        class: 'answer',
        name: 'answer'
      })
      .appendTo(form_set);
    form_set.appendTo($('#options'))
    $('#id_form-TOTAL_FORMS').attr('value', empty_form_count + 1);
  })

  $(document).on('click', '.remove', function(event) {
    if (event) {
      event.preventDefault();
    }
    if ($('.problem-form').length <= 2){
      alert('選択肢は２個以上必要です');
      return
    }

    const id = $(this).data('id');
    for(var i=id; i <= $('.problem-form').length; i++){
      const regrex = new RegExp(i - 1, 'g');
      $(`#id_form-${i - 1}-content`).val($(`#id_form-${i}-content`).val());
    }

    $(`#form-set-${$('.problem-form').length}`).remove();
    $('#id_form-TOTAL_FORMS').attr('value', $('.problem-form').length);
  })
}
