document.addEventListener('DOMContentLoaded', function() {
    const stars = document.querySelectorAll('#rating span');
    let selectedValue = 0;

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
            //Muestra la cantidad de estrellas
            document.getElementById('Calificación-value').textContent = `Calificación: ${selectedValue }/5 estrellas`;
            //Muestra la valoración de la cabaña dependiendo del número de estrellas
            if (selectedValue==5){
                calif.textContent = 'Valoración: Excelente';
            }
            else if (selectedValue==4){
                calif.textContent = 'Valoración: Buena';
            }
            else if (selectedValue==3){
                calif.textContent = 'Valoración: Regular';
            }
            else if (selectedValue==2){
                calif.textContent = 'Valoración: Mala';
            }
            else if (selectedValue==1){
                calif.textContent = 'Valoración: Muy mala';
            }
            else{
                calif.textContent = 'Sin Valoraciones';
            }
        });
    });
    //Animación de las estrellas
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
