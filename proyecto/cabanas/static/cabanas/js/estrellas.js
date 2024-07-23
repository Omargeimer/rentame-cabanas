document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('#rating span');
    let selectedValue = 0;
    const numeroEstrellasInput = document.querySelector('input[name="numero_estrellas"]');
    const calif = document.getElementById('calif');

    stars.forEach(star => {
        star.addEventListener('mouseover', () => {
            const value = parseInt(star.getAttribute('data-value'));
            updateStars(value, 'hovered');
        });

        star.addEventListener('mouseout', () => {
            updateStars(selectedValue, 'selected');
        });

        star.addEventListener('click', () => {
            const value = parseInt(star.getAttribute('data-value'));
            if (selectedValue === value) {
                selectedValue = 0; // Deseleccionar estrella 
            } else {
                selectedValue = value;
            }
            updateStars(selectedValue, 'selected');

            // Muestra la cantidad de estrellas
            document.getElementById('Calificación-value').textContent = `Calificación: ${selectedValue}/5 estrellas`;

            // Guarda el valor en el campo oculto
            numeroEstrellasInput.value = selectedValue;

            console.log(selectedValue);
            // Muestra la valoración de la cabaña dependiendo del número de estrellas
            switch (selectedValue) {
                case 5:
                    calif.textContent = 'Valoración: Excelente';
                    break;
                case 4:
                    calif.textContent = 'Valoración: Buena';
                    break;
                case 3:
                    calif.textContent = 'Valoración: Regular';
                    break;
                case 2:
                    calif.textContent = 'Valoración: Mala';
                    break;
                case 1:
                    calif.textContent = 'Valoración: Muy mala';
                    break;
                default:
                    calif.textContent = 'Sin Valoraciones';
                    break;
            }
        });
    });

    // Animación de las estrellas
    function updateStars(value, className) {
        stars.forEach(star => {
            const starValue = parseInt(star.getAttribute('data-value'));
            if (starValue <= value) {
                star.classList.add('selected');
                star.classList.add('animated-star');
            } else {
                star.classList.remove('selected');
                if (className === 'hovered') {
                    star.classList.add('animated-star');
                } else {
                    star.classList.remove('animated-star');
                }
            }
        });
    }
});
