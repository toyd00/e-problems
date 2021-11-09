{
  const total_forms = document.getElementById('id_form-TOTAL_FORMS')
  const regrex = new RegExp('__prefix__', 'g');
  const options = document.querySelector('#options');
  document.querySelector('#add').addEventListener('click', (event) => {
    if (event) {
      event.preventDefault();
    }
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    empty_form.setAttribute('class', 'problem-form');
    const empty_form_count = document.getElementsByClassName('problem-form').length
    empty_form.setAttribute('id', `form-${empty_form_count}`);
    empty_form.innerHTML = empty_form.innerHTML.replace(regrex, empty_form_count)
    total_forms.setAttribute('value', empty_form_count)
    options.append(empty_form);
    const button = document.getElementById('remove-button').cloneNode(true);
    //const button = document.createElement('button');
    //button.textContent = '削除'
    button.setAttribute('id', `remove-${empty_form_count}`);
    button.setAttribute('class', 'remove');
    button.setAttribute('data-id', `${empty_form_count}`);
    options.append(button);
  });

}
{
  $(document).on('click', '.remove', function(event) {
    console.log('iiii')
    if (event) {
      event.preventDefault();
    }
    const id = $(this).data('id');
    console.log('#form-' + (id - 1));
    $('#form-' + id).remove();
    $('#remove-' + id).remove();
    $('#string').remove();
  })
}
