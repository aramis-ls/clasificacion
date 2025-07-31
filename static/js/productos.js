document.addEventListener("DOMContentLoaded", function () {
    $('#tabla').DataTable();
});

function buscar() {
    const query = document.getElementById("search-input").value;
    window.location.href = `?q=${query}`;
}

function seleccionar(id, codigo, cliente, fraccion) {
    document.getElementById('producto_id').value = id;
    document.querySelector('[name="codigo"]').value = codigo;
    document.querySelector('[name="id_prov"]').value = cliente;
    document.querySelector('[name="id_frcc"]').value = fraccion;
}
