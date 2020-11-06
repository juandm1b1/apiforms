$(document).ready(function(){
    
    $('.eliminar').click(function eliminarRegistro(event){
        r=confirm("¿Está seguro de querer eliminar el registro?");
        if(r==true){                        
            alert("Registro eliminado");
        }else{
            event.preventDefault();
            alert("Se ha cancelado la eliminación");
        }
    })

})