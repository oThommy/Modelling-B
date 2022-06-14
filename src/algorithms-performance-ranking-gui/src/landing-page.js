const $dropdown = document.getElementById('dropdown-dataset-dirs');

async function init() {
    const dataset_dirs = await window.api.getDatasetDirs();
    // const dataset_dirs = [];

    for (const [index, [ datasetDir, _ ]] of dataset_dirs.entries()) {
        let $dropdownItem = document.createElement('a');
        $dropdownItem.classList.add('dropdown-item');
        $dropdownItem.innerText = datasetDir;

        $dropdownItem.addEventListener('click', async function() {
            await window.api.setDatasetDir(index);
            window.location.href = 'index.html';
        });

        $dropdown.appendChild($dropdownItem);
    }
}

init();