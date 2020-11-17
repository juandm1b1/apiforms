$(document).ready(function(){
    
    $('.eliminar').click(function eliminarRegistro(event){
        r=confirm("¿Está seguro de querer eliminar el registro?");
        if(r==true){                        
            alert("Registro eliminado");
        }else{
            event.preventDefault();
            alert("Se ha cancelado la eliminación");
        }
    });

    $("#este_btn").click(function(){
        const value = JSON.parse(document.getElementById('este_id').textContent); 
        alert("El animal es " + value["animal"] + " y la categoría es " + value["categoria"]); 
        $(this).css({"background-color": "orange", "color": "green"});       
    });
})





