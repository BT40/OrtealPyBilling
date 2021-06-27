import sys
import gi

from submods import functions
from submods import guicommon
from submods import guiprocessor

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk



def reload_screen(somesignal, mainwindow, guiinvoicingins) :     
        children=mainwindow.invoicingbox.get_children()
        for eachchild in children:
            mainwindow.invoicingbox.remove(eachchild)
            eachchild.destroy()        
        guicommon.loadguicommon()
        mainwindow.bph=guiinvoicingins.generatepage(mainwindow, guiinvoicingins)
        mainwindow.invoicingbox.add(mainwindow.bph)
        mainwindow.invoicingbox.show_all()  
        print('successfully reloaded sucreen, reporting from newsalesub line 24')      
       
