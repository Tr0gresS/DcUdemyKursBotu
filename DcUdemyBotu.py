from discord.ext import commands
import requests, re
from bs4 import BeautifulSoup


def udemy():
    response = requests.get("https://www.discudemy.com/feed/")
    if(response.status_code == 200):
        response_content = BeautifulSoup(response.content,"lxml")
        item =  response_content.select("channel > item > description >a")
     
        for j in item:
            url_code = j.get("href")
            
            first_index = url_code[26:]
            p = re.search("/",first_index)
            url_content = first_index[p.end():]
            response_coupon = requests.get(f"https://www.discudemy.com/go/{url_content}")
            
            response_coupon_content = BeautifulSoup(response_coupon.content,"lxml")
            url_coupon = re.search('<a href="(https://www.udemy.com/course.*) target=',str(response_coupon_content))
            content = url_coupon.group(1)
           
            return content
    else:
        print(response.status_code)

           
bot = commands.Bot('-')


if __name__ == "__main__":
    
    
    @bot.command()
    async def start(msg):
        kurs = None    
        while True:
            return_content = udemy()
            if return_content != kurs:
                kurs = return_content
                print(kurs)
                await msg.send(kurs)
    
      


    bot.run("Token")
