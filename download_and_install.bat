@echo off

REM Code from https://stackoverflow.com/a/10052222/13921835
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------



cd /D %ProgramFiles%
@RD /S /Q "discord-better-scss"
mkdir "Discord Better SCSS" >nul 2>&1
cd "Discord Better SCSS"

curl -so "zipjs.bat" https://raw.githubusercontent.com/npocmaka/batch.scripts/master/hybrids/jscript/zipjs.bat
curl -so "main.zip" https://codeload.github.com/TayIsAsleep/discord-better-scss/zip/refs/heads/main

@RD /S /Q main
call zipjs.bat unzip -source "%cd%\main.zip" -destination "%cd%\main" -keep no -force no
del "zipjs.bat"

cd "main/discord-better-scss-main/"
python installer.py

cd /D "%AppData%\BetterDiscord\themes"
start .