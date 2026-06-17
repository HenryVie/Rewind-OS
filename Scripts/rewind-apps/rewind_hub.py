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
    # Initialization
    def __init__(self, hub):
        super().__init__(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=10
        )

        self.hub = hub

        # Widgets
        title = Gtk.Label(
            label = "SETTINGS"
        )

        aboutButton = Gtk.Button(
            label = "About"
        )

        personalizeButton = Gtk.Button(
            label = "Personalization"
        )

        taskbarButton = Gtk.Button(
            label = "Taskbar"
        )

        applicationButton = Gtk.Button(
            label = "Applications"
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
        self.set_valign(
            Gtk.Align.CENTER
        )

        self.set_margin_top(30)
        self.set_margin_bottom(30)
        self.set_margin_start(20)
        self.set_margin_end(20)

        self.append(title)
        self.append(aboutButton)
        self.append(personalizeButton)
        self.append(taskbarButton)
        self.append(applicationButton)
        self.append(returnButton)

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
            label = "Defined User Profils"
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
        self.append(returnButton)

    def on_return_clicked(self, button):
        self.hub.go_main()

class RewindApp(Gtk.Application):
    def __init__(self):
        super().__init__()

    def do_activate(self):
        window = RewindHub(self)
        window.present()

app = RewindApp()
app.run()