const { app, BrowserWindow, ipcMain } = require('electron');
const path = require('path');
const fs = require('fs')

// FIXME: refactor
let ALGO_PERFORMANCE_RANKING_DIR;
const ALGO_PERFORMANCE_RANKING_DIR_1 = path.join(__dirname, '..', '..', 'out/algo-performance-ranking');
const ALGO_PERFORMANCE_RANKING_DIR_2 = path.join(__dirname, '..', '..', '..', '..', '..', '..', 'out/algo-performance-ranking');
if (fs.existsSync(ALGO_PERFORMANCE_RANKING_DIR_1)) {
    ALGO_PERFORMANCE_RANKING_DIR = ALGO_PERFORMANCE_RANKING_DIR_1;
} else if (fs.existsSync(ALGO_PERFORMANCE_RANKING_DIR_2)) {
    ALGO_PERFORMANCE_RANKING_DIR = ALGO_PERFORMANCE_RANKING_DIR_2;
} else {
    error('Cannnot find algo-performance-ranking directory.');
}
const DATASET_DIRS = fs.readdirSync(ALGO_PERFORMANCE_RANKING_DIR, { withFileTypes: true })
    .filter(dirent => dirent.isDirectory())
    .sort((direntA, direntB) => direntB.name.localeCompare(direntA.name))
    .map((dirent) => [dirent.name, path.resolve(ALGO_PERFORMANCE_RANKING_DIR, dirent.name)]);
let datasetDirChoice;

function handleGetDatasetDirs() {
    return DATASET_DIRS;
}

function handleSetDatasetDir(event, choice) {
    datasetDirChoice = choice;
    return;
}

function handleGetRankingsData() {
    const [ _, datasetDir ] = DATASET_DIRS[datasetDirChoice];
    rankingsDataPath = path.join(datasetDir, 'guiData.json');
    const rankingsData = JSON.parse(fs.readFileSync(rankingsDataPath));
    return rankingsData;
}

const createWindow = () => {
    // Create the browser window.
    const mainWindow = new BrowserWindow({
      width: 800,
      height: 600,
      webPreferences: {
          preload: path.join(__dirname, 'preload.js')
      }
    });
  
    // and load the index.html of the app.
    mainWindow.loadFile(path.join(__dirname, 'landing-page.html'));
};
  
// This method will be called when Electron has finished
// initialization and is ready to create browser windows.
// Some APIs can only be used after this event occurs.
app.on('ready', () => {
    ipcMain.handle('dialog:getDatasetDirs', handleGetDatasetDirs);
    ipcMain.handle('dialog:setDatasetDir', handleSetDatasetDir);
    ipcMain.handle('dialog:getRankingsData', handleGetRankingsData);
    createWindow();
});

// Quit when all windows are closed, except on macOS. There, it's common
// for applications and their menu bar to stay active until the user quits
// explicitly with Cmd + Q.
app.on('window-all-closed', () => {
if (process.platform !== 'darwin') {
    app.quit();
}
});

app.on('activate', () => {
// On OS X it's common to re-create a window in the app when the
// dock icon is clicked and there are no other windows open.
if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
}
});