const $main = document.getElementsByTagName('main')[0];
const MAIN_WIDTH = '100vw';
let buttonIndex = 0;
let $mainWrapperArr = [];

function create2dTableElem(tableObj, caption) {
    let $table = document.createElement('table');
    $table.classList.add('table', 'table-striped', 'table-dark');

    // caption
    if (caption) {
        let $caption = document.createElement('caption');
        $caption.innerText = caption;
        $table.appendChild($caption);
    }

    // table head
    let $thead = document.createElement('thead');
    let $tr = document.createElement('tr');
    let $emptyTh = document.createElement('th');
    $emptyTh.setAttribute('scope', 'col');
    $emptyTh.innerText = '';
    $tr.appendChild($emptyTh);
    
    for (const n of Object.keys(tableObj)) {
        let $th = document.createElement('th');
        $th.setAttribute('scope', 'col');
        $th.innerText = n.toString();
        $tr.appendChild($th);
    }

    $thead.appendChild($tr);
    $table.appendChild($thead);

    // table body
    let $tbody = document.createElement('tbody');
    for (const [src, rowObj] of Object.entries(tableObj)) {
        // first (origin/source) column
        let $tr = document.createElement('tr');
        let $thN = document.createElement('th');
        $thN.setAttribute('scope', 'row');
        $thN.innerText = src.toString();
        $tr.appendChild($thN);

        // actual row values
        for (const val of Object.values(rowObj)) {
            $td = document.createElement('td');
            $td.innerText = val.toString();
            $tr.appendChild($td);
        }

        $tbody.appendChild($tr);
    }

    $table.appendChild($tbody);
    
    return $table;
}

function create1dTableElem(tableObj, caption) {
    let $table = document.createElement('table');
    $table.classList.add('table', 'table-striped', 'table-dark');

    // caption
    if (caption) {
        let $caption = document.createElement('caption');
        $caption.innerText = caption;
        $table.appendChild($caption);
    }

    // table head
    let $thead = document.createElement('thead');
    let $trHead = document.createElement('tr');
    
    for (const n of Object.keys(tableObj)) {
        let $th = document.createElement('th');
        $th.setAttribute('scope', 'col');
        $th.innerText = n.toString();
        $trHead.appendChild($th);
    }

    $thead.appendChild($trHead);
    $table.appendChild($thead);

    // table body
    let $tbody = document.createElement('tbody');
    let $tr = document.createElement('tr');

    // actual row values
    for (const val of Object.values(tableObj)) {
        $td = document.createElement('td');
        $td.innerText = val.toString();
        $tr.appendChild($td);
    }
    
    $tbody.appendChild($tr);
    $table.appendChild($tbody);
    
    return $table;
}

function createGraphIframe(htmlPath, caption) {
    let $iframe = document.createElement('iframe');
    $iframe.setAttribute('src', htmlPath);

    if (caption) {
        $iframe.setAttribute('title', caption);
        let $caption = document.createElement('caption');
        $caption.innerText = caption;
        $iframe.appendChild($caption);
    }

    return $iframe;
}

function leftButton() {
    buttonIndex -= 1;
    buttonIndex = Math.max(0, buttonIndex);
    for (const $mainWrapper of $mainWrapperArr) {
        $mainWrapper.style.transform = `translate(calc(-${buttonIndex} * ${MAIN_WIDTH}))`;
    }
    console.log(buttonIndex);
}

function rightButton() {
    buttonIndex += 1;
    buttonIndex = Math.min($mainWrapperArr.length - 1, buttonIndex);
    for (const $mainWrapper of $mainWrapperArr) {
        $mainWrapper.style.transform = `translate(calc(-${buttonIndex} * ${MAIN_WIDTH}))`;
    }
    console.log(buttonIndex);
}

async function init() {
    const rankingsDataArr = await window.api.getRankingsData();
    console.log(rankingsDataArr);

    for (const [index, rankingsData] of rankingsDataArr.entries()) {
        let $mainWrapper = document.createElement('div');
        $mainWrapper.classList.add('main-wrapper');
        
        // data column
        let $dataColumn = document.createElement('div');
        $dataColumn.classList.add('data-column-wrapper');

        const $wTable = create2dTableElem(rankingsData.ilpW, 'Flow \\( w_{ij} \\)');
        const $cTable = create2dTableElem(rankingsData.ilpC, 'Costs \\( c_{ij} \\)');
        const $fTable = create1dTableElem(rankingsData.ilpF, 'Fixed costs \\( f_i \\)');

        $dataColumn.appendChild($wTable);
        $dataColumn.appendChild($cTable);
        $dataColumn.appendChild($fTable);
        // $dataColumn.appendChild($dataTable);
        $mainWrapper.appendChild($dataColumn);

        // graph column
        let $graphColumn = document.createElement('div');
        $graphColumn.classList.add('graph-column-wrapper');

        let $iframeGurobi = createGraphIframe(rankingsData.gurobiGraphPath);
        let $iframeHeuristic = createGraphIframe(rankingsData.heuristic2GraphPath);

        $graphColumn.appendChild($iframeGurobi);
        $graphColumn.appendChild($iframeHeuristic);
        $mainWrapper.appendChild($graphColumn);

        $main.appendChild($mainWrapper);
        $mainWrapperArr.push($mainWrapper);
    }

    // left and right button
    let $leftButton = document.getElementById('left-button');
    let $rightButton = document.getElementById('right-button');
    $leftButton.addEventListener('click', leftButton);
    $rightButton.addEventListener('click', rightButton);

    console.log($main.children)
}

init();