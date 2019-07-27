import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.com.tr/gp/product/B07DTN4R3J/ref=s9_acsd_top_hd_bw_bHuZGXf_c_x_w?pf_rd_m=A1UNQM1SR2CHM&pf_rd_s=merchandised-search-11&pf_rd_r=CQT638K0Z24F7C7PT4F3&pf_rd_t=101&pf_rd_p=a35db865-592c-5650-8c0b-85873909ea2d&pf_rd_i=16410138031'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36 OPR/62.0.3331.72'}

def check_price():
    page = requests.get(url= URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:6])
    if (converted_price > 100):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('alabeysamet@gmail.com', 'sxgadcdngfqqmuoe')

    subject = 'Hey, price down!'
    body = 'Check the amazon link= https://www.amazon.com.tr/gp/product/B07DTN4R3J/ref=s9_acsd_top_hd_bw_bHuZGXf_c_x_w?pf_rd_m=A1UNQM1SR2CHM&pf_rd_s=merchandised-search-11&pf_rd_r=CQT638K0Z24F7C7PT4F3&pf_rd_t=101&pf_rd_p=a35db865-592c-5650-8c0b-85873909ea2d&pf_rd_i=16410138031'
    msg = f'Subject:{subject}\n\n {body}'
    server.sendmail(
        'alabeysamet@gmail.com',
        'samet.alabey@hotmail.com',
        msg

        )
    print("Hey Mail Just sent.")

    server.quit()

check_price()