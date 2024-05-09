const btnVerify = document.getElementById('verifyProd');
const btnUpdate = document.getElementById('updateProd');
const btnDelete = document.getElementById('deleteProd');

const changePage = (url) => {
    window.location.href = url;
};

btnUpdate.addEventListener('click', () => {
    const id = btnUpdate.value;
    const url = '/update/product/' + id;
    changePage(url);
});

btnDelete.addEventListener('click', () => {
    const id = btnDelete.value;
    const url = '/delete/product/' + id;
    changePage(url);
});
