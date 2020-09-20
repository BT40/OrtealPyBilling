import sys
import guimainwin
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gio
from gi.repository import Gtk
from gi.repository import Gdk


class App(Gtk.Application):
    def __init__(self):
        Gtk.Application.__init__(self,
                                 application_id="com.githubbt40.orpybill",
                                 flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        window = guimainwin.MainWindow(self)
        window.show_all()
        window.maximize()


if __name__ == '__main__':
    
    app = App()
    app.run(sys.argv)
