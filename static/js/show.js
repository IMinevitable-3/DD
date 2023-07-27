const showFormButton = document.getElementById('showFormButton');
const myForm = document.getElementById('myForm');

showFormButton.addEventListener('click', function () {
    myForm.style.display = myForm.style.display === 'none' ? 'block' : 'none';
});
