import tkinter
import tkinter.messagebox
import math
class JSQ:


 def __init__(self):
 #创建主界面
 self.root = tkinter.Tk()
 self.root.minsize(270, 330)
 self.root.maxsize(270, 330)
 self.root.title('小可乐的计算器')
 #定义一个变量赋值给页面label
 self.result = tkinter.StringVar()
 #界面先显示个0
 self.result.set(0)
 # 设置一个全局变量 运算数字和符号的列表
 self.lists = []
 # 添加一个判断是否按下运算符号的标志
 self.isPressSign = False
 # 添加一个判断是否运算完毕的标志,如果运算完毕在获取数字的方法中会清空上一轮运算结果
 self.islistsclear = False
 # 添加一个判断百分号是否使用的功能
 self.isbaifenhao = False
 # 为了下面的百分号方法使用(在百分号中为按下运算符号之后的数字)
 self.num1 = ''
 # 定义一个全局变量（获取百分好的结果）为了在‘='运算的时候输出
 self.result3 = None
 # 获取运算符号之前的数字
 self.num = ''
 # 获取运算符号给百分好方法使用
 self.sign1 = ''
 self.layout()
 self.menubar()
 #将窗口一直显示
 self.root.mainloop()

 def menubar(self):
 # 创建总菜单
 allmenu = tkinter.Menu(self.root)
 # 创建子菜单
 filemenu = tkinter.Menu(allmenu, tearoff=0)
 # 在子菜单里添加文件
 filemenu.add_command(label='标准型(T) Alt+1',command = lambda : self.func2())
 filemenu.add_command(label='科学性(S) Alt+2',command = lambda : self.func2())
 filemenu.add_command(label='程序员(p) Alt+3',command = lambda : self.func2())
 filemenu.add_command(label='统计信息(A) Alt+4',command = lambda : self.func2())
 # 创建分割线
 filemenu.add_separator()
 filemenu.add_command(label='历史记录(Y) Ctrl+H',command = lambda : self.func2())
 filemenu.add_command(label='数学分组(I)',command = lambda : self.func2())
 filemenu.add_separator()
 filemenu.add_command(label='基本(B) Ctrl+F4',command = lambda : self.func2())
 filemenu.add_command(label='单位转换(U) Ctrl+U',command = lambda : self.func2())
 filemenu.add_command(label='日期计算(D) Ctrl+E',command = lambda : self.func2())
 # 在子菜单里再创建一个菜单
 filemenunei = tkinter.Menu(filemenu, tearoff=0)
 # 在子菜单里的菜单添加文件
 filemenunei.add_command(label='抵押(M)',command = lambda : self.func2())
 filemenunei.add_command(label='汽车租赁(V)',command = lambda : self.func2())
 filemenunei.add_command(label='油耗（mpg）(F)',command = lambda : self.func2())
 filemenunei.add_command(label='油耗（1/100km）(U)',command = lambda : self.func2())
 # 将子菜单里的菜单添加到子菜单里
 filemenu.add_cascade(label='工作表(W)', menu=filemenunei)
 # 添加退出功能
 filemenu.add_command(label='退出', command=self.root.quit)
 # 将子菜单添加到总菜单里
 allmenu.add_cascade(label='查看(V)', menu=filemenu)
 # 再创建一个子菜单
 editmenu = tkinter.Menu(allmenu, tearoff=0)
 # 在子菜单里添加文件
 editmenu.add_command(label='复制(C)',command = lambda : self.func2())
 editmenu.add_command(label='粘贴(P)',command = lambda : self.func2())
 # 创建分割线
 editmenu.add_separator()
 # 在子菜单里创建一个菜单
 editmenunei = tkinter.Menu(editmenu, tearoff=0)
 # 在子菜单里的菜单添加文件
 editmenunei.add_command(label='复制历史记录(I)', stat='disable')
 editmenunei.add_command(label='编辑(E) F2', stat='disable')
 editmenunei.add_command(label='取消编辑(N) Esc', stat='disable')
 editmenunei.add_command(label='清除(L) Ctrl+Shift+D', stat='disable')
 # 将子菜单里的菜单添加到子菜单
 editmenu.add_cascade(label='历史记录(H)', menu=editmenunei)
 # 将子菜单添加到总菜单
 allmenu.add_cascade(label='编辑(E)', menu=editmenu)
 # 创建第三个子菜单
 helpmenu = tkinter.Menu(allmenu, tearoff=0)
 # 在第三个子菜单里添加文件
 helpmenu.add_command(label='查看帮助(v) F1',command = lambda : self.func2())
 # 创建分割线
 helpmenu.add_separator()
 helpmenu.add_command(label='关于计算器(A)',command = lambda : self.func2())
 # 将第三个子菜单添加到总菜单中
 allmenu.add_cascade(label='帮助(H)', menu=helpmenu)
 # 将总菜单布局到主窗口
 self.root.config(menu=allmenu)

 # 下面代码用于页面布局
 def layout(self):
 #显示结果的标签
 label = tkinter.Label(self.root, textvariable=self.result, bg='white', font=('黑体', 10), anchor='e')
 label.place(x=20, y=10, width=230, height=30)

 btnmc = tkinter.Button(self.root, text='MC',command = lambda : self.func2())
 btnmc.place(x=20, y=50, width=30, height=30)

 btnmr = tkinter.Button(self.root, text='MR',command = lambda : self.func2())
 btnmr.place(x=70, y=50, width=30, height=30)

 btnms = tkinter.Button(self.root, text='MS',command = lambda : self.func2())
 btnms.place(x=120, y=50, width=30, height=30)

 btnmjia = tkinter.Button(self.root, text='M+',command = lambda : self.func2())
 btnmjia.place(x=170, y=50, width=30, height=30)

 btnmjian = tkinter.Button(self.root, text='M-',command = lambda : self.func2())
 btnmjian.place(x=220, y=50, width=30, height=30)

 btnjiantou = tkinter.Button(self.root, text='←', command=lambda: self.jiantou())
 btnjiantou.place(x=20, y=90, width=30, height=30)

 btnce = tkinter.Button(self.root, text='CE', command=lambda: self.CE())
 btnce.place(x=70, y=90, width=30, height=30)

 btnc = tkinter.Button(self.root, text='C', command=lambda: self.clears())
 btnc.place(x=120, y=90, width=30, height=30)

 btnzhengfu = tkinter.Button(self.root, text='±', command=lambda: self.zhenffu())
 btnzhengfu.place(x=170, y=90, width=30, height=30)

 btnkaigen = tkinter.Button(self.root, text='√', command=lambda: self.sqrts())
 btnkaigen.place(x=220, y=90, width=30, height=30)

 btn7 = tkinter.Button(self.root, text='7', command=lambda: self.pressNum('7'))
 btn7.place(x=20, y=130, width=30, height=30)

 btn8 = tkinter.Button(self.root, text='8', command=lambda: self.pressNum('8'))
 btn8.place(x=70, y=130, width=30, height=30)

 btn9 = tkinter.Button(self.root, text='9', command=lambda: self.pressNum('9'))
 btn9.place(x=120, y=130, width=30, height=30)

 btnchu = tkinter.Button(self.root, text='/', command=lambda: self.pressCompute('/'))
 btnchu.place(x=170, y=130, width=30, height=30)

 btnbaifen = tkinter.Button(self.root, text='%', command=lambda: self.baifenhao())
 btnbaifen.place(x=220, y=130, width=30, height=30)

 btn4 = tkinter.Button(self.root, text='4', command=lambda: self.pressNum('4'))
 btn4.place(x=20, y=170, width=30, height=30)

 btn5 = tkinter.Button(self.root, text='5', command=lambda: self.pressNum('5'))
 btn5.place(x=70, y=170, width=30, height=30)

 btn6 = tkinter.Button(self.root, text='6', command=lambda: self.pressNum('6'))
 btn6.place(x=120, y=170, width=30, height=30)

 btncheng = tkinter.Button(self.root, text='*', command=lambda: self.pressCompute('*'))
 btncheng.place(x=170, y=170, width=30, height=30)

 btnfenshu = tkinter.Button(self.root, text='1/X', command=lambda: self.fenshu())
 btnfenshu.place(x=220, y=170, width=30, height=30)

 btn1 = tkinter.Button(self.root, text='1', command=lambda: self.pressNum('1'))
 btn1.place(x=20, y=210, width=30, height=30)

 btn2 = tkinter.Button(self.root, text='2', command=lambda: self.pressNum('2'))
 btn2.place(x=70, y=210, width=30, height=30)

 btn3 = tkinter.Button(self.root, text='3', command=lambda: self.pressNum('3'))
 btn3.place(x=120, y=210, width=30, height=30)

 btnjian = tkinter.Button(self.root, text='-', command=lambda: self.pressCompute('-'))
 btnjian.place(x=170, y=210, width=30, height=30)

 btndenghao = tkinter.Button(self.root, text='=', command=lambda: self.pressEqual())
 btndenghao.place(x=220, y=210, width=30, height=70)

 btn0 = tkinter.Button(self.root, text='0', command=lambda: self.pressNum('0'))
 btn0.place(x=20, y=250, width=80, height=30)

 btndian = tkinter.Button(self.root, text='.', command=lambda: self.pressNum('.'))
 btndian.place(x=120, y=250, width=30, height=30)

 btnjia = tkinter.Button(self.root, text='+', command=lambda: self.pressCompute('+'))
 btnjia.place(x=170, y=250, width=30, height=30)

 # 数字函数(获取数字的函数)
 def pressNum(self,num):
 # 下面的百分好会用到
 self.num1 = num
 # 判断是否按下运算符号
 if self.isPressSign == False:
  pass
 #如果按下运算符号界面归0
 else:
  self.result.set(0)
  self.isPressSign = False
 # 判断运算是否完毕
 if self.islistsclear == False:
  # 获取面板上原有的数字
  oldNum = self.result.get()
  # 判断原有数字是否为零
  if oldNum == '0':
  #将传入的数字显示
  self.result.set(num)
  else:
  #原来的数字加上现在输入的数字
  newNum = oldNum + num
  self.result.set(newNum)
 # 运算完毕界面自动清空
 else:
  # lists.clear()#如果添加这行代码就不能在上一轮运算结果的基础上运算了
  self.result.set('0')
  self.islistsclear = False
  self.result.set(num)

 # 运算操作(获取运算符号然后将数字和符号添加到列表中)
 def pressCompute(self,sign):
 # 获取界面上的数字
 if True:
  #获取输入运算符之前的数字
  self.num = self.result.get()
  #将数字加入列表之中
  self.lists.append(self.num)
  #将运算符加入到列表之中
  self.lists.append(sign)
  #将运算符赋值给sign1（下面的百分号方法会用到）
  self.sign1 = sign
  #将是否按下运算符号标志改成True
  self.isPressSign = True
 # 在刚开始的时候添加一个负号（-）用于正负好转换使用
 #如果列表第一位为0
 if self.lists[0] == '0':
  #如果列表第二位为‘-'
  if self.lists[1] == '-':
  self.result.set('-')
  # 设置运算符号的状态
  self.isPressSign = False

 # 获取运算结果（将列表内的值转换为字符串，然后将字符串用python代码执行）
 def pressEqual(self):
 # 获取当前页面的数字
 curnum = self.result.get()
 self.lists.append(curnum)
 #将列表中的数据转换为字符串
 computeStr = ''.join(self.lists)
 #将字符串用python代码执行
 endNum = eval(computeStr)
 #界面显示结果
 self.result.set(endNum)
 #如果百分号标志触发
 if self.isbaifenhao == True:
  #界面显示self.result3
  self.result.set(self.result3)
 #运算结束后将列表清空
 self.lists.clear()
 #将运算标志改成True
 self.islistsclear = True

 # 清空运算
 def clears(self):
 self.lists.clear()
 self.result.set('0')

 # 删除上一位数字
 def CE(self):
 self.result.set('0')

 # 用于更改数的正负值
 def zhenffu(self):
 self.result1 = self.result.get()
 self.result.set(float(self.result1) * (-1))
 self.islistsclear = True

 # 用于开平方运算
 def sqrts(self):
 result1 = self.result.get()
 self.result.set(math.sqrt(float(result1)))
 self.lists.clear()
 self.islistsclear = True

 # 用于求x/9的值
 def fenshu(self):
 result1 = self.result.get()
 self.result.set(1 / float(result1))
 self.islistsclear = True

 #用于求百分号功能的方法
 def baifenhao(self):
 listss = []
 # 判断如果输入一个数没输运算符号的话界面自动归零
 if len(self.lists) < 1:
  self.result.set(0)
 else:
  #获取输入运算符号之前的数字
  a1 = float(self.num)
  #获取运算符号
  a2 = self.sign1

  #再次获取输入运算符号之前的数字
  a3 = float(self.num)

  a4 = '*'
  #算出最后一个数字的百分数
  a6 = float(self.num1) / 100

  #算出百分号的那个结果
  resultmuqian = a3 * a6
  #总结果
  resultbai = str(a1) + a2 + str(a3) + a4 + str(a6)
  #将字符串用python代码执行
  self.result3 = eval(resultbai)
  #在界面上按下%符号是显示的结果
  self.result.set(resultmuqian)
  #改变百分号的标志
  self.isbaifenhao = True

 #delete删除后一位数字
 def jiantou(self):
 result1 = self.result.get()
 result1 = list(result1)
 del result1[-1]
 result1 = str(result1)
 self.result.set(result1)

 def func2(self):
 tkinter.messagebox.askokcancel(title = '略过',message='运算错误')


myjsq = JSQ()