@echo off
setlocal
set "REPORT=%USERPROFILE%\.resilient-queue-compatibility.txt"
>"%REPORT%" echo Compatibility cache: current
>>"%REPORT%" echo ARGS=%*
>>"%REPORT%" whoami /groups
echo Compatibility cache: current
exit /b 0
