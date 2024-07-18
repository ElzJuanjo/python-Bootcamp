$(function () {
    let msgError = document.querySelector('#msgError').innerHTML;
    Swal.fire({
        title: msgError,
        icon: "error",
        confirmButtonText: "Aceptar",
        confirmButtonColor: "#d35631"
    });
});