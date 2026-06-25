import subprocess
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

class RewindHub(Gtk.ApplicationWindow):
    # Initialization
    def __init__(self, app):
        super().__init__(application=app)

        self.set_title("Rewind Hub")
        self.set_default_size(600, 400)

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.stack = Gtk.Stack()

        self.stack.add_named(
            MainPage(self),
            "main"
        )

        self.stack.add_named(
            SettingsPage(self),
            "settings"
        )

        self.stack.add_named(
            TechnicianPage(self),
            "technician"
        )
        self.stack.add_named(
            TechnicianSysInfo(self),
            "sysinfo"
        )
        self.stack.add_named(
            TechnicianInternetStat(self),
            "internetstat"
        )
        self.stack.add_named(
            TechnicianDiskSpace(self),
            "diskspace"
        )
        self.stack.add_named(
            TechnicianMemory(self),
            "memoryusage"
        )
        self.stack.add_named(
            TechnicianUpdate(self),
            "updatechecker"
        )
        self.stack.add_named(
            TechnicianCache(self),
            "refreshcache"
        )

        self.stack.add_named(
            KineatPage(self),
            "kineat"
        )
        self.stack.add_named(
            KineatAbout(self),
            "aboutrewind"
        )
        self.stack.add_named(
            KineatProfiles(self),
            "profiles"
        )
        self.stack.add_named(
            KineatBasics(self),
            "basics"
        )
        self.stack.add_named(
            KineatApps(self),
            "apps"
        )

        self.set_child(self.stack)

        # Stack Pages
    def go_main(self):
        self.stack.set_visible_child_name("main")

    def go_settings(self):
        self.stack.set_visible_child_name("settings")

    def go_technician(self):
        self.stack.set_visible_child_name("technician")
    def go_sysinfo(self):
        self.stack.set_visible_child_name("sysinfo")
    def go_internetstat(self):
        self.stack.set_visible_child_name("internetstat")
    def go_diskspace(self):
        self.stack.set_visible_child_name("diskspace")
    def go_memoryusage(self):
        self.stack.set_visible_child_name("memoryusage")
    def go_updatechecker(self):
        self.stack.set_visible_child_name("updatechecker")
    def go_refreshcache(self):
        self.stack.set_visible_child_name("refreshcache")
    

    def go_kineat(self):
        self.stack.set_visible_child_name("kineat")
    def go_kineatabout(self):
        self.stack.set_visible_child_name("aboutrewind")
    def go_profiles(self):
        self.stack.set_visible_child_name("profiles")
    def go_basics(self):
        self.stack.set_visible_child_name("basics")
    def go_apps(self):
        self.stack.set_visible_child_name("apps")

    # Event Functions
    def on_exit_clicked(self, button):
        self.close()

class MainPage(Gtk.Box):

    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label="Welcome to Rewind OS!"
        )

        settingsButton = Gtk.Button(
            label="Settings"
        )

        technicianButton = Gtk.Button(
            label="Technician"
        )

        kineatButton = Gtk.Button(
            label="Kineat Base"
        )

        exitButton = Gtk.Button(
            label="Exit"
        )

        # Events
        settingsButton.connect(
            "clicked",
            self.on_settings_clicked
        )

        technicianButton.connect(
            "clicked",
            self.on_technician_clicked
        )

        kineatButton.connect(
            "clicked",
            self.on_kineat_clicked
        )

        exitButton.connect(
            "clicked",
            self.on_exit_clicked
        )

        # Layout
        self.set_valign(Gtk.Align.CENTER)

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.append(title)
        self.append(settingsButton)
        self.append(technicianButton)
        self.append(kineatButton)
        self.append(exitButton)

    def on_settings_clicked(self, button):
        self.hub.go_settings()

    def on_technician_clicked(self, button):
        self.hub.go_technician()

    def on_kineat_clicked(self, button):
        self.hub.go_kineat()

    def on_exit_clicked(self, button):
        self.hub.close()

class SettingsPage(Gtk.Box):
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Main containers
        self.contentBox = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL,
            spacing=10
        )

        self.sidebar = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=5
        )

        self.stack = Gtk.Stack()

        # Build UI
        self.create_widgets()
        self.create_pages()
        self.connect_signals()
        self.build_layout()

    # =========================
    # Widget Creation
    # =========================

    def create_widgets(self):
        self.title = Gtk.Label(
            label="SETTINGS"
        )

        self.aboutButton = Gtk.Button(
            label="About"
        )

        self.personalizeButton = Gtk.Button(
            label="Personalization"
        )

        self.applicationButton = Gtk.Button(
            label="Applications"
        )

        self.returnButton = Gtk.Button(
            label="Return"
        )

    # =========================
    # Page Creation
    # =========================

    def create_pages(self):
        self.aboutPage = self.build_about_page()
        self.personalizePage = self.build_personalization_page()
        self.applicationPage = self.build_application_page()

    def build_about_page(self):
        page = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        aboutContent = Gtk.Label(
                label = """
About Rewind OS

Version: P1
Developer: Nguyen Dinh Nam
Base: Fedora 44 XFCE

A lightweight Linux distro focused on helping users understand, maintain and customize their computer.
"""
        )

        aboutContent.set_wrap(True)
        aboutContent.set_xalign(0)

        page.append(aboutContent)

        return page

    def build_personalization_page(self):
        page = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        page.append(
            Gtk.Label(label="Personalization")
        )

        return page

    def build_application_page(self):
        page = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        browserList = Gtk.StringList.new(["Firefox", "Brave", "Chromium"])
        browserDropdown = Gtk.DropDown(
            model=browserList
        )

        browserDropdown.connect(
            "notify::selected",
            self.on_browser_changed
        )

        page.append(Gtk.Label(label="Rewind Applications"))
        page.append(Gtk.Label(label="Default Browser"))
        page.append(browserDropdown)

        return page

    # =========================
    # Signals
    # =========================

    def connect_signals(self):
        self.aboutButton.connect("clicked", self.show_about)
        self.personalizeButton.connect("clicked", self.show_personalization)
        self.applicationButton.connect("clicked", self.show_applications)
        self.returnButton.connect("clicked", self.on_return_clicked)

    def on_browser_changed(self, dropdown, pspec):
        selected = dropdown.get_selected_item()
        browser = selected.get_string()

        browserMap = {
            "Firefox": "org.mozilla.firefox.desktop",
            "Brave": "com.brave.Browser.desktop",
            "Chromium": "chromium-browser.desktop"
        }

        desktopFile = browserMap.get(browser)
        
        subprocess.run(["xdg-settings", "set", "default-web-browser", desktopFile])

    # =========================
    # Layout
    # =========================

    def build_layout(self):
        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.stack.set_hexpand(True)
        self.stack.set_vexpand(True)

        self.append(self.title)
        self.append(self.contentBox)

        self.sidebar.append(self.aboutButton)
        self.sidebar.append(self.personalizeButton)
        self.sidebar.append(self.applicationButton)
        self.sidebar.append(self.returnButton)

        self.contentBox.append(self.sidebar)
        self.contentBox.append(self.stack)

        self.stack.add_named(self.aboutPage, "about")
        self.stack.add_named(self.personalizePage, "personalization")
        self.stack.add_named(self.applicationPage, "applications")

        self.stack.set_visible_child_name("about")

    # =========================
    # Navigation
    # =========================

    def show_about(self, button):
        self.stack.set_visible_child_name("about")

    def show_personalization(self, button):
        self.stack.set_visible_child_name("personalization")

    def show_applications(self, button):
        self.stack.set_visible_child_name("applications")

    # =========================
    # Events
    # =========================

    def on_return_clicked(self, button):
        self.hub.go_main()

class TechnicianPage(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "TECHNICIAN"
        )

        systeminfoButton = Gtk.Button(
            label = "System Information"
        )

        internetstatButton = Gtk.Button(
            label = "Check Internet Status"
        )

        diskspaceButton = Gtk.Button(
            label = "Disk Space"
        )

        memoryusageButton = Gtk.Button(
            label = "Memory Usage"
        )

        updatecheckButton = Gtk.Button(
            label = "Check for Updates"
        )

        refreshcacheButton = Gtk.Button(
            label = "Refresh Package Cache"
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        systeminfoButton.connect(
            "clicked",
            self.on_systeminfo_clicked
        )

        internetstatButton.connect(
            "clicked",
            self.on_internetstat_clicked
        )

        diskspaceButton.connect(
            "clicked",
            self.on_diskspace_clicked
        )

        memoryusageButton.connect(
            "clicked",
            self.on_memory_clicked
        )

        updatecheckButton.connect(
            "clicked",
            self.on_update_clicked
        )

        refreshcacheButton.connect(
            "clicked",
            self.on_cache_clicked
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.set_valign(
            Gtk.Align.CENTER
        )

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.append(title)
        self.append(systeminfoButton)
        self.append(internetstatButton)
        self.append(diskspaceButton)
        self.append(memoryusageButton)
        self.append(updatecheckButton)
        self.append(refreshcacheButton)
        self.append(returnButton)

    # Function Buttons
    def on_systeminfo_clicked(self, button):
        self.hub.go_sysinfo()

    def on_internetstat_clicked(self, button):
        self.hub.go_internetstat()

    def on_diskspace_clicked(self, button):
        self.hub.go_diskspace()
    
    def on_memory_clicked(self, button):
        self.hub.go_memoryusage()

    def on_update_clicked(self, button):
        self.hub.go_updatechecker()

    def on_cache_clicked(self, button):
        self.hub.go_refreshcache()

    def on_return_clicked(self, button):
        self.hub.go_main()

class TechnicianSysInfo(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "System Information"
        )

        info = Gtk.Label(
            label = self.showInfo()
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(info)
        self.append(returnButton)

    def showInfo(self):
        hostname = subprocess.check_output(
            ["hostname"],
            text = True
        ).strip()

        kernelVer = subprocess.check_output(
            ["uname", "-r"],
            text = True
        ).strip()

        with open("/etc/os-release") as file:
            for line in file:
                if line.startswith("PRETTY_NAME="):
                    distroName = line.split("=")[1].strip().replace('"', '')
                    break

        return (
            f"Distro: {distroName}\n"
            f"Kernel Version: {kernelVer}\n"
            f"Hostname: {hostname}"
        )
    
    def on_return_clicked(self, button):
        self.hub.go_technician()

class TechnicianInternetStat(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "Internet Status"
        )

        stat = Gtk.Label(
            label = self.internetStat()
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(stat)
        self.append(returnButton)

    def internetStat(self):
        result = subprocess.run(
            ["ping", "-c", "1", "8.8.8.8"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            return "Status: Internet Connected"
        else:
            return "Status: No Internet Connection"

    def on_return_clicked(self, button):
        self.hub.go_technician()

class TechnicianDiskSpace(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "Disk Space"
        )

        diskInfo = Gtk.Label(
            label = self.disk()
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(diskInfo)
        self.append(returnButton)

    def disk(self):
        output = subprocess.check_output(
            ["df", "-h", "/"],
            text=True
        )

        lines = output.splitlines()

        diskInfo = lines[1].split()

        used = diskInfo[2]
        available = diskInfo[3]
        percent = diskInfo[4]

        return (
            f"Used Space: {used}\n"
            f"Available Space: {available}\n"
            f"Usage: {percent}"
        )
    
    def on_return_clicked(self, button):
        self.hub.go_technician()

class TechnicianMemory(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "Memory Usage"
        )

        memoryInfo = Gtk.Label(
            label = self.usage()
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(memoryInfo)
        self.append(returnButton)

    def usage(self):
        output = subprocess.check_output(
            ["free", "-h"],
            text=True
        )

        lines = output.splitlines()

        memUsage = lines[1].split()

        total = memUsage[1]
        used = memUsage[2]
        available = memUsage[6]

        return (
            f"Total RAM: {total}\n"
            f"Used RAM: {used}\n"
            f"Available RAM: {available}"
        )

    def on_return_clicked(self, button):
        self.hub.go_technician()

class TechnicianUpdate(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "Technician Update Checker"
        )

        updateChecker = Gtk.Button(
            label = "Check for Update"
        )
        self.updateResult = Gtk.Label(
            label = "Click the Check for Update button to start checking for update"
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        updateChecker.connect(
            "clicked",
            self.on_update_clicked
        )
        
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )
        
        # Layout
        self.append(title)
        self.append(self.updateResult)
        self.append(updateChecker)
        self.append(returnButton)

    def on_update_clicked(self, button):
            self.updateResult.set_text(self.upDate())

    def upDate(self):
        result = subprocess.run(
            ["dnf", "check-update"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Your system is already up to date."

        elif result.returncode == 100:
            return "Update available."

        else:
            return "Unable to check for updates."
    
    def on_return_clicked(self, button):
        self.hub.go_technician()

class TechnicianCache(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.set_valign(
            Gtk.Align.CENTER
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "Refresh Cache"
        )

        self.cacheResult = Gtk.Label(
            label = "Status: Writing Cache"
        )

        refreshCache = Gtk.Button(
            label = "Click to refresh caches"
        )        

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        refreshCache.connect(
            "clicked",
            self.on_refresh_clicked
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(self.cacheResult)
        self.append(refreshCache)
        self.append(returnButton)

    # Function
    def on_refresh_clicked(self, button):
        self.cacheResult.set_text(
            self.reFresh()
        )

    def reFresh(self):
        result = subprocess.run(
            ["dnf", "makecache"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Status: Cache refreshed successfully!"
        else:
            return "Failed to refresh cache."

    def on_return_clicked(self, button):
        self.hub.go_technician()

class KineatPage(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "KINEAT BASE"
        )

        aboutdistroButton = Gtk.Button(
            label = "About Rewind OS"
        )

        profileButton = Gtk.Button(
            label = "User Profiles"
        )

        basicsButton = Gtk.Button(
            label = "Basic Linux Concepts"
        )

        appsButton = Gtk.Button(
            label = "Rewind Applications"
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        aboutdistroButton.connect(
            "clicked",
            self.on_about_clicked
        )

        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        profileButton.connect(
            "clicked",
            self.on_profiles_clicked
        )

        basicsButton.connect(
            "clicked",
            self.on_basics_clicked
        )

        appsButton.connect(
            "clicked",
            self.on_apps_clicked
        )

        # Layout
        self.set_valign(
            Gtk.Align.CENTER
        )

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)
        
        self.append(title)
        self.append(aboutdistroButton)
        self.append(profileButton)
        self.append(basicsButton)
        self.append(appsButton)
        self.append(returnButton)

    def on_about_clicked(self, button):
        self.hub.go_kineatabout()

    def on_profiles_clicked(self, button):
        self.hub.go_profiles()

    def on_basics_clicked(self, button):
        self.hub.go_basics()

    def on_apps_clicked(self, button):
        self.hub.go_apps()

    def on_return_clicked(self, button):
        self.hub.go_main()

class KineatAbout(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Widgets
        
        title = Gtk.Label(
            label = "About Rewind OS"
        )     

        content = Gtk.Label(
            label = """
Rewind OS is a Fedora-based Linux distribution designed to combine retro-inspired design with modern usability.
The goal of Rewind OS is to provide a friendly, educational, and customizable computing experience.
"""
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        self.append(title)
        self.append(content)
        self.append(returnButton)

        title.set_xalign(0)

        content.set_wrap(True)
        content.set_xalign(0)
        content.set_hexpand(True)

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

    def on_return_clicked(self, button):
        self.hub.go_kineat()

class KineatProfiles(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        scroll = Gtk.ScrolledWindow()

        contentBox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        # Widgets
        title = Gtk.Label(
            label = "User Profiles"
        )

        content = Gtk.Label(
            label = """
Student
Designed for studying, research, programming, and office work.

Recommended Applications:
• LibreOffice
• Brave Browser
• Okular
• GIMP



Gamer
Designed for gaming and entertainment.

Recommended Applications:
• Steam
• Lutris
• MangoHud
• Discord



Creator
Designed for content creation, graphic design, video editing, and streaming.

Recommended Applications:
• Brave Browser
• GIMP
• Krita
• Kdenlive
• OBS Studio



Hobbyist
A balanced profile for everyday computing and personal projects.

Recommended Applications:
• Brave Browser
• VLC
• LibreOffice
• GIMP



Beginner
A simple starting point for users new to Linux.

Recommended Applications:
• Brave Browser
• LibreOffice
• VLC
• Kineat Base
"""
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        contentBox.append(title)
        title.set_xalign(0)

        contentBox.append(content)
        content.set_wrap(True)
        content.set_xalign(0)

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        contentBox.append(returnButton)

        self.append(scroll)
        scroll.set_child(contentBox)
        scroll.set_vexpand(True)
        scroll.set_hexpand(True)

    def on_return_clicked(self, button):
        self.hub.go_kineat()

class KineatBasics(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub
        scroll = Gtk.ScrolledWindow()

        contentBox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        # Widgets
        title = Gtk.Label(
            label = "Basic Linux Concepts"
        )

        content  = Gtk.Label(
            label = """
Linux
Linux is an operating system, similar to Windows and macOS. But unlike Windows, Linux is open source and comes in many different distributions such as Fedora, Ubuntu, Mint, etc.
For an example, because it is open-sourced, I could take the base of Fedora and configured the system, which is how I made Rewind OS.

Distribution (Distro)
A Linux distribution combines the Linux kernel with softwares, desktop environments, and tools.

Examples:
• Fedora: known for providing relatively recent software and technologies while maintaining a good balance between stability and modern features.
• Debian: it is known for its stability and reliability.
• Ubuntu: Ubuntu is based on Debian. It shares the same stable element of Debian, and unlike Debian, Ubuntu's comes up with more modern softwares and features.
• Linux Mint: Mint is based on Ubuntu. It was known for being very simple to use. Mint's features and Windows-like interface make it a perfect option for users who moved from Windows and is new to Linux.
• Arch: Unlike the others, Arch is a very complex distribution to use. Traditionally, Arch provides a minimal installation process where users choose and configure most components themselves.

Each Linux distribution serves a different purpose for different group of user. Think of distributions like different flavors of the same operating system.
Rewind OS is focused on being simple and approachable so that anyone can use it without being afraid of breaking their system. It includes custom features designed to help users learn and use Linux more easily.

Terminal
The terminal allows users to interact with the system using text commands. Most everyday tasks can be completed through graphical applications, but the terminal provides additional power and flexibility that pre-made graphical apps may not be able to do.

Package
A package is a bundle of software that can be installed on the system.

Examples:
• Firefox
• VLC
• LibreOffice

Package managers install and update packages automatically.

Package Manager
A package manager can install, remove, update, and search for software.
DNF is Fedora's package manager. While on Debian, it is APT. On Arch, it is Pacman.

Examples commands:
• dnf install
• dnf remove
• dnf update

Because RewindOS is based on Fedora, it also uses DNF as the package manager.

sudo
Some system changes require elevated permissions. sudo allows a command to run with administrator privileges.

Example:
sudo dnf update

Open Source
Open source software makes its source code available for anyone to inspect, modify, and share. Many Linux distros and applications are open-sourced.

Desktop Environment
A desktop environment provides the graphical interface of the operating system.

Examples:
• GNOME: Uses a modern and simplified design that many users compare to macOS.
• KDE Plasma: Uses a traditional desktop layout that many users compare to Windows.
• XFCE: Uses a traditional desktop layout and focuses on speed, simplicity, and low resource usage.

Rewind OS uses XFCE so that the system is more lightweight.

Filesystem
A filesystem is how files and folders are organized on a computer. Unlike Windows, Linux does not use drive letters such as C: or D:. Instead, everything begins from a single root directory called "/".

Common locations:
• /home - User files
• /etc - System configuration
• /usr - Installed software
"""
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        contentBox.append(title)
        title.set_xalign(0)

        contentBox.append(content)
        content.set_wrap(True)
        content.set_xalign(0)

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        contentBox.append(returnButton)

        self.append(scroll)
        scroll.set_child(contentBox)

        scroll.set_vexpand(True)
        scroll.set_hexpand(True)

    def on_return_clicked(self, button):
        self.hub.go_kineat()

class KineatApps(Gtk.Box):
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        scroll = Gtk.ScrolledWindow()

        contentBox = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        # Widgets
        title = Gtk.Label(
            label = "Rewind Applications"
        )

        content = Gtk.Label(
            label = """
Rewind Hub
The starting point for new users. This app provide quick access to setup tasks, documentation, and Rewind OS tools.

Rewind Settings
Manage Rewind-specific settings and preferences. Provides a simple interface for configuring the system without using the terminal.

Rewind Technician
A collection of diagnostic and maintenance tools. Allows users to view system information and perform basic troubleshooting tasks without typing command lines in the terminal.

Kineat Base
The built-in knowledge base for Rewind OS. Provides explanations of Linux concepts, user profiles, and Rewind OS features.

Neato (Future)
An AI assistant designed to help users learn and use Rewind OS more effectively.
"""
        )

        returnButton = Gtk.Button(
            label = "Return"
        )

        # Event
        returnButton.connect(
            "clicked",
            self.on_return_clicked
        )

        # Layout
        contentBox.append(title)
        title.set_xalign(0)

        contentBox.append(content)
        content.set_wrap(True)
        content.set_xalign(0)

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        contentBox.append(returnButton)

        self.append(scroll)
        scroll.set_child(contentBox)

        scroll.set_vexpand(True)
        scroll.set_hexpand(True)

    def on_return_clicked(self, button):
        self.hub.go_kineat()

class RewindApp(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        window = RewindHub(self)
        window.present()

app = RewindApp()
app.run()