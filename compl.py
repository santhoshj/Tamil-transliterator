#!/usr/bin/python

import gtk

COL_TEXT = 0

class CompletedEntry(gtk.Entry):
    def __init__(self):
        gtk.Entry.__init__(self)
        completion = gtk.EntryCompletion()
        completion.set_match_func(self.match_func)
        completion.connect("match-selected",
                           self.on_completion_match)
        completion.set_model(gtk.ListStore(str))
        completion.set_text_column(COL_TEXT)
        self.set_completion(completion)
        self.add_words(['abc', 'deff', 'degh','ghi', 'jkl', 'mno',
                      'pqr', 'stu', 'vwx', 'yz'])

    def match_func(self, completion, key, iter):
        model = completion.get_model()
        temp = self.get_text().split(' ')
        word = temp[len(temp)-1]
        return model[iter][COL_TEXT].startswith(word)
    
    def on_completion_match(self, completion, model, iter):
        temp = self.get_text().split(' ')
        words = temp[:-1]
        temp_w = ""
        for word in words:
            temp_w += word
            temp_w += " "
        new_text = temp_w + model[iter][COL_TEXT]
        print new_text
        self.set_text(new_text)
        self.set_position(-1)
	return True

    def add_words(self, words):
        model = self.get_completion().get_model()
        op = open("/home/santhosh/.pytam/history")
        words = op.readlines()
        
        for word in words:
            model.append([word])

if __name__ == "__main__":
    win = gtk.Window()
    win.connect('delete-event', gtk.main_quit)
    
    entry = CompletedEntry()
    entry.add_words(['abc', 'deff', 'degh','ghi', 'jkl', 'mno',
                      'pqr', 'stu', 'vwx', 'yz'])
    win.add(entry)
    win.show_all()
    
    gtk.main()
