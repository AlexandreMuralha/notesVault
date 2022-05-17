20200518_220912

### Electron on WSL

After hours falling into a bunch of errors while trying to launch electron from WSL, I found the easiest way is to install electron on Windows then start it from WSL.Steps:

1. Make sure you have **Node.js & npm installed on your Windows machine** (you can remove them afterwards). 
2. Open **cmd.exe, move to your project directory and run npm install electron –save-dev**. This will install the Windows version of the prebuilt Electron binary instead of the Linux one, which would occur if you try to install from WSL. (This is the actual trick) 
3. Enter Bash on Ubuntu on Windows, move to your project directory then run ./node_modules/.bin/electron (or use an npm script) to launch your Electron app

Though, I’m not sure this is very convenient, it seems to work well. I hope this will help people encoutering the same issue in the future!

---

Thanks for the tip. It worked for me too. I had previously installed the linux version in bash and I had to **delete the node_modules/electron** folder and the install from Windows CMD.

Indeed, you could also **npm uninstall electron** then **npm install electro**

https://github.com/electron-userland/electron-prebuilt/issues/260

---

I found the easiest way is to install electron on Windows then start it from WSL.

---

**tags:** #electron #wsl #javascript 
**links:**
https://github.com/electron-userland/electron-prebuilt/issues/260