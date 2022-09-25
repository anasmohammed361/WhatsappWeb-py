from webbrowser import open
from urllib.parse import quote
import webbrowser
import pyautogui as pg
import os

class Whats():
    def __init__(self) -> None:
        self.url="https://web.whatsapp.com/send?phone={}&text={}"
        self.attach="images/attach.png"
        self.document="images/document.png"
        self.image="images/image.png"
    
    def format_no(self,no:str):
        no=no.replace(" ","")
        if(len(no)==10):
            return f"+91{no}"
        elif (len(no)>10):
            return no[:12] if no.startswith("+") else  f"+{no[:12]}"
        else:
            raise "Invalid no"
    
    
    def _click_image(self,*logo:str):
        for i in logo:
            pg.click(pg.locateCenterOnScreen(logo))
            pg.sleep(0.5)


    def _click_text(self,*texts):
        pass

    def send_msg(self,no:str,msg:str,wait_time:int=20,attach_img:bool=False,attach_document:bool=False):
        no=self.format_no(no)
        self.url.format(no,quote(msg))
        webbrowser.open(self.url)
        pg.sleep(wait_time)
        pg.press("return")
        if attach_document:
            pass
        if attach_img:
            pass
        pg.sleep(5)
        pg.hotkey("ctrl","w")
    
    def send_image(self,img:str):
        if os.path.exists(img):
            self._click_image(self.attach,self.image)
