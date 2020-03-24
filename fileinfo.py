import os
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
from PIL import Image,ImageTk


#打开文件 
def openfile():  
    global filename
    #利用tf库里的askopenfilename函数得到文件的绝对路径。如果不是很清晰，后面用defaultextension函数添加'txt'来说明文件类型
    filename = askopenfilename(defaultextension = '.txt')
    if filename == '':
        filename=None
    else:
        ##利用os.path.basename()函数返回path最后的文件名，即格式
        window.title(os.path.basename(filename))
        #清空原来的文档
        text.delete(1.0,END)
        f = open(filename,'r')
        #读入新的文档
        text.insert(1.0,f.read())
        f.close()
        
#新建文档
def new():
    window.title('新建文档')
    filename = None
    text.delete(1.0,END)
 
#保存
def save():
    try:
        f = open(filename,'w')
        content = text.get(1.0,END)
        f.write(content)
        f.close()
    except:
        #如果这是一个新建的文档保存，就用saveas指令
        saveas()
 
 #另存为
def saveas():
    f = asksaveasfilename(initialfile= '新建文档', defaultextension='.txt')
    filename = f
    window.title(os.path.basename(f))
    fw = open(f,'w')
    content = text.get(1.0,END)
    fw.write(content)
    fw.close()
    window.title(os.path.basename(f))


#引入event类来实现键盘上的复制粘贴等操作，然后用generate函数来实现

#复制 
def copy():
    text.event_generate('<<Copy>>')
#粘贴 
def paste():
    text.event_generate('<<Paste>>')

#全选 
def selectAll():
    #利用tag函数中的add操作，sel表示全选
    text.tag_add('sel','1.0',END)

#剪切
def cut():
    text.event_generate('<<Cut>>')

#撤销
def redo():
    text.event_generate('<<Redo>>')

#重做
def undo():
    text.event_generate('<<Undo>>')

#查找指定内容的个数 
def search():
    def dosearch():
        wordname = entry1.get()             #获取查找的内容--string型
        essay = str(text.get(1.0,END))#文本框的内容
        showinfo(title='查找结果：',message=("查找结果：{}共有{}个").format(wordname,essay.count(wordname)))#直接用count函数找
        
    topsearch = Toplevel(window)
    topsearch.geometry('400x50+150+200')
    label1 = Label(topsearch,text='请输入需要查找的单词')
    label1.grid(row=0, column=0,padx=5)
    entry1 = Entry(topsearch,width=20)
    entry1.grid(row=0, column=1,padx=5)
    button1 = Button(topsearch,text='查找',command=dosearch)
    button1.grid(row=0, column=3)

#统计词数
def allwords():
    content=text.get(1.0,END)
    wordlist=list((' '+content+' ').split())
    showinfo(title='文章总词数：',message='{}'.format(len(wordlist)))

#小写化并输出    
def lower_essay():
    content=text.get(1.0,END)
    wordlist=list(((' '+content+' ').lower()).split())
    def f(x):
        for i in range(len(wordlist)):
            if x in wordlist[i]:
                j=wordlist[i].replace(x,'')
                wordlist[i]=j                
    f('.')
    f(',')
    f('?')
    f('“')
    f('”')
    f('-')
    f('—')
    f('’')
    f('，')
    f(':')
    wl1=[]
    for i in range(len(wordlist)):
        if wordlist[i]!='':
            wl1.append(wordlist[i])
    text.delete(1.0,END)
    text.insert(1.0,''.join(wl1))

#统计所有单词词频
def countword():
    content=text.get(1.0,END)
    wordlist=list(((' '+content+' ').lower()).split())
    def f(x):
        for i in range(len(wordlist)):
            if x in wordlist[i]:
                j=wordlist[i].replace(x,'')
                wordlist[i]=j                
    f('.')
    f(',')
    f('?')
    f('“')
    f('”')
    f('-')
    f('—')
    f('’')
    f('，')
    f(':')
    wl1=[]
    for i in range(len(wordlist)):
        if wordlist[i]!='':
            wl1.append(wordlist[i])
    word=[]
    for i in wl1:
        if i in word:
            continue
        else:
            word.append(i)
    word_number=[]
    for i in word:
        word_number.append(wordlist.count(i))  
    each_word_number=dict(zip(word,word_number))
    window1=Tk()
    window1.geometry("600x600+200+200")
    window1.title('所有单词词频')
    newPad = Text(window1, undo=True)
    newPad.pack(expand=YES, fill=BOTH)
    for i in each_word_number:
        newPad.insert(1.0,i+'  '+str(each_word_number[i])+'\n')
    window1.mainloop()

#将使用频率最高的6个字母绘图输出
def mostused():
    def getkey(dic,value):
        return [k for (k,v) in dic.items() if v == value]
    n=6
    content=text.get(1.0,END)
    wordlist=list(((' '+content+' ').lower()).split())
    def f(x):
        for i in range(len(wordlist)):
            if x in wordlist[i]:
                j=wordlist[i].replace(x,'')
                wordlist[i]=j                
    f('.')
    f(',')
    f('?')
    f('“')
    f('”')
    f('-')
    f('—')
    f('’')
    f('，')
    f(':')
    wl1=[]
    for i in range(len(wordlist)):
        if wordlist[i]!='':
            wl1.append(wordlist[i])
    word=[]
    for i in wl1:
        if i in word:
            continue
        else:
            word.append(i)
    word_number=[]
    for i in word:
        word_number.append(wordlist.count(i))  
    each_word_number=dict(zip(word,word_number))
    f1=open('停词表.txt','r')
    stop_word=list(f1.readlines())
    for i in range(len(stop_word)):
        stop_word[i]=stop_word[i].strip('\n')
    
    for i in stop_word:
        if i in word:
            del each_word_number[i]
    E_numbers=sorted(list(each_word_number.values()),reverse=True)
    new_numbers=[]
    for i in range(n):
        new_numbers.append(E_numbers[i])
    mostused_words=[]
    for i in new_numbers:
        mostused_words+=getkey(each_word_number,i)
    mostusedwords=[]
    for i in mostused_words:
        if i in mostusedwords:
            continue
        else:
            mostusedwords.append(i)#前六个频率最高的字母
    real_wordnumber=[]
    for i in mostusedwords:
        real_wordnumber.append(each_word_number[i])#前六个最常见的字母对应的数字       
    import numpy as np
    import matplotlib.pyplot as plt
    N =len(mostusedwords)
    ind = np.arange(N)  # the x locations for the groups
    width = 0.4      # the width of the bars
    fig, ax = plt.subplots()
    rects1 = ax.bar(ind,real_wordnumber, width)
    from pylab import mpl
    mpl.rcParams['font.sans-serif']=['SimHei']
    ax.set_ylabel('单词数值')
    ax.set_title('单词数值分析表')
    ax.set_xticks(ind+width)
    ax.set_xticklabels(list(mostusedwords))
    plt.savefig('photo.PNG')
    plt.show()
    top=Toplevel()
    top.geometry('800x600')
    image=Image.open('photo.PNG')
    photo=ImageTk.PhotoImage(image)
    Lab=Label(top,image=photo,text='warning')
    Lab.pack()
    top.mainloop()
        

#替换功能
def replace():
    def r_word():
        oword=entry1.get()
        nword=entry2.get()
        content=text.get(1.0,END)
        ncontent=content.replace(oword,nword)
        text.delete(1.0,END)
        text.insert(1.0,ncontent)
        topsearch.destroy()
    
    topsearch = Tk()
    topsearch.title('替换')
    topsearch.geometry('200x100+0150+200')
    label1 = Label(topsearch,text='原单词：')
    label1.grid(row=0, column=0,padx=5)
    entry1 = Entry(topsearch,width=10)
    entry1.grid(row=0, column=1,padx=5)
    label2 = Label(topsearch,text='替换的新单词：')
    label2.grid(row=1, column=0,padx=5)
    entry2 = Entry(topsearch,width=10)
    entry2.grid(row=1, column=1,padx=5)
    
    button1 = Button(topsearch,text='开始替换',command=r_word)
    button1.grid(row=2, column=1)
    
def author():
    showinfo(title='程序的作者是',message='殷望——18377226')
 
def reback():
    showinfo('有问题请联系:','15884007088')
     
filename = ''

window = Tk()
window.title('文档编辑器-殷望-18377226')
window.geometry("800x600+100+50")

#设置主界面的菜单
menubar = Menu(window)
window.config(menu = menubar)

#文件菜单
filemenu = Menu(menubar)
filemenu.add_command(label='新建   Ctrl + N', command= new)
filemenu.add_command(label='打开   Ctrl + O',command = openfile)
filemenu.add_command(label='保存   Ctrl + S', command=save)
filemenu.add_command(label='另存为   Ctrl + Shift + S',command=saveas)
menubar.add_cascade(label='文件',menu=filemenu)

#编辑菜单 
editmenu = Menu(menubar)
editmenu.add_command(label = "复制   Ctrl + C", command=copy)
editmenu.add_command(label = "粘贴   Ctrl + V", command= paste)
editmenu.add_command(label = "剪切   Ctrl + X",command=cut)
editmenu.add_command(label = "全选   Ctrl + A", command= selectAll)
editmenu.add_separator()
editmenu.add_command(label='撤销   Ctrl + Z', command=undo)
editmenu.add_command(label='重做   Ctrl + y', command=redo)
menubar.add_cascade(label = "编辑",menu = editmenu)



#特殊功能
specialmenu = Menu(menubar)
specialmenu.add_command(label='拆解文章并小写化输出',command=lower_essay)
specialmenu.add_separator() 
specialmenu.add_command(label='总词数',command=allwords)
specialmenu.add_separator()
specialmenu.add_command(label = "统计指定单词词频", command=search)
specialmenu.add_separator()
specialmenu.add_command(label='统计所有单词词频',command=countword)
specialmenu.add_command(label='关键词生成并绘图（不包含停词表）',command=mostused)
specialmenu.add_separator()
specialmenu.add_command(label='替换功能',command=replace)
specialmenu.add_separator()
menubar.add_cascade(label = "指导书要求的功能往这看",menu=specialmenu)

#关于
aboutmenu = Menu(menubar)
aboutmenu.add_command(label = "作者", command=author)
aboutmenu.add_command(label = "用户反馈", command = reback)
menubar.add_cascade(label = "关于",menu=aboutmenu)

#toolbar最上面有保存和打开的框
toolbar = Frame(window, height=20,bg='light yellow')
shortButton = Button(toolbar, text='打开',command = openfile)
shortButton.pack(side=LEFT, padx=5, pady=5) 
shortButton = Button(toolbar, text='保存', command = save)
shortButton.pack(side=LEFT)
toolbar.pack(expand=NO,fill=X) 
lnlabel =Label(window, width=2, bg='light blue')
lnlabel.pack(side=LEFT, fill=Y) 
text = Text(window,undo=True)
text.pack(expand=YES, fill=BOTH)

#滚动
scroll = Scrollbar(text)
text.config(yscrollcommand= scroll.set)
scroll.config(command = text.yview)
scroll.pack(side=RIGHT,fill=Y)

#Status Bar最下面的框
status = Label(window,height=1,bg='light pink',bd=3, relief=SUNKEN,anchor=W)
status.pack(side=BOTTOM, fill=X)

window.mainloop()


