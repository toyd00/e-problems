{
  let i = 2;
  const total_forms = document.getElementById('id_choice_set-TOTAL_FORMS')
  document.querySelector('#add').addEventListener('click', (event) => {
    if (event) {
      event.preventDefault();
    }
    const empty_form = document.getElementById('empty-form').cloneNode(true);
    empty_form.setAttribute('class', 'problem-form');
    const empty_form_count = document.getElementsByClassName('problem-form').length
    empty_form.setAttribute('id', `form-${empty_form_count}`);
    const options = document.querySelector('#options');
    const regrex = new RegExp('__prefix__', 'g');
    empty_form.innerHTML = empty_form.innerHTML.replace(regrex, empty_form_count)
    total_forms.setAttribute('value', empty_form_count + 1)
    options.append(empty_form);

    i += 1;
  });
}