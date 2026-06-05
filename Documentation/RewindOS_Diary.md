# Rewind OS Diary
## 29/5/2026
I suddenly think about the fiction Linux distro “KingSolution” from TADC and wanted to make my own Linux distro with a retro vibe like that.\
I asked Nova to know more about what “make a Linux distro” actually is. Then, she gave me a list of Linux concepts and programming languages that I need to learn to be able to make one by my own.
## 30/5/2026
I started to brainstorm out ideas for my dream Linux distro. Because most ideas were already existed, it is hard to think of making something that is unique.\
I asked Nova again, and spent the whole morning to finalize the concept of my dream distro. I drew it as a vision board on my iPad, everything was done in the morning.\
The concept is like this:\
**Distro name:** Rewind OS\
**Description:** A distro with retro-style desktop environment. Gives Windows 98 feeling to the machine but still allows to run modern applications.\
**Target user:** student, casual gamer, hobbyist, and Linux beginner.\
**Goal:**\
    • Calm user experience.\
    • Has personality.\
    • Even non-tech users will feel comfortable when use it (main goal).\
    • Be familiar to Windows users.\
    • A separate ISO especially made for machines that use NVIDIA graphic card.\
**Principles:** stable, simple to use, welcoming.\
**System:**\
    • Fedora-based.\
    • Desktop environment is XFCE.\
    • Core unique apps for the distro: Rewind Welcome, Rewind Settings, Rewind Technician, Kineat Base, Neato (built-in feature).\
**Features:**\
    • Human-friendly error explanation: translate the command errors in terminal into something that a non-tech person can understand.\
    • Built-in AI assistant for terminal problems: a built-in local AI will shows up if being called. It will help the user identifies and gives solutions to the terminal problems that user is facing.\
    • Retro game compatibility: instead of focusing experience on modern games like Steam games, the distro will come configured for playing retro games. Emulators like RetroArch and Dolphin will be automatically set up.\
    • Steam game compatibility: will be focus on configuring to be compatible with Steam games, but on the later updates.\
**Kineat Base:** is a database app comes prep-installed. It provides documentation about the distro.\
**Neato AI:** is the mascot of Rewind OS. It will show message bubble to talk to user. Only shows up when be called and shows its whole design when appear. Gives the vibe of a living character on the machine.\
Neato can suggest to open required apps to fix a problem. If its recommendation is approved by the user, it will automatically open the apps and run the fix.\
In the afternoon and evening, I started to learn the foundations of Linux operating system. This is phase 1 of the journey of making Rewind OS, I will need to understand the system before I make anything.\
## 31/5/2026
I finished learning phase 1 at nearly 4 pm. I’ve learned a lot of topics, include: terminal basics, filesystem structure, packages management, desktop environment, permissions, and shell scripting.\
**Conclusion:** a Linux distro is roughly: Linux kernel + Packages repositories + Package manager + Desktop environment + Configuration + Branding.\
After completing phase 1, I moved right onto phase 2.
## 1/6/2026
I’ve finally done learning phase 2 at nearly 4 pm again (wow).\
Topics in this phase were: boot process, systemd, desktop customization, display servers, driver, repositories, packages, ISO building, Git, and Networking.\
Then, I moved to phase 3. Currently, I completed learning about fundamentals of Bash scripting and practical Linux automation.
## 2/6/2025
I finally done phase 3 at just 9:30 am, much earlier than phase 1 and 2. I also made a design blueprint for Rewind OS as Nova told me to do. Now, I can read the Bash scripts easily, they are much easier than I expected.\
To start phase 4, I need to install a few things. First, I created a separate directory on GitHub for Rewind OS. Then, I connected Git on my laptop to my GitHub account. After that, I created separate directories inside to categorize my files and documents. I tried the first Git commands, it worked.\
Then, I installed Oracle VirtualBox to make a virtual machine. I decided to install Fedora on it because I planned to make Rewind OS based on Fedora too. Everything went smoothly! After the Fedora virtual machine was installed, I went installing Developer Tools, Git, and XFCE on it. I also installed Brave to replace Firefox.
## 03/6/2026
I'm ready for phase 4. Before I really start, I identified target users and apps one more time.\
**Student:** LibreOffice apps, Spotify, OBS Studio.\
**Casual Gamer:** ProtonPlus, Steam, RetroArch, Lutris, OBS Studio.\
**Hobbyist:** Arduino, VS Code, PyCharm, FreeCAD.\
**Linux beginner:** LibreOffice apps, Steam, ProtonPlus, RetroArch, Spotify.\
**Creator:** GIMP, Krita, Inkscape, Blender, Kdenlive, OBS Studio.\
All profiles have browser: Brave/Chrome/FireFox.
### Phase 4 Milestone:
Created and tested the first working Rewind OS script: Scripts/install/install-packages.sh\
The script reads package names from a text file and installs them automatically using DNF. Learned:
- Bash variables
- Executable permission
- Package installation automation
- Github token authentication

Wrote and tested the profile installation script sucessfully: Scripts/install/install-profile.sh\
The script reads profile name inputted in the terminal, finds and installs packages based on that profile and also install essentials package. Instead of having to code the command sudo dnf install over and over again, I used the install-package script that I wrote to directly install the packages.
## 04/6/2026
This morning, I wrote the script to show profile menu: /Scripts/setup/profile-menu.sh\
Its job is to ask what type the user is (student, gamer, hobbyist, creator, Linux beginner). Then, after the user typed in their choice, it will automatically installs essential pack and the chosen profile pack. I tested with the Creator pack and it worked good, even I did have to fix a few things about file paths inside the scripts.\
At noon, I wrote the first prototype of Rewind Welcome app and Kineat Base, made some documentation files to put in Kineat. I was able to connect them together that the user can access Kineat from the Welcome menu too.\
I created the first prototype of Rewind Settings: Scripts/rewind-apps/rewind-settings.sh:
- The settings now has a simple menu with a few options to customize the system
- A "About" section which shows full detailed information of the system
- Rewind Settings now has the first working feature: change background image
## 05/6/2026
This morning, I've successfully wrote a function in Rewind Settings which allows the user to change default web browser. It shows a list of installed browsers, the user input by number and the browser will be default by their choice. Additionally, I also modified the structure of the program. Now, the menu and sub-menu systems in Rewind Settings will allow user to do decisions or return to parent menu if they wanted to, because everything is put inside while loops now.