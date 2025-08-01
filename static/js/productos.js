document.addEventListener("DOMContentLoaded", function () {
    const inputBusqueda = document.getElementById("busqueda");
    const form = document.getElementById("form-producto");
    
    window.mostrarFormulario = function (tipo) {
        document.getElementById("formulario-emergente").classList.remove("oculto");

        if (tipo === 'nuevo') {
            form.reset();
            document.getElementById("titulo-formulario").textContent = "Insertar un nuevo producto";
            document.getElementById("producto_id").value = "";
        } else if (tipo === 'modificar') {
            const seleccionado = document.querySelector("#tabla-productos tr.seleccionado");
            if (!seleccionado) {
                mostrarMensaje();
                return;
            }

            document.getElementById("titulo-formulario").textContent = "Modificar producto";
            const celdas = seleccionado.querySelectorAll("td");

            form.elements['codigo'].value = celdas[0].textContent.trim();
            form.elements['id_prov'].value = celdas[1].textContent.trim();
            form.elements['id_frcc'].value = celdas[2].textContent.trim();
            document.getElementById("producto_id").value = seleccionado.dataset.id;
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
    const tabla = $('#tabla-productos').DataTable({
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
            .column(0) // Buscar por código de producto
            .search(this.value)
            .draw();
    });

    $('#tabla-productos tbody').on('click', 'tr', function () {
        if ($(this).hasClass('seleccionado')) {
            $(this).removeClass('seleccionado');
        } else {
            $('#tabla-productos tbody tr').removeClass('seleccionado');
            $(this).addClass('seleccionado');
            filaSeleccionada = $(this);
        }
    });
});
