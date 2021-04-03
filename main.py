from tkinter import *
from PIL import ImageGrab
import time

class Shot(Tk):
	def __init__(self):
		super().__init__()
		self.overrideredirect(False)
		self.wm_attributes('-alpha', 0.5)
		# self.wm_attributes('-transparent', True)
		# root.config(bg = 'systemTransparent')
		self.snap = Button(self, text = "Screenshot", command = self.screenshot)
		self.snap.pack()

	def screenshot(self):
		self.snap.pack_forget()
		self.attributes('-fullscreen', True)
		x = self.winfo_rootx()
		y = self.winfo_rooty()
		time.sleep(2)
		x1 = x +self.winfo_width()
		y1 = y+self.winfo_height()
		ImageGrab.grab().crop((x, y, x1, y1, )).save('screenshot.jpg')
		self.destroy()

if __name__=='__main__':
	Shot().mainloop()
