function fetchSuggestions(input) {
const url = `/get-names?search=${input}`;

return fetch(url)
    .then(response => response.json())
    .then(data => data.payload)
    .catch(error => {
    console.error('Error fetching suggestions:', error);
    return [];
    });
}

function showSuggestions(suggestions) {
const suggestionList = document.getElementById('suggestion-list');
suggestionList.innerHTML = '';

suggestions.forEach(suggestion => {
    const li = document.createElement('li');
    li.textContent = suggestion.name;
    suggestionList.appendChild(li);
});
}


document.getElementById('autocomplete').addEventListener('input', function () {
const input = this.value.trim();
if (input === '') {
    showSuggestions([]);
} else {
    fetchSuggestions(input)
    .then(suggestions => showSuggestions(suggestions));
}
});


document.getElementById('suggestion-list').addEventListener('click', function (event) {
const selectedValue = event.target.textContent;
document.getElementById('autocomplete').value = selectedValue;
showSuggestions([]);
});

function addToSelectedList(value) {
const selectedValuesList = document.getElementById('selected-values');


const li = document.createElement('li');
li.textContent = value;

const removeButton = document.createElement('button');
removeButton.textContent = 'Remove';
removeButton.addEventListener('click', function () {
    li.remove();
});

li.appendChild(removeButton);
selectedValuesList.appendChild(li);
}



document.getElementById('suggestion-list').addEventListener('click', function (event) {
const selectedValue = event.target.textContent;
document.getElementById('autocomplete').value = selectedValue;
showSuggestions([]);


addToSelectedList(selectedValue);
});


document.getElementById('submit-button').addEventListener('click', function () {
const selectedValuesList = document.getElementById('selected-values');
const selectedDate = document.getElementById('selected-date').value;

const selectedValues = Array.from(selectedValuesList.children)
    .map(li => li.textContent);


console.log('Selected Values:', selectedValues);
console.log('Selected Date:', selectedDate);

});
