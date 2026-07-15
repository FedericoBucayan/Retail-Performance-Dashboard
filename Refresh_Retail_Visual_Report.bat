@echo off
title Refresh Retail Visual Report
echo ============================================================
echo   REPLENISHING AND RECOMPILING RETAIL PERFORMANCE REPORT
echo ============================================================
echo.

:: Detect Python Command (prefer "py" launcher, then actual "python")
set PY_CMD=
py --version >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set PY_CMD=py
) else (
    python --version >nul 2>nul
    if %ERRORLEVEL% EQU 0 (
        :: Test if it is a working Python shell, not the Microsoft Store dummy redirector
        python -c "import sys" >nul 2>nul
        if %ERRORLEVEL% EQU 0 (
            set PY_CMD=python
        )
    )
)

if "%PY_CMD%"=="" (
    echo [ERROR] Python was not found on your system.
    echo Please install Python and ensure it is added to your environment PATH.
    echo.
    pause
    exit /b 1
)

echo [1/3] Loading database spreadsheets and aggregating records...
%PY_CMD% Reference_Material/prepare_data.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Database aggregation failed. Please check your Excel files.
    echo.
    pause
    exit /b %ERRORLEVEL%
)
echo.

echo [2/3] Merging template and compiling single-file dashboard...
%PY_CMD% Reference_Material/compile.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Dashboard compilation failed.
    echo.
    pause
    exit /b %ERRORLEVEL%
)
echo.

echo [3/3] Running validation check on compiled report...
%PY_CMD% Reference_Material/validate.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [WARNING] Validation checks failed. Dashboard might have layout errors.
    echo.
    pause
)
echo.

echo ============================================================
echo   COMPILATION COMPLETED SUCCESSFULLY!
echo   Opening index.html in your default browser...
echo ============================================================
echo.

start "" "index.html"
exit
