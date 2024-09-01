document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchBySelect = document.getElementById('search-by');
    const suggestionsList = document.getElementById('suggestions-list');

    searchInput.addEventListener('input', function() {
        const query = searchInput.value;
        const searchBy = searchBySelect.value;

        if (query.length < 1) {
            suggestionsList.innerHTML = ''; // No mostrar sugerencias si la consulta es demasiado corta
            return;
        }

        fetch(`/search-suggestions/?q=${query}&search_by=${searchBy}`)
            .then(response => response.json())
            .then(data => {
                suggestionsList.innerHTML = '';
                data.suggestions.forEach(suggestion => {
                    const li = document.createElement('li');
                    li.className = 'list-group-item';
                    li.textContent = suggestion;
                    li.addEventListener('click', () => {
                        searchInput.value = suggestion;
                        suggestionsList.innerHTML = '';
                    });
                    suggestionsList.appendChild(li);
                });
            });
    });
});
