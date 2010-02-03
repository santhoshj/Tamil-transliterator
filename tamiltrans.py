#!/usr/bin/env python

import sys
try:
  import pygtk
  pygtk.require("2.0")
except:
  pass
try:
  import gtk
  import gtk.glade
except:
  sys.exit(1)

from util import *
from compl import CompletedEntry


class tamilTrans:
  def __init__(self):
    #Set the Glade file
    self.gladefile = "gui.glade"  
    self.wTree = gtk.glade.XML(self.gladefile) 
    self.window = self.wTree.get_widget("mainWindow")
    
    self.text = CompletedEntry()
    self.text.set_property("can-focus", "True")
    
    self.text.connect("changed",self.on_changed)
    self.hbox = self.wTree.get_widget("hbox2")
    self.hbox.add(self.text)
#    self.vbox.reorder_child(self.text, 1)
    self.text.grab_focus()
    #print (self.vbox)

    self.window.show_all()
    self.textview = self.wTree.get_widget("display")
    self.textbuffer = self.textview.get_buffer()

    dic = { "on_clicked" : self.on_clicked,
            "on_changed" : self.on_changed,
            "on_about" : self.on_about,
            "on_clear" : self.on_clear,
            "on_copy" : self.on_copy,
	    "on_mainWindow_destroy" : gtk.main_quit }

    self.wTree.signal_autoconnect(dic)

  
  def on_clear(self, widget):
    self.text.set_text("")
  #  self.on_changed(self.text)

  def on_copy(self, widget):
    clip = gtk.Clipboard()
    clip.set_text(self.tam_text)

  def on_about(self, widget):
    from aboutdialog import AboutDialog
    AboutDialog().run()


  def on_changed(self, widget):
    self.tam_text = u""
    self.prevVow = ""
    en_text = widget.get_text()

    tam = Tamilify(en_text)
    tam_text = tam.run()
  #  for letter in en_text:
  #    self.tamil(letter)
    
    self.textbuffer.set_text(tam_text)
  
  def on_clicked(self, widget):
    gtk.main_quit()



class Tamilify:
  def __init__(self, en_text):
    self.keymap = {}
    self.prevVow = str()
    self.fillkeymap()
    self.en_text = en_text
    self.tam_text = unicode()

  def fillkeymap(self):
    keymap = self.keymap
    keymap['Q'] = keymap['q'] = u"\u0B83"
    keymap['a'] = u"\u0B85"
    keymap['A'] = keymap['aa'] = u"\u0B86"
    keymap['i'] = u"\u0B87"
    keymap['I'] = keymap['ee'] = u"\u0B88"
    keymap['u'] = u"\u0B89"
    keymap['U'] = keymap['oo'] = u"\u0B8A"
    keymap['e'] = u"\u0B8E"
    keymap['E'] = keymap['ae'] = u"\u0B8F"
    keymap['Y'] = keymap['ai'] = u"\u0B90"
    keymap['o'] = u"\u0B92"
    keymap['O'] = keymap['oa'] = u"\u0B93"
    keymap['W'] = keymap['au'] = keymap['w'] = u"\u0B94" 
    
    keymap['k'] = keymap['K'] = u"\u0B95\u0BCD"
    keymap['c'] = keymap['C'] = u"\u0B95\u0BCD"
    keymap['g'] = keymap['G'] = u"\u0B95\u0BCD"
    keymap['ng'] = keymap['NG'] = u"\u0B99\u0BCD"
    keymap['ch'] = keymap['Ch'] = u"\u0B9A\u0BCD"
    keymap['j'] = keymap['J'] = u"\u0B9C\u0BCD"
    keymap['f'] = keymap['F'] = u"\u0BAA\u0BCD"
    keymap['ny'] = keymap['Ny'] = u"\u0B9E\u0BCD"
    keymap['nj'] = keymap['Nj'] = u"\u0B9E\u0BCD\u0B9A\u0BCD"
    keymap['th'] = keymap['Th'] = keymap['dh'] = keymap['Dh'] = u"\u0BA4\u0BCD"
    keymap['N'] = u"\u0BA3\u0BCD"
    keymap['d'] = keymap['D'] = u"\u0B9F\u0BCD"
    keymap['t'] = keymap['T'] = u"\u0B9F\u0BCD"
    keymap['n'] = u"\u0BA9\u0BCD"
    keymap['x'] = keymap['X'] = u"\u0BA8\u0BCD"
    keymap['p'] = keymap['P'] = keymap['b'] = keymap['B'] = u"\u0BAA\u0BCD"
    keymap['m'] = keymap['M'] = u"\u0BAE\u0BCD"
    keymap['y'] = u"\u0BAF\u0BCD"
    keymap['r'] = u"\u0BB0\u0BCD"
    keymap['R'] = u"\u0BB1\u0BCD"
    keymap['l'] = u"\u0BB2\u0BCD"
    keymap['L'] = u"\u0BB3\u0BCD"
    keymap['z'] = keymap['Z'] = u"\u0BB4\u0BCD"
    keymap['v'] = keymap['V'] = u"\u0BB5\u0BCD"
    keymap['sh'] = keymap['Sh'] = u"\u0BB7\u0BCD"
    keymap['s'] =  u"\u0B9A\u0BCD"
    keymap['S'] = u"\u0BB8\u0BCD"
    keymap['h'] = keymap['H'] = u"\u0BB9\u0BCD"

  
  def insertFrom(self, text, amt):
    #print text
    length = len(self.tam_text)
    if not (length-amt-1) < 0:
      left = self.tam_text[:(length-amt)]
    else:
      left = ""
    if not amt == 0:
      right = self.tam_text[(length-amt):]
    else:
      right = ""
    self.tam_text = left + text #+ right
      
  def tamil(self, key):
    #print "%s + %s" % (self.prevVow,key)
    keymap = self.keymap
    if key == " " or key == "\n":
      self.tam_text += key;

    if keymap.has_key(key):
      res = keymap[key]
    else:
      return True

    if keymap.has_key(self.prevVow+key):
      combined = keymap[self.prevVow+key]
    else:
      combined = None

    if not len(self.tam_text) == 0:
      prevUni = self.tam_text[-1]
    else:
      prevUni = unicode()

    
    if valid(self.prevVow) and  (combined != None):
      if prevUni == u"\u0BCD":
        self.insertFrom(combined, 2)
      elif mei(prevUni):
        self.insertFrom(convertuyirmei(combined), 0)
      elif uyirmei(prevUni):
        self.insertFrom(convertuyirmei(combined), 1)
      else: 
        self.insertFrom(combined, 1)
      self.prevVow = ""
      return False
  
    if uyir(res):
      if mei(prevUni):
        self.insertFrom(convertuyirmei(res), 0)
      elif prevUni == u"\u0BCD":
        self.insertFrom(convertuyirmei(res), 1)
      else:
        self.insertFrom(res, 0)
    else:
      self.insertFrom(res, 0)
    
    self.prevVow = key
    return False

  def run(self):
    for letter in self.en_text:
      self.tamil(letter)
    
    return self.tam_text
  

if __name__ == "__main__":
  t = tamilTrans()
  gtk.main()
