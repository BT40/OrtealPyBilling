import sys
import gi
from submods import b4gui
import guiinvoicing
import guiinventory
import guicompany
import guipayments
import guimore
import time
import importlib.resources

from os.path import dirname

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class MainWindow(Gtk.ApplicationWindow):

    def __init__(self, applic): #applic is application instance
        super(MainWindow, self).__init__(title="Orteal Billing", application=applic, name="ortealbilling")        
        
        #self.set_default_size(280, 180)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(10)
        
        projectdirectory=dirname(dirname(__file__))   #directory path fetching, if reqd, can used for data storage
        
        b4guiins=b4gui.Startt()
        b4guiins.some_initialisations(projectdirectory)    
        guiinvoicingins=guiinvoicing.GtkInvoicing()
        guiinventoryins=guiinventory.GtkInventory()
        guicompanyins=guicompany.GtkCompany() 
        guipaymentsins=guipayments.GtkPayments()
        guimoreins=guimore.GtkMore()       
        
        mainbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        self.add(mainbox)

        leftvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        mainbox.add(leftvbox)
        
        rightvbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        mainbox.add(rightvbox)        

        stack = Gtk.Stack()
        stack.set_hexpand(True)
        stack.set_vexpand(True)
        rightvbox.pack_start(stack, True, True, 0)
        
        stacksidebar = Gtk.StackSidebar()
        stacksidebar.set_stack(stack)
        leftvbox.pack_start(stacksidebar, True, True, 0)
        
        self.invoicingbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.bph=guiinvoicingins.generatepage(self, guiinvoicingins)
        self.invoicingbox.add(self.bph)
        stack.add_titled(self.invoicingbox, "billboxmain", "Invoicing") 
        
        paymentsbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        abph=guipaymentsins.generatepage(self)
        paymentsbox.add(abph)
        stack.add_titled(paymentsbox, "paymentsmain", "Payments")
        self.paymentsbox=paymentsbox #For code compatibility, do ot remove else bugs will be introduced
        self.guipaymentsins=guipaymentsins #For code compatibility, do ot remove else bugs will be introduced
           
        inventorybox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        iph=guiinventoryins.generatepage(self.invoicingbox, self.bph, guiinvoicingins, self) #iph=inventory page holder
        inventorybox.add(iph)
        stack.add_titled(inventorybox, "inventorymain", "Items")
        #print("Inventory box loaded, now trying loading Create box")        
        
        companybox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)        
        cph=guicompanyins.generatepage(self.invoicingbox, self.bph, guiinvoicingins, self, guipaymentsins) # company page holder
        companybox.add(cph)
        stack.add_titled(companybox, "companyboxmain", "Company")        
       
        #reportsbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        #stack.add_titled(reportsbox, "reportsboxmain", "Reports")              
        
        morebox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        mph=guimoreins.generatepage(applic, self.invoicingbox, self.bph, guiinvoicingins, companybox, cph, guicompanyins, self) #mph=more page holder
        morebox.add(mph)
        stack.add_titled(morebox, "moremain", "More")
        
        style_provider = Gtk.CssProvider()      
        
        try:   #for normal running from source code
            style_provider.load_from_path("submods/styl.css")            
        except: #for zipapps, they cant read normal file in project directory
            csscontent=importlib.resources.read_binary('submods', 'styl.css')            
            style_provider.load_from_data(csscontent)   
            
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(), style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
              
        #print("GUI creating done, reporting from main window")        
