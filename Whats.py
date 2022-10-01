from webbrowser import open
from urllib.parse import quote
import pyautogui as pg
import os

class Whats():
    def __init__(self) -> None:
        self.url="https://web.whatsapp.com/send?phone={}&text={}"
        self.attach="images/attach.png"
        self.document="images/document.png"
        self.image="images/image.png"
        self.home="images/home.png"
        self.search="images/search.png"
    
    def _format_no(self,no:str):
        no=no.replace(" ","")
        if(len(no)==10):
            return f"+91{no}"
        elif (len(no)>10):
            return no[:13] if no.startswith("+") else  f"+{no[:12]}"
        else:
            raise "Invalid no"
    
    
    def _click_image(self,logo):
            pg.click(pg.locateCenterOnScreen(logo))
            pg.sleep(0.5)
            

    def _search_for_document(self,location:str):
        self._click_image(self.home)
        path_lis=location.split(os.path.sep)[3:]
        for i in path_lis:
            self._click_image(self.search)
            pg.typewrite(i)
            pg.sleep(0.5)
            pg.press("down")
            pg.sleep(0.5)
            pg.press("return")


    def send_msg(self,no:str,msg:str,wait_time:int=30):
        no=self._format_no(no)
        
        open(self.url.format(no,quote(msg)))

        pg.sleep(wait_time)
        pg.press("return")

        pg.sleep(5)
        pg.hotkey("ctrl","w")
    
    def send_doc(self,no:str,doc:str,wait_time:int=30,is_img:bool=False):
        doc=os.path.abspath(doc)

        if not os.path.exists(doc):
            print("Sorry file not found. Please provide a valid path")
            return

        open(self.url.format(self._format_no(no)," "))
        pg.sleep(wait_time)

        self._click_image(self.attach)
        pg.sleep(3)

        if is_img:
            self._click_image(self.image)
        else :
            self._click_image(self.document)

        pg.sleep(3)

        self._search_for_document(doc)
        pg.sleep(5)
        
        pg.press("return")