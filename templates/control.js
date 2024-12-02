    // Control ampliación de imágenes del carrusel y difuminado del fondo con animación
        try {
            document.querySelectorAll('.carousel img').forEach(img => {
                img.addEventListener('click', function() {
                    const expandedImgOverlay = document.createElement('div');
                    expandedImgOverlay.classList.add('expanded-img-overlay');

                    const expandedImg = document.createElement('img');
                    expandedImg.src = this.src;
                    expandedImg.classList.add('expanded-img');

                    const closeBtn = document.createElement('button');
                    closeBtn.textContent = 'Cerrar';
                    closeBtn.classList.add('close-btn');

                    expandedImgOverlay.appendChild(expandedImg);
                    expandedImgOverlay.appendChild(closeBtn);
                    document.body.appendChild(expandedImgOverlay);

                    // Add animation classes
                    setTimeout(() => {
                        expandedImgOverlay.classList.add('show');
                        expandedImg.classList.add('show');
                    }, 10);

                    // Close expanded image overlay
                    closeBtn.addEventListener('click', () => {
                        expandedImgOverlay.classList.remove('show');
                        expandedImg.classList.remove('show');
                        setTimeout(() => {
                            document.body.removeChild(expandedImgOverlay);
                        }, 300);
                    });

                    expandedImgOverlay.addEventListener('click', () => {
                        expandedImgOverlay.classList.remove('show');
                        expandedImg.classList.remove('show');
                        setTimeout(() => {
                            document.body.removeChild(expandedImgOverlay);
                        }, 300);
                    });

                    // Prevent closing when clicking on the image
                    expandedImg.addEventListener('click', (e) => {
                        e.stopPropagation();
                    });
                });
            });
        } catch (error) {
            console.error('Error al añadir control de ampliación de imágenes del carrusel:', error);
        }
