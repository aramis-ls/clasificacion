document.addEventListener("DOMContentLoaded", function () {
    const inputBusqueda = document.getElementById("busqueda");
    const form = document.getElementById("form-fraccion");
    window.mostrarFormulario = function (tipo) {
        document.getElementById("formulario-emergente").classList.remove("oculto");

        if (tipo === 'nuevo') {
            form.reset();
            document.getElementById("titulo-formulario").textContent = "Insertar una nueva fraccion";
            document.getElementById("fraccion_id").value = "";
        } else if (tipo === 'modificar') {
            const seleccionado = document.querySelector("#tabla-fracciones tr.seleccionado");
            if (!seleccionado) {
                mostrarMensaje();
                return;
            }
            document.getElementById("titulo-formulario").textContent = "Modificar fraccion";
            const celdas = seleccionado.querySelectorAll("td");

            form.elements['nombre_prov'].value = celdas[0].textContent.trim();
            form.elements['taxid'].value = celdas[1].textContent.trim();
            form.elements['domicilio'].value = celdas[2].textContent.trim();
            document.getElementById("fraccion_id").value = seleccionado.dataset.id;
        }
    };

    window.cerrarFormulario = function () {
        document.getElementById("formulario-emergente").classList.add("oculto");
        form.reset();
    };

    window.mostrarMensaje = function () {
        document.getElementById("mensaje-emergente").classList.remove("oculto");
    };

    window.cerrarMensaje = function () {
        document.getElementById("mensaje-emergente").classList.add("oculto");
    };
    
});
$(document).ready(function () {
    const tabla = $('#tabla-fracciones').DataTable({
        language: {
            search: "",
            searchPlaceholder: "",
            lengthMenu: "Mostrar _MENU_ registros por página",
            info: "Mostrando _START_ a _END_ de _TOTAL_ registros",
            paginate: {
                previous: "Anterior",
                next: "Siguiente"
            },
            emptyTable: "No hay datos disponibles en la tabla",
        },
        dom: 'lrtip'
    });

    $('#busqueda').on('keyup', function () {
        tabla
            .column(0) // Asegúrate que la columna 0 es nombre_prov
            .search(this.value)
            .draw();
    });


    $('#tabla-fracciones tbody').on('click', 'tr', function () {
        if ($(this).hasClass('seleccionado')) {
            $(this).removeClass('seleccionado');
        } else {
            $('#tabla-fracciones tbody tr').removeClass('seleccionado');
            $(this).addClass('seleccionado');
            filaSeleccionada = $(this);
        }
    });

});
