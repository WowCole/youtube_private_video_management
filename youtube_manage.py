import tkinter as tk
from tkinter import *
from tkinter import filedialog
from threading import Thread
from datetime import *
import time as tm
from tools import *

# try:
#     f=open("save.txt",'r')
# except Exception as e:
#     f=open("save.txt",'w')
#     f.write("이메일@이메일.com,0000")
#     print("새로 세이브파일 만들어짐")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        try:
            f=open("save.txt",'r')
        except Exception as e:
            f=open("save.txt",'w')
            f.write("이메일@이메일.com,0000")
            print("새로 세이브파일 만들어짐")
        def button_control(state):
            if state == "active":
                self.id_txt.config(state='normal')
                self.pw_txt.config(state='normal')
                self.btn.config(state="active")
                self.private.config(state="normal")
                self.unlisted.config(state="normal")
            else:
                self.id_txt.config(state='readonly')
                self.pw_txt.config(state='readonly')
                self.btn.config(state="disabled")
                self.private.config(state="disabled")
                self.unlisted.config(state="disabled")

                
        def folder():
            self.dirName=filedialog.askdirectory()
            self.inform.config(text=self.dirName)
            
        def reset():
            f=open("save.txt",'w')
            f.write("이메일@이메일.com,0000")
            f = open("save.txt", 'r')
            saved_email = f.line = f.readline().split(",")[0]
            self.id_txt.delete(0,999)
            self.id_txt.insert(0,saved_email)
            self.pw_txt.delete(0,999)
            self.inform.config(text="정보 초기화")
            print("정보 초기화")
        def go():
            th1=Thread(target=start_c)
            th1.daemon = True
            th1.start()
            return
        def start_c():
            button_control("disable")
            driver,wait=initialize()
            login_id = self.google_id.get()
            login_pw = self.google_pw.get()
            choosed_option=self.option.get()
            day=self.day.get()
            try:
                location=self.dirName
            except Exception as e:
                    self.inform.config(text=f"{e}")
                    button_control('active')
                    driver.quit()
                    return
            if len(login_id)<5 or len(login_pw)<5 or len(location)<5 or len(choosed_option)<5:
                self.inform.config(text="제대로 입력이 되지 않았음 재시도 필요")
                button_control('active')
                driver.quit()
                return
            last_time=save_check()
            new_save=login_id+","+str(datetime.timestamp(datetime.fromtimestamp(tm.time(),timezone.utc)))
            try:
                login(login_id,login_pw,driver,wait)
                self.inform.config(text="로그인 완료")
            except Exception as e:
                    self.inform.config(text=f"{e}")
                    button_control('active')
                    driver.quit()
                    return
            try:
                channels=setting(location,last_time,choosed_option,day)
            except:
                self.inform.config(text="폴더안의 파일이 잘못됨")
                button_control('active')
                driver.quit()
                return
            if len(channels) ==0:
                self.inform.config(text="변경사항 없음")
                button_control('active')
                driver.quit()
                f=open("save.txt", 'w')
                f.write(new_save)
                f.close()
                return
            
            for channel in channels:
                try:
                    select_channel(channel['name'],channel['tag'],choosed_option,driver,wait)
                    self.inform.config(text=f"{channel['name']} 채널 선택 완료")
                except Exception as e:
                    self.inform.config(text=f"{e}")
                    button_control('active')
                    driver.quit()
                    return
                try:
                    email_modify(self,channel,choosed_option,driver,wait)
                    self.inform.config(text=f"{channel['name']} 채널 이메일 수정 완료")
                except Exception as e:
                    self.inform.config(text=f"{e}")
                    button_control('active')
                    driver.quit()
                    return
            self.inform.config(text=f"전체 이메일 수정 완료")
            button_control('active')
            driver.quit()
            f=open("save.txt", 'w')
            f.write(new_save)
            f.close()
            return
        
        def disabled_day():
            if self.option.get()=="PRIVATE":
                self.mon.config(state="disabled")
                self.tue.config(state="disabled")
                self.wed.config(state="disabled")
                self.thu.config(state="disabled")
                self.fri.config(state="disabled")
                self.sat.config(state="disabled")
                self.sun.config(state="disabled")
            else:
                self.mon.config(state="normal")
                self.tue.config(state="normal")
                self.wed.config(state="normal")
                self.thu.config(state="normal")
                self.fri.config(state="normal")
                self.sat.config(state="normal")
                self.sun.config(state="normal")
            


        id_area=tk.Frame(self)
        id_area.grid(row=0,column=0)                
        option_area=tk.Frame(self)
        option_area.grid(row=0,column=1)
        day_area=tk.Frame(self)
        day_area.grid(row=1,column=0)
        start_area=tk.Frame(self)
        start_area.grid(row=1,column=1)
        inform_area=tk.Frame(self)
        inform_area.grid(row=2,column=0)
        self.option=tk.StringVar()
        self.google_id=tk.StringVar()
        self.google_pw=tk.StringVar()
        self.day=tk.StringVar()
        
        
        self.id_input = Label(id_area,text="ID")
        self.id_input.grid(row=1, column=1)
        f = open("save.txt", 'r')
        saved_email = f.line = f.readline().split(",")[0]
        self.id_txt = Entry(id_area,textvariable=self.google_id)
        self.id_txt.grid(row=1,column=2)
        self.id_txt.insert(0,saved_email)

        self.pw_input = Label(id_area,text="PW")
        self.pw_input.grid(row=2,column=1)

        self.pw_txt = Entry(id_area,show="*",textvariable=self.google_pw)
        self.pw_txt.grid(row=2,column=2)

        self.reset=Button(option_area,text="리셋",command=reset)
        self.reset.grid(row=2,column=4)

        self.btn = Button(start_area,text="시작!",command=go)
        self.btn.grid(row=8,column=4)

        self.unlisted = Radiobutton(option_area,text="일부공개",value="UNLISTED",variable=self.option,command=disabled_day)
        self.unlisted.grid(row=1,column=3)

        self.private = Radiobutton(option_area,text="비공개",value="PRIVATE",variable=self.option,command=disabled_day)
        self.private.grid(row=1,column=4)

        self.mon = Radiobutton(day_area,text="월",value="mon",variable=self.day)
        self.mon.grid(row=1,column=4)
        self.tue = Radiobutton(day_area,text="화",value="tue",variable=self.day)
        self.tue.grid(row=1,column=5)
        self.wed = Radiobutton(day_area,text="수",value="wed",variable=self.day)
        self.wed.grid(row=1,column=6)
        self.thu = Radiobutton(day_area,text="목",value="thu",variable=self.day)
        self.thu.grid(row=1,column=7)
        self.fri = Radiobutton(day_area,text="금",value="fri",variable=self.day)
        self.fri.grid(row=2,column=4)
        self.sat = Radiobutton(day_area,text="토",value="sat",variable=self.day)
        self.sat.grid(row=2,column=5)
        self.sun = Radiobutton(day_area,text="일",value="sun",variable=self.day)
        self.sun.grid(row=2,column=6)
        self.folder_btn=Button(option_area, text="폴더",command=folder)
        self.folder_btn.grid(row=2,column=3)

        self.inform = Label(inform_area)
        self.inform.grid(row=7,column=1)
     
def main():
    root = tk.Tk()
    root.resizable(False,False)
    myapp = App(root)
    myapp.master.title("유튜브 비공개 영상 관리 프로그램")
    myapp.mainloop()

    

if __name__ == '__main__':
    main()
