document.addEventListener('DOMContentLoaded', function() {
    const precioInput = document.querySelector('input[name="precio"]');
    
    precioInput.addEventListener('input', function() {
        if (isNaN(precioInput.value) || precioInput.value < 0) {
            precioInput.setCustomValidity('Por favor, ingrese un valor numérico válido.');
        } else {
            precioInput.setCustomValidity('');
        }
    });
});
