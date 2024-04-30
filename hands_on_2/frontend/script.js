document.addEventListener('DOMContentLoaded', function() {
    fetch('http://localhost:5000/api/items')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('items');
            data.forEach(item => {
                const li = document.createElement('li');
                li.textContent = item[1];
                list.appendChild(li);
            });
        });
});
