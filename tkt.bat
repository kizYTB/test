@echo off
setlocal

REM URL du fichier à télécharger
set FILE_URL=https://drive.usercontent.google.com/download?id=1cAlw3WHZD7NhFeFR4ULy8YudYMzIkIq1&export=download&authuser=0&confirm=t&uuid=b2b81c7f-523d-4056-8d96-35815f69bf19&at=APZUnTXVng41z9-SwKMplUgEXjBV:1719015323762

REM Emplacement où enregistrer le fichier téléchargé (répertoire temporaire de l'utilisateur)
set SAVE_PATH=%TEMP%\temp.py

REM Utilisation de bitsadmin pour démarrer le téléchargement en arrière-plan
bitsadmin /transfer myDownloadJob /download /priority normal %FILE_URL% %SAVE_PATH%

REM Vérification si le téléchargement a réussi
if exist "%SAVE_PATH%" (
    echo Téléchargement terminé : %SAVE_PATH%
) else (
    echo Erreur lors du téléchargement du fichier depuis %FILE_URL%
)

pause
