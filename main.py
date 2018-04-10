from commission import *
import os
from tkinter import *
import tkinter.messagebox as messagebox
import tkinter.filedialog as filedialog
import pandas as pd


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.finished = False

    def createWidgets(self):
        self.choosetestscrip = Button(self, text="选择待测脚本", command=self.choosefile1)
        self.choosetestscrip.pack()
        self.label1 = Label(self, text='')
        self.label1.pack()

        self.choosetestcase = Button(self, text="选择测试用例", command=self.choosefile2)
        self.choosetestcase.pack()
        self.label2 = Label(self, text='')
        self.label2.pack()

        self.startbutton = Button(self, text="开始测试", command=self.starttest)
        self.startbutton.pack()

        self.savebutton = Button(self, text="结果另存为", command=self.save)
        self.savebutton.pack()
        self.label3 = Label(self, text='')
        self.label3.pack()

    def choosefile1(self):
        filename = filedialog.askopenfilename(filetypes=(("py files", "*.py"), ))
        if filename != '':
            self.label1.config(text="您选择的待测脚本是:\n" + filename)
            self.testscrip = filename
        else:
            self.label1.config(text="您没有选择任何文件")

    def choosefile2(self):
        filename = filedialog.askopenfilename(filetypes=(("CSV files", "*.csv"), ))
        if filename != '':
            self.label2.config(text="您选择的测试用例是:\n" + filename)
            self.testcase = filename
        else:
            self.label2.config(text="您没有选择任何文件")

    def starttest(self):
        try:
            df = pd.read_csv(self.testcase)
            [row, col] = df.shape
            test_result = []
            for i in range(row):
                testcase = df.iloc[i]
                if self.testCommission(testcase):
                    test_result.append("pass")
                else:
                    test_result.append("failed")
            df['test_result'] = test_result
            self.df = df
            messagebox.showinfo(message="测试完成")
            self.finished = True
        except:
            self.finished = False
            messagebox.showinfo(title='error', message='请选择正确的文件')

    def testCommission(self, testcase):
        cmd = 'python ' + self.testscrip
        len = testcase.size
        for i in range(len-1):
            cmd += ' ' + str(testcase[i])
        result = os.popen(cmd)
        if int(result.read()) == testcase[len-1]:
            return True
        return False

    def save(self):
        if not self.finished:
            messagebox.showinfo(message='请先完成测试')
            return
        path = filedialog.asksaveasfilename(filetypes=(("csv files", "*.csv"), ))
        if path != '' and not os.path.exists(path):
            self.label3.config(text='您保存的路径: ' + path)
            self.df.to_csv(path)
        else:
            self.label3.config(text="路径错误")

app = Application()
# 设置窗口标题:
app.master.title('Test Tool')
app.master.minsize(600, 400)
# 主消息循环:
app.mainloop()
