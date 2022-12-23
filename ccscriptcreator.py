
from tkinter import *
from tkinter.ttk import Progressbar
from tkinter.ttk import Combobox
from tkinter.ttk import Notebook
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
from tkinter.filedialog import asksaveasfilename
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
        self.label1 = Label(self.w1, text = "   Version 0.6 By HaniCraft", fg = "#2f2f2f", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
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
        self.onkeydown = Button(self.w1, text = "on keydown", bg = "#005500", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeydown.place(x = 60, y = 420, width = 140, height = 22)
        self.onkeydown['command'] = self.keydown
        self.label2 = Label(self.w1, text = "Events", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label2.place(x = 60, y = 390, width = 90, height = 22)
        self.onkeyup = Button(self.w1, text = "on keyup", bg = "#005500", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onkeyup.place(x = 60, y = 450, width = 140, height = 22)
        self.onkeyup['command'] = self.keyup
        self.onmousedown = Button(self.w1, text = "on mouse down", bg = "#005500", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmousedown.place(x = 60, y = 480, width = 140, height = 22)
        self.onmousedown['command'] = self.mousedown
        self.onmouseup = Button(self.w1, text = "on mouse up", bg = "#005500", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.onmouseup.place(x = 60, y = 510, width = 140, height = 22)
        self.onmouseup['command'] = self.mouseup
        self.label3 = Label(self.w1, text = "scene nodes", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label3.place(x = 260, y = 390, width = 90, height = 22)
        self.button7 = Button(self.w1, text = "clone node", bg = "#00007f", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button7.place(x = 260, y = 420, width = 120, height = 22)
        self.button7['command'] = self.clonenode
        self.button8 = Button(self.w1, text = "remove node", bg = "#00007f", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button8.place(x = 260, y = 450, width = 120, height = 22)
        self.button8['command'] = self.removenode
        self.label4 = Label(self.w1, text = "various", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label4.place(x = 420, y = 20, width = 90, height = 22)
        self.label5 = Label(self.w1, text = "camera", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label5.place(x = 260, y = 480, width = 90, height = 22)
        self.button9 = Button(self.w1, text = "set active camera", bg = "#550000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button9.place(x = 260, y = 510, width = 120, height = 22)
        self.button9['command'] = self.setcamera
        self.button10 = Button(self.w1, text = "get active camera", bg = "#550000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button10.place(x = 260, y = 540, width = 120, height = 22)
        self.button10['command'] = self.getcamera
        self.switch_scene = Button(self.w1, text = "switch scene", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.switch_scene.place(x = 420, y = 110, width = 140, height = 22)
        self.switch_scene['command'] = self.scene_switch
        self.button12 = Button(self.w1, text = "get current node", bg = "#00007f", fg = "#ffffff", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button12.place(x = 390, y = 420, width = 120, height = 22)
        self.button12['command'] = self.getcurrentnode
        self.label6 = Label(self.w1, text = "remember to format your code", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label6.place(x = 550, y = 490, width = 150, height = 22)
        self.label7 = Label(self.w1, text = "before adding it to coppercube", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label7.place(x = 550, y = 470, width = 150, height = 22)
        self.button13 = Button(self.w1, text = "export action", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.button13.place(x = 610, y = 10, width = 90, height = 22)
        self.button13['command'] = self.save
        self.label8 = Label(self.w1, text = "remeber to add action_ to", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label8.place(x = 550, y = 510, width = 140, height = 22)
        self.label9 = Label(self.w1, text = "your file name so coppercube", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label9.place(x = 550, y = 530, width = 140, height = 22)
        self.label10 = Label(self.w1, text = "can reconize it", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label10.place(x = 550, y = 550, width = 90, height = 22)
        self.varname = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.varname.place(x = 570, y = 50, width = 130, height = 22)
        self.varname.insert(INSERT, "enter varible name")
        self.createfunction = Button(self.w1, text = "create function", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.createfunction.place(x = 420, y = 140, width = 140, height = 22)
        self.createfunction['command'] = self.func_create
        self.funcname = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.funcname.place(x = 570, y = 140, width = 130, height = 22)
        self.funcname.insert(INSERT, "enter function name")
        self.label11 = Label(self.w1, text = "scripted actions", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.label11.place(x = 420, y = 170, width = 90, height = 22)
        self.nodename = Entry(self.w1, font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.nodename.place(x = 390, y = 450, width = 120, height = 22)
        self.nodename.insert(INSERT, "enter node name")
        self.healthbar = Button(self.w1, text = "healthbar", bg = "#55ff7f", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.healthbar.place(x = 420, y = 200, width = 140, height = 22)
        self.healthbar['command'] = self.health_bar
        self.dolater = Button(self.w1, text = "do later", bg = "#55ff7f", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.dolater.place(x = 420, y = 230, width = 140, height = 22)
        self.dolater['command'] = self.do_later
        self.loadtexture = Button(self.w1, text = "load texture", bg = "#55ff7f", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.loadtexture.place(x = 570, y = 200, width = 130, height = 22)
        self.loadtexture['command'] = self.load_texture
        self.replace = Button(self.w1, text = "replace", bg = "#55ff7f", fg = "#000000", font = tkinter.font.Font(family = "MS Shell Dlg 2", size = 8), cursor = "arrow", state = "normal")
        self.replace.place(x = 570, y = 230, width = 130, height = 22)
        self.replace['command'] = self.replace_1

    def setvar(self):
        self.output.insert('1.0', "\n ccbSetCopperCubeVariable("+ self.varname.get() +", value of varible)")

    def getvar(self):
        self.output.insert('1.0', "\n ccbGetCopperCubeVariable("+ self.varname.get() +")")

    def scene_switch(self):
        self.output.insert('1.0', "\n ccbSwitchToScene(sceneName)")

    def keydown(self):
        self.output.insert('1.0', "\n ccbRegisterKeyDownEvent(keyPressedDown); \n function keyPressedDown(keyCode) \n {    \n print(A key was pressed down: + keyCode); \n }")

    def keyup(self):
        self.output.insert('1.0', "\n ccbRegisterKeyUpEvent(keyPressedUp); \n function keyPressedUp(keyCode) \n {  \n print(A key was left up: + keyCode); \n }")

    def mousedown(self):
        self.output.insert('1.0', "\n ccbRegisterMouseDownEvent(mousePressedDown);\n function mousePressedDown(button){     \n print(A mouse button was presssed down: + button); \n }")

    def mouseup(self):
        self.output.insert('1.0', "\n ccbRegisterMouseUpEvent(mousePressedUp); \n function mousePressedUp(button) \n {   \n print(A mouse button was presssed up: + button); \n }")

    def clonenode(self):
        self.output.insert('1.0', "\n var sourceNode = ccbGetSceneNodeFromName("+ self.nodename.get() +"); \n var newscenenode = ccbCloneSceneNode(sourceNode);")

    def removenode(self):
        self.output.insert('1.0', "\n ccbRemoveSceneNode( ccbGetSceneNodeFromName("+ self.nodename.get() +") );")

    def getcurrentnode(self):
        self.output.insert('1.0', "\n ccbGetCurrentNode()")

    def setcamera(self):
        self.output.insert('1.0',"\n ccbGetActiveCamera()")

    def getcamera(self):
        self.output.insert('1.0',"\n ccbSetActiveCamera(cameraNode)")

    def save(self):
        outputtext = self.output.get("1.0", "end-1c")
        actionsave = asksaveasfilename(defaultextension="js")
        with open(actionsave, "w") as fname3:
            fname3.write(outputtext)

    def func_create(self):
        self.output.insert('1.0', "function "+ self.funcname.get() +"() \n { \n \n }")

    def health_bar(self):
        
        with open("data/healthbar.js", "r") as fname2:
            text = fname2.read()
            self.output.insert('1.0',text)

    def do_later(self):
        with open("data/dolater.js", "r") as fname2:
            text = fname2.read()
            self.output.insert('1.0',text)

    def replace_1(self):
        with open("data/replace.js", "r") as fname2:
            text = fname2.read()
            self.output.insert('1.0',text)

    def load_texture(self):
        with open("data/loadtexture.js", "r") as fname2:
            text = fname2.read()
            self.output.insert('1.0',text)

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