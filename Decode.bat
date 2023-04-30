@echo off

if "%~1"=="" (
    echo No file was dragged and dropped onto the batch file.
    pause
) else (
    python Main/B64_Decode.py "%~1"
)