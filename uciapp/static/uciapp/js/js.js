        function actualizarSignos() {
            $.getJSON("{% url 'valores' %}", function(data) {
                $("#fc").text(data.fc);
                $("#ta").text(data.ta);
                $("#pox").text(data.pox);
            });
        }

        setInterval(actualizarSignos, 2000);

        $("#emergencia").on("click", function() {
            $.get("{% url 'emergencia' %}", function() {
                alert("¡Emergencia! Los signos vitales han cambiado.");
                actualizarSignos();
            });
        });


        // Canvas para simular el electrocardiograma
        const canvas = document.getElementById('ecg-canvas');
        const ctx = canvas.getContext('2d');
        canvas.width = canvas.clientWidth;
        canvas.height = canvas.clientHeight;

        // Parámetros del patrón ECG
        const ecgPattern = [
            { x: 0, y: 0 },    // Inicio del ciclo
            { x: 10, y: 0 },   // Línea base
            { x: 15, y: -15 }, // Pico de onda P
            { x: 25, y: 0 },   // Retorno a la línea base
            { x: 35, y: 20 },  // Pico Q (negativo)
            { x: 45, y: -35 }, // Pico R (positivo)
            { x: 55, y: 15 },  // Pico S (negativo)
            { x: 65, y: 0 },   // Retorno a la línea base
            { x: 75, y: 10 },  // Onda T
            { x: 90, y: 0 }    // Fin del ciclo
        ];
        const waveHeight = canvas.height / 2; // Centro de la onda
        let xOffset = 0;

        // Función para dibujar el patrón ECG
        function drawECGWave() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.beginPath();

            ecgPattern.forEach((point, index) => {
                const x = point.x + xOffset;
                const y = waveHeight - point.y;

                if (index === 0) {
                    ctx.moveTo(x, y);
                } else {
                    ctx.lineTo(x, y);
                }
            });

            ctx.strokeStyle = '#0f0';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Actualizar la posición horizontal
            xOffset -= 2;
            if (xOffset <= -90) xOffset = 0; // Reiniciar ciclo al completar el patrón
        }

        // Actualizar la gráfica ECG cada 50 ms
        setInterval(drawECGWave, 50);
