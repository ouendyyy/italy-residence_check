import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

url = "https://questure.poliziadistato.it/stranieri"

user_input = simpledialog.askstring(
    title="居留查询",
    prompt="请输入居留小条passwd："
)

params = {
    'mime': '1',
    'lang': 'english',
    'pratica': user_input
}

headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": "_ga=GA1.1.175613607.1759919126; cookieconsent_status=dismiss; _ga_D4HCRLQJ3L=GS2.1.s1760804661$o3$g1$t1760805344$j34$l0$h0",
    "referer": "https://questure.poliziadistato.it/stranieri?lang=italian&mime=&pratica=055999475045&invia=Invia",
    "sec-ch-ua": '"Google Chrome";v="141", "Not?A_Brand";v="8", "Chromium";v="141"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36"
}

def show_result(message, error=False):
    """显示弹窗消息"""
    root = tk.Tk()
    root.withdraw() 
    if error:
        messagebox.showerror("查询失败", message)
    else:
        messagebox.showinfo("居留许可状态", message)
    root.destroy()


try:
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        m_ok_div = soup.find('div', class_='m-ok')
        
        if m_ok_div:
            full_text = m_ok_div.get_text(strip=True, separator=' ')
            
            show_result(full_text)

        else:
            show_result("未找到 class='m-ok' 的 div 元素，可能页面结构已变或查询失败。", error=True)

        with open("result.html", "w", encoding="utf-8") as f:
            f.write(response.text)
        print("\n 页面已保存为 result.html")

except requests.exceptions.RequestException as e:
    print(" 请求发生异常:", e)
except Exception as e:
    print(" 解析过程中出现错误:", e)