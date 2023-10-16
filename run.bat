@echo off
setlocal enabledelayedexpansion

REM Check if two Excel files were provided as arguments
if "%~2"=="" (
    if "%~1"=="" (
        echo Please drag and drop a data Excel file onto the script.
        pause
        exit /b
    ) else (
        set data_path=%~1
        set image_path=
    )
) else (
    set data_path=%~1
    set image_path=%~2
)

REM Run the Python script with the appropriate arguments
if not "!image_path!"=="" (
    python utils/xlsx_to_csv.py -d "!data_path!" -i "!image_path!"
) else (
    python utils/xlsx_to_csv.py -d "!data_path!"
)

REM Wait for a key press to close
pause

endlocal
