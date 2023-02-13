import tkinter as tk
from tkinter import *
from tkinter import filedialog
from threading import Thread
from datetime import *
import time as tm
from tools import *

try:
    f=open("save.txt",'r')
except Exception as e:
    f=open("save.txt",'w')
    f.write("이메일@이메일.com,0000")
    print("새로 세이브파일 만들어짐")
else:
    data=f.read().split(",")

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid()
        
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
            driver,wait=initialize()
            login_id = self.google_id.get()
            login_pw = self.google_pw.get()
            choosed_option=self.option.get()
            try:
                location=self.dirName
            except Exception as e:
                    self.inform.config(text=f"{e}")
                    return
            if len(login_id)<5 or len(login_pw)<5 or len(location)<5 or len(choosed_option)<5:
                self.inform.config(text="제대로 입력이 되지 않았음 재시도 필요")
                return
            self.id_txt.config(state='readonly')
            self.pw_txt.config(state='readonly')
            self.btn.config(state="disabled")
            self.private.config(state="disabled")
            self.unlisted.config(state="disabled")
        
            last_time=save_check()
            new_save=login_id+","+str(datetime.timestamp(datetime.fromtimestamp(tm.time(),timezone.utc)))
            try:
                login(login_id,login_pw,driver,wait)
                self.inform.config(text="로그인 완료")
            except Exception as e:
                    self.inform.config(text=f"{e}")
                    self.id_txt.config(state='normal')
                    self.pw_txt.config(state='normal')
                    self.btn.config(state="active")
                    self.private.config(state="normal")
                    self.unlisted.config(state="normal")
                    driver.quit()
                    return
            
            
            channels=setting(location,last_time)
            if len(channels) ==0:
                self.inform.config(text="변경사항 없음")
                self.id_txt.config(state='normal')
                self.pw_txt.config(state='normal')
                self.btn.config(state="active")
                self.private.config(state="normal")
                self.unlisted.config(state="normal")
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
                    self.id_txt.config(state='normal')
                    self.pw_txt.config(state='normal')
                    self.btn.config(state="active")
                    self.private.config(state="normal")
                    self.unlisted.config(state="normal")
                    driver.quit()
                    return
                try:
                    email_modify(self,channel,choosed_option,driver,wait)
                    self.inform.config(text=f"{channel['name']} 채널 이메일 수정 완료")
                except Exception as e:
                    self.inform.config(text=f"{e}")
                    self.id_txt.config(state='normal')
                    self.pw_txt.config(state='normal')
                    self.btn.config(state="active")
                    self.private.config(state="normal")
                    self.unlisted.config(state="normal")
                    driver.quit()
                    return
            self.inform.config(text=f"전체 이메일 수정 완료")
            self.id_txt.config(state='normal')
            self.pw_txt.config(state='normal')
            self.btn.config(state="active")
            self.private.config(state="normal")
            self.unlisted.config(state="normal")
            driver.quit()
            f=open("save.txt", 'w')
            f.write(new_save)
            f.close()
            return
    
        self.option=tk.StringVar()
        self.google_id=tk.StringVar()
        self.google_pw=tk.StringVar()

        self.id_input = Label(text="ID")
        self.id_input.grid(row=1, column=0)
        f = open("save.txt", 'r')
        saved_email = f.line = f.readline().split(",")[0]
        self.id_txt = Entry(textvariable=self.google_id)
        self.id_txt.grid(row=1,column=1)
        self.id_txt.insert(0,saved_email)

        self.pw_input = Label(text="PW")
        self.pw_input.grid(row=2,column=0)

        self.pw_txt = Entry(show="*",textvariable=self.google_pw)
        self.pw_txt.grid(row=2,column=1)

        self.reset=Button(text="리셋",command=reset)
        self.reset.grid(row=7,column=4)

        self.btn = Button(text="시작!",command=go)
        self.btn.grid(row=8,column=4)

        self.unlisted = Radiobutton(text="일부공개",value="UNLISTED",variable=self.option)
        self.unlisted.grid(row=1,column=4)

        self.private = Radiobutton(text="비공개",value="PRIVATE",variable=self.option)
        self.private.grid(row=2,column=4)

        self.folder_btn=Button(text="폴더",command=folder)
        self.folder_btn.grid(row=7,column=1)

        self.inform = Label()
        self.inform.grid(row=8,column=1)
     
        
def main():
    root = tk.Tk()
    myapp = App(root)
    myapp.master.title("유튜브 비공개 영상 관리 프로그램")
    myapp.mainloop()

    

if __name__ == '__main__':
    main()
