
import wx
import wx.xrc

from loginScreen import loginScreen

def main():
	app = wx.App()
	loginScreen(None).Show()
	
	app.MainLoop()
	
if __name__ == "__main__":
	main()
