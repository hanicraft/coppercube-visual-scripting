
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
import tkinter.font



class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#666666')
            self.w1.geometry('710x580')
            self.w1.title("CopperCube Visual Scripting By hanicraft")
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#666666')
            self.w1.place(x = 0, y = 0, width = 710, height = 580)
        self.label1 = Label(self.w1, text = "   Version 0.1 By HaniCraft", fg = "#2f2f2f", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label1.place(x = 0, y = 550, width = 130, height = 32)
        self.output = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.output.place(x = 10, y = 10, width = 390, height = 370)
        self.set_varible = Button(self.w1, text = "set varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.set_varible.place(x = 420, y = 50, width = 140, height = 22)
        self.set_varible['command'] = self.setvar
        self.button1_copy = Button(self.w1, text = "set varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button1_copy.place(x = 1990, y = 360, width = 140, height = 22)
        self.get_varible = Button(self.w1, text = "get varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.get_varible.place(x = 420, y = 80, width = 140, height = 22)
        self.get_varible['command'] = self.getvar
        self.onkeydown = Button(self.w1, text = "on keydown", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeydown.place(x = 60, y = 420, width = 140, height = 22)
        self.onkeydown['command'] = self.keydown
        self.label2 = Label(self.w1, text = "Events", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 60, y = 390, width = 90, height = 22)
        self.onkeyup = Button(self.w1, text = "on keyup", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeyup.place(x = 60, y = 450, width = 140, height = 22)
        self.onkeyup['command'] = self.keyup
        self.onmousedown = Button(self.w1, text = "on mouse down", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmousedown.place(x = 60, y = 480, width = 140, height = 22)
        self.onmousedown['command'] = self.mousedown
        self.onmouseup = Button(self.w1, text = "on mouse up", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmouseup.place(x = 60, y = 510, width = 140, height = 22)
        self.onmouseup['command'] = self.mouseup
        self.label3 = Label(self.w1, text = "scene nodes", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 260, y = 390, width = 90, height = 22)
        self.button7 = Button(self.w1, text = "clone node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button7.place(x = 260, y = 420, width = 120, height = 22)
        self.button8 = Button(self.w1, text = "remove node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button8.place(x = 260, y = 450, width = 120, height = 22)
        self.label4 = Label(self.w1, text = "various", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label4.place(x = 420, y = 20, width = 90, height = 22)
        self.label5 = Label(self.w1, text = "camera", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label5.place(x = 260, y = 480, width = 90, height = 22)
        self.button9 = Button(self.w1, text = "set active camera", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button9.place(x = 260, y = 510, width = 120, height = 22)
        self.button10 = Button(self.w1, text = "get active camera", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button10.place(x = 260, y = 540, width = 120, height = 22)
        self.switch_scene = Button(self.w1, text = "switch scene", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.switch_scene.place(x = 420, y = 110, width = 140, height = 22)
        self.switch_scene['command'] = self.scene_switch
        self.button12 = Button(self.w1, text = "get current node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button12.place(x = 390, y = 420, width = 120, height = 22)

    def setvar(self):
        self.output.insert('1.0', "ccbSetCopperCubeVariable(varible name, value of varible)")

    def getvar(self):
        self.output.insert('1.0', "ccbGetCopperCubeVariable(varible name)")

    def scene_switch(self):
        self.output.insert('1.0', "ccbSwitchToScene(sceneName)")

    def keydown(self):
        self.output.insert('1.0', "ccbRegisterKeyDownEvent(keyPressedDown); function keyPressedDown(keyCode) {    print(A key was pressed down: + keyCode);}")

    def keyup(self):
        self.output.insert('1.0', "ccbRegisterKeyUpEvent(keyPressedUp); function keyPressedUp(keyCode) {  print(A key was left up: + keyCode);}")

    def mousedown(self):
        self.output.insert('1.0', "ccbRegisterMouseDownEvent(mousePressedDown); function mousePressedDown(button){   print(A mouse button was presssed down: + button);}")

    def mouseup(self):
        self.onmouseup.insert('1.0', "ccbRegisterMouseUpEvent(mousePressedUp); function mousePressedUp(button){   print(A mouse button was presssed up: + button);}")

    def clonenode(self):
        print('clonenode')

    def removenode(self):
        print('removenode')

    def getcurrentnode(self):
        print('getcurrentnode')

    def setcamera(self):
        print('setcamera')

    def getcamera(self):
        print('getcamera')

if __name__ == '__main__':
    a = Widget1(0)
    a.w1.mainloop()

class Widget1():
    def __init__(self, parent):
        self.gui(parent)

    def gui(self, parent):
        if parent == 0:
            self.w1 = Tk()
            self.w1.configure(bg = '#666666')
            self.w1.geometry('710x580')
            self.w1.title("CopperCube Visual Scripting By hanicraft")
        else:
            self.w1 = Frame(parent)
            self.w1.configure(bg = '#666666')
            self.w1.place(x = 0, y = 0, width = 710, height = 580)
        self.label1 = Label(self.w1, text = "   Version 0.1 By HaniCraft", fg = "#2f2f2f", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label1.place(x = 0, y = 550, width = 130, height = 32)
        self.output = Text(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.output.place(x = 10, y = 10, width = 390, height = 370)
        self.set_varible = Button(self.w1, text = "set varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.set_varible.place(x = 420, y = 50, width = 140, height = 22)
        self.button1_copy = Button(self.w1, text = "set varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button1_copy.place(x = 1990, y = 360, width = 140, height = 22)
        self.get_varible = Button(self.w1, text = "get varible", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.get_varible.place(x = 420, y = 80, width = 140, height = 22)
        self.onkeydown = Button(self.w1, text = "on keydown", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeydown.place(x = 60, y = 420, width = 140, height = 22)
        self.label2 = Label(self.w1, text = "Events", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 60, y = 390, width = 90, height = 22)
        self.onkeyup = Button(self.w1, text = "on keyup", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeyup.place(x = 60, y = 450, width = 140, height = 22)
        self.onmousedown = Button(self.w1, text = "on mouse down", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmousedown.place(x = 60, y = 480, width = 140, height = 22)
        self.onmouseup = Button(self.w1, text = "on mouse up", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmouseup.place(x = 60, y = 510, width = 140, height = 22)
        self.label3 = Label(self.w1, text = "scene nodes", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 260, y = 390, width = 90, height = 22)
        self.button7 = Button(self.w1, text = "clone node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button7.place(x = 260, y = 420, width = 120, height = 22)
        self.button8 = Button(self.w1, text = "remove node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button8.place(x = 260, y = 450, width = 120, height = 22)
        self.label4 = Label(self.w1, text = "various", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label4.place(x = 420, y = 20, width = 90, height = 22)
        self.label5 = Label(self.w1, text = "camera", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label5.place(x = 260, y = 480, width = 90, height = 22)
        self.button9 = Button(self.w1, text = "set active camera", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button9.place(x = 260, y = 510, width = 120, height = 22)
        self.button10 = Button(self.w1, text = "get active camera", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button10.place(x = 260, y = 540, width = 120, height = 22)
        self.switch_scene = Button(self.w1, text = "switch scene", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.switch_scene.place(x = 420, y = 110, width = 140, height = 22)
        self.button12 = Button(self.w1, text = "get current node", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button12.place(x = 390, y = 420, width = 120, height = 22)

        
    def setvar(self):
        self.set_varible.insert('1.0', "ccbSetCopperCubeVariable(varible name, value of varible)")

    def getvar(self):
        self.get_varible.insert('1.0', "ccbGetCopperCubeVariable(varible name)")
    
    def scene_switch(self):
        self.switch_scene.insert('1.0', "ccbSwitchToScene(sceneName)")

    def keydown(self):
        self.onkeydown.insert('1.0', "ccbRegisterKeyDownEvent(keyPressedDown); function keyPressedDown(keyCode) {    print(A key was pressed down: + keyCode);}")

    def keyup(self):
        insert('1.0', "ccbRegisterKeyUpEvent(keyPressedUp); function keyPressedUp(keyCode) {  print(A key was left up: + keyCode);}")

    def mousedown(self):
        insert('1.0', "ccbRegisterMouseDownEvent(mousePressedDown); function mousePressedDown(button){   print(A mouse button was presssed down: + button);}")

    def mouseup(self):
        insert('1.0', "ccbRegisterMouseUpEvent(mousePressedUp); function mousePressedUp(button){   print(A mouse button was presssed up: + button);}")