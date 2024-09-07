let dataTable;
let dataTableIsInitialized=false;

const dataTableOptions={
    columnDefs:[
        {className:'centered',targets:[0,1,2,3,4,5,6,7]},
        {orderable: false, targets: [0,3,7]},
        { searchable: false, targets: [0,3,7]}
    ],
    pageLength:4,
    destroy: true
}

const initDataTable=async()=>{
if(dataTableIsInitialized){
    dataTable.destroy();
}

await listArticles();

dataTable=$('#datatable-articulos').DataTable(dataTableOptions);

dataTableIsInitialized = true
};

const listArticles = async() => {
    try {
        const response = await fetch('http://127.0.0.1:8000/list_articles/');
        const data = await response.json();

        let content = ``;
        data.articulos.forEach((articulo) => {
            let autorContent = articulo.id_autor__nombre || 'Autor no asignado';
            let tipoContent;
            if (articulo.id_tipo_id === 1) {
                tipoContent = 'Informe Técnico';
            } else if (articulo.id_tipo_id === 2) {
                tipoContent = 'Acta de Congreso';
            } else  {
                tipoContent = 'Revista Científica';
            }
            
            content += `
                <tr>
                    <td>${articulo.id}</td>
                    <td><a href="/article/${articulo.id}/">${articulo.titulo}</a></td>
                    <td>${articulo.palabras_clave}</td>
                    <td>${articulo.copia === true ?"<i class='fa-solid fa-check' style='color: green;'></i>" : "<i class='fa-solid fa-xmark' style='color: red;'></i>"}</td>
                    <td>${articulo.ubicacion}</td>
                    <td><a href="/autor/${autorContent.id}/">${autorContent}</a></td>
                    <td>${tipoContent}</td>
                    <td>
                    <button class='btn btn-sm btn-primary' onclick="location.href='/article/${articulo.id}/edit'">
                        <i class='fa-solid fa-pencil'></i>
                    </button>
                    <button class='btn btn-sm btn-danger' onclick="location.href='/article/${articulo.id}/delete'">
                        <i class='fa-solid fa-trash-can'></i>
                    </button>
                    </td>
                </tr>
            `;
        });
        tableBody.innerHTML = content;
    } catch (ex) {
        
    }
}


window.addEventListener('load',async()=>{
    await initDataTable();
});

