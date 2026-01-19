@echo off
REM Build script for LinxTap Windows application

echo ========================================
echo Building LinxTap for Windows
echo ========================================
echo.

REM Check if .NET SDK is installed
dotnet --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: .NET SDK not found!
    echo Please install .NET 8.0 SDK from https://dot net.microsoft.com/download
    exit /b 1
)

echo Cleaning previous builds...
if exist "LinxTap\bin" rmdir /s /q "LinxTap\bin"
if exist "LinxTap\obj" rmdir /s /q "LinxTap\obj"

echo.
echo Building Release version...
cd LinxTap
dotnet publish -c Release -r win-x64 --self-contained true -p:PublishSingleFile=true -p:PublishTrimmed=false

if errorlevel 1 (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    cd ..
    exit /b 1
)

cd ..

echo.
echo ========================================
echo BUILD SUCCESSFUL!
echo ========================================
echo.
echo Executable location:
echo   LinxTap\bin\Release\net8.0-windows\win-x64\publish\LinxTap.exe
echo.
echo File size:
for %%A in ("LinxTap\bin\Release\net8.0-windows\win-x64\publish\LinxTap.exe") do echo   %%~zA bytes (%%~zA / 1024 / 1024 MB)
echo.
echo You can now distribute the LinxTap.exe file.
echo It's a standalone executable that doesn't require .NET installation.
echo.

pause
