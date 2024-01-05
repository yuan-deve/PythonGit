import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.simpledialog as dlg
import tkinter.filedialog as fd
import os
import json
import requests as req

# 全局变量
filepath = ''
filename = ''
thispath = ''

# 新建文件
def new(event=None):
    filename = dlg.askstring('新建', '请输入文件名')
    root.title(f'记事本-{filename}')
    text.delete(1.0, tk.END)

# 打开文件
def openfile(event=None):
    global thispath, filename, filepath
    filepath = fd.askopenfilename(title='打开文件', filetypes=[('文本文件', '*.txt')])
    thispath = os.path.dirname(filepath)
    filename = os.path.basename(filepath)
    root.title(f'记事本-{filename}')
    text.delete(1.0, tk.END)
    with open(filename, 'r') as f:
        text.insert(1.0, f.read())

# 保存文件
def save(event=None):
    global filepath
    if os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(text.get(1.0, tk.END))
    else:
        saveas()

# 另存为
def saveas(event=None):
    filepath = fd.asksaveasfilename(title='另存为', filetypes=[('文本文件', '*.txt')])
    with open(filepath, 'w+') as f:
        f.write(text.get(1.0, tk.END))

# 撤销
def undo(event=None):
    text.edit_undo()

# 重做
def redo(event=None):
    text.edit_redo()

# 剪切
def cut(event=None):
    text.event_generate('<<Cut>>')

# 复制
def copy(event=None):
    text.event_generate('<<Copy>>')

# 粘贴
def paste(event=None):
    text.event_generate('<<Paste>>')

# 查找
def find(event=None):
    text.tag_remove('found', '1.0', tk.END)
    target = dlg.askstring('查找', '请输入查找内容')
    if target:
        idx = '1.0'
        while True:
            idx = text.search(target, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            lastidx = '%s+%dc' % (idx, len(target))
            text.tag_add('found', idx, lastidx)
            idx = lastidx
        text.tag_config('found', foreground='lightblue')

# 全选
def selectall(event=None):
    text.tag_add('sel', '1.0', tk.END)

# 设置
def setting(event=None):
    setwindow = tk.Toplevel()
    setwindow.title('设置')
    setwindow.geometry('300x200')
    setwindow.resizable(False, False)

def openjson():
    with open('setting.json', 'w+') as f:
        setting = json.load(f)

# 创建窗口
root = tk.Tk()
root.title('记事本')
root.geometry('800x600')

# 创建菜单栏
menubar = tk.Menu(root)
root.config(menu=menubar)
# 创建子菜单‘文件’
menufile = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='文件', menu=menufile)

# 创建子菜单‘编辑’
menuedit = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='编辑', menu=menuedit)

# 创建子菜单‘设置’
menuset = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='设置', menu=menuset)

# 创建子菜单‘文件’的选项
menufile.add_command(label='新建', accelerator='Ctrl+N', command=new)
menufile.add_command(label='打开', accelerator='Ctrl+O', command=openfile)
menufile.add_command(label='保存', accelerator='Ctrl+S', command=save)
menufile.add_command(label='另存为', accelerator='Ctrl+Shift+S', command=saveas)
menufile.add_separator()
menufile.add_command(label='退出', accelerator='Ctrl+Q', command=quit)

# 创建子菜单‘编辑’的选项
menuedit.add_command(label='撤销', accelerator='Ctrl+Z', command=undo)
menuedit.add_command(label='重做', accelerator='Ctrl+Y', command=redo)
menuedit.add_separator()
menuedit.add_command(label='剪切', accelerator='Ctrl+X', command=cut)
menuedit.add_command(label='复制', accelerator='Ctrl+C', command=copy)
menuedit.add_command(label='粘贴', accelerator='Ctrl+V', command=paste)
menuedit.add_separator()
menuedit.add_command(label='查找', accelerator='Ctrl+F', command=find)
menuedit.add_command(label='全选', accelerator='Ctrl+A', command=selectall)

# 创建子菜单‘设置’的选项
menuset.add_command(label='设置', command=setting, accelerator='Ctrl+,')
menuset.add_separator()
menuset.add_command(label='打开json设置文件', command=openjson)

# 创建文本框
text = tk.Text(root, undo=True, font = ("Monaco", font_size.get()))

# 创建滚动条
scroll = tk.Scrollbar(root)
scroll.pack(side=tk.RIGHT, fill=tk.Y)
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)
text.pack(fill=tk.BOTH, expand=tk.YES)

# 创建状态栏
status = tk.StringVar()
status.set('Ln 1, Col 1')
statusbar = tk.Label(root, textvariable=status, anchor=tk.S)
statusbar.pack(side=tk.BOTTOM, fill=tk.X)

# 创建快捷键
root.bind('<Control-n>', lambda event: new())
root.bind('<Control-o>', lambda event: openfile())
root.bind('<Control-s>', lambda event: save())
root.bind('<Control-S>', lambda event: saveas())
root.bind('<Control-q>', lambda event: quit())
root.bind('<Control-z>', lambda event: undo())
root.bind('<Control-y>', lambda event: redo())
root.bind('<Control-x>', lambda event: cut())
root.bind('<Control-c>', lambda event: copy())
root.bind('<Control-v>', lambda event: paste())
root.bind('<Control-f>', lambda event: find())
root.bind('<Control-a>', lambda event: selectall())
root.bind('<Control-,>', lambda event: setting())

# 进入消息循环
root.mainloop()
