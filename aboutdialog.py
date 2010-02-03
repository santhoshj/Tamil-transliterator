# You may redistribute it and/or modify it under the terms of the
# GNU General Public License, as published by the Free Software
# Foundation; either version 3 of the License, or (at your option)
# any later version.
# 


import pygtk
pygtk.require('2.0')
import gtk
import pkg_resources

class AboutDialog:
    def __init__(self):
        # Get the glade file for the about dialog
        self.about = gtk.AboutDialog()
        self.about.set_position(gtk.WIN_POS_CENTER)
        self.about.set_name("Tamil Transliterator")
        self.about.set_program_name("Tamil Transliterator")

        self.about.set_copyright(u'Copyright \u00A9 2007-2008 Santhosh Kumar')
        self.about.set_comments("A simple tamil transliterator")
        self.about.set_version("1.0")
        self.about.set_authors(["Santhosh Kumar"])
        self.about.set_wrap_license(True)
        self.about.set_license(("This program is free software; you can redistribute \
it and/or modify it under the terms of the GNU General Public License as published by \
the Free Software Foundation; either version 3 of the License, or (at your option) any \
later version. This program is distributed in the hope that it will be useful, but \
WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS \
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. You \
should have received a copy of the GNU General Public License along with this program; \
if not, see <http://www.gnu.org/licenses>."))
        self.about.set_website("http://www.cse.iitm.ac.in/~santhuj")
        self.about.set_website_label("http://www.cse.iitm.ac.in/~santhuj")
     
           
    def run(self):
        self.about.show_all()
        self.about.run()
        self.about.destroy()
