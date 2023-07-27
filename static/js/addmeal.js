const addInputButton = document.getElementById('addInputButton');
const inputContainer = document.getElementById('inputContainer');

addInputButton.addEventListener('click', function () {
    const newInput = document.createElement('input');
    newInput.type = 'text';
    newInput.name = 'dynamicInput[]'; 
    inputContainer.appendChild(newInput);
});
