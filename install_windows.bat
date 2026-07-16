@echo off
echo Complete Bible Archive - Windows Installer
echo ==========================================
echo.

REM Check for Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python not found. Please install Python 3.8+
    pause
    exit /b 1
)

echo [1/5] Installing dependencies...
pip install sqlite3 colorama

echo [2/5] Setting up directories...
mkdir data 2>nul
mkdir exports 2>nul
mkdir docs 2>nul

echo [3/5] Verifying database...
if not exist "data\complete_bible.db" (
    echo WARNING: Database not found. Run import scripts first.
)

echo [4/5] Creating shortcuts...
echo python tools\search_system.py > Search.bat
echo python tools\analyzers\seeds_decoder_v3.py > Analyze.bat

echo [5/5] Done!
echo.
echo Usage:
echo   Search.bat    - Search the archive
echo   Analyze.bat   - Run analysis
echo   README.md     - Documentation
echo.
pause
