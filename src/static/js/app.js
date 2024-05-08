const btnVerify = document.getElementById('verifyProd')
const btnUpdate = document.getElementById('updateProd')
const btnDelete = document.getElementById('deleteProd')

function changePageUpdate() {
    const id = btnUpdate.value;
    const url = '/update/product/' + id; 
    window.location.href = url;  
}

function changeDeletePage(){
    const id = btnDelete.value;
    const url = '/delete/product/' + id;
    window.location.href = url;
}