@echo off

:: Install requirements from a file using pip
pip install -r requirements.txt

:: Pause to wait for user input
echo Dependencies installed successfully!
echo Press any key to close...
pause > nul