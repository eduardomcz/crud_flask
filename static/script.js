document.getElementById('fab').addEventListener('click', function() {
    document.getElementById('form-container').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
});

document.getElementById('overlay').addEventListener('click', function() {
    document.getElementById('form-container').style.display = 'none';
    document.getElementById('update-form-container').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
});

document.addEventListener('DOMContentLoaded', function() {
    const updateLinks = document.querySelectorAll('.update-link');
    const updateFormContainer = document.getElementById('update-form-container');
    const updateForm = document.getElementById('update-form');
    const updateId = document.getElementById('update-id');
    const updateNome = document.getElementById('update-nome');
    const updateEmail = document.getElementById('update-email');
    const updateCpf = document.getElementById('update-cpf');

    // Formatar todos os CPFs na tabela
    document.querySelectorAll('.cpf').forEach(function(element) {
        element.textContent = formatCPF(element.textContent);
    });

    updateLinks.forEach(link => {
        link.addEventListener('click', function(event) {
            event.preventDefault();
            updateId.value = this.dataset.id;
            updateNome.value = this.dataset.nome;
            updateEmail.value = this.dataset.email;
            updateCpf.value = formatCPF(this.dataset.cpf); // Formatar CPF ao abrir o formulário de atualização
            document.getElementById('overlay').style.display = 'block';
            updateFormContainer.style.display = 'block';
        });
    });

    updateForm.addEventListener('submit', function(event) {
        event.preventDefault();
        const formData = new FormData(updateForm);
        fetch('/atualizar', {
            method: 'POST',
            body: formData
        }).then(response => {
            if (response.ok) {
                window.location.reload();
            }
        });
    });
});

function formatCPF(cpf) {
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, "$1.$2.$3-$4");
}
