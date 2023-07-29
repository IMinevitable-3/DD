function addTask() {
const taskInput = document.getElementById('taskInput');
const taskText = taskInput.value.trim();

if (taskText !== '') {
    const taskList = document.getElementById('taskList');
    const newTask = document.createElement('li');

    
    const taskTextSpan = document.createElement('span');
    taskTextSpan.textContent = taskText;

    
    const removeButton = document.createElement('button');
    removeButton.textContent = 'Remove';
    removeButton.onclick = function() {
    removeTask(this.parentElement);
    };

    newTask.appendChild(taskTextSpan);
    newTask.appendChild(removeButton);
    taskList.appendChild(newTask);

    taskInput.value = '';
}
}


function removeTask(task) {
task.remove();
}


function submitTasks() {
const taskList = document.getElementById('taskList');
const allTasks = taskList.querySelectorAll('li');
const selectedDate = document.getElementById('dateInput').value;

const taskArray = [];
allTasks.forEach((task) => {
    taskArray.push(task.querySelector('span').textContent.trim());
});


alert(`Selected Date: ${selectedDate}\nSubmitted Tasks:\n${taskArray.join('\n')}`);
}

