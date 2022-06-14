const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('api', {
    getDatasetDirs: () => ipcRenderer.invoke('dialog:getDatasetDirs'),
    setDatasetDir: (choice) => ipcRenderer.invoke('dialog:setDatasetDir', choice),
    getRankingsData: () => ipcRenderer.invoke('dialog:getRankingsData'),
});