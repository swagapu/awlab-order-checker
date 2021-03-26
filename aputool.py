# ------------------------------------------------------------------------------- #
import sys, logging, urllib3, json, requests, csv, os, random, time, datetime, uuid, threading, winreg, platform, wget, zipfile, colorlog, requests, discord, cloudscraper
from dhooks import Webhook
from dhooks import Embed
from discord.ext import commands
from termcolor import colored
from colorama import Fore, init
from datetime import datetime, timedelta
from bs4 import BeautifulSoup as Bs


bot = commands.Bot(command_prefix='+')


def sprint(text):
    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - {text}", 'yellow'))
def sprint2(text):
    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - {text}", 'red'))


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game('APUtool, +help'))
    sprint(f'Logged in as: {bot.user.name}')    
    sprint(f'User ID: {bot.user.id}')
    sprint('--------------------------------------')


bot.remove_command('help')


@bot.command(aliases=['Ping'])
async def ping(ctx):
    ping = discord.Embed(colour =55552, title = 'Pong!  :ping_pong:', description = (f'`Bot latency: {round(bot.latency * 1000)} ms`'))
    ping.set_footer(text="APUTOOL", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
    ping.timestamp = datetime.utcnow()
    await ctx.send(embed=ping) 


@bot.command()
async def help(ctx):


    embed = discord.Embed(title="**APUTOOL - DRIPPEST EVER**", description="with love - APU#0001", color=3997605)
    embed.url = 'https://twitter.com/swagapu'
    embed.add_field(name='**AW-LAB checker**', value='+awlabcheck *orderN* *email* *zipcode*' , inline=False)
    embed.add_field(name='**PING**', value='+ping - check if the bot is online' , inline=False)
    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
    embed.timestamp = datetime.utcnow()

    await ctx.send(embed=embed)



@bot.command(pass_context=True)
async def awlabcheck(ctx, ordernumber, email, zipcode):

    s = cloudscraper.create_scraper(captcha={'provider':'2captcha','api_key': 'c75008aa5ed9b23551f6766476b8a234'})


    mainheaders = {
        'authority': 'www.aw-lab.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="86", "\\"Not\\\\A;Brand";v="99", "Google Chrome";v="86"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'it,en-US;q=0.9,en;q=0.8',
    }
    trackresultheaders = {
        'authority': 'www.aw-lab.com',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'upgrade-insecure-requests': '1',
        'origin': 'https://www.aw-lab.com',
        'content-type': 'application/x-www-form-urlencoded',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'referer': 'https://www.aw-lab.com/controllaspedizione',
        'accept-language': 'it',
        '$cookie': '__cfduid=d3ac7097a86ce9e6469e58e186a4c05731614469711; dwac_1475e29a8c29e08671dad6a42b=yH9z1WALHb6PjRv4pdBylBWWIln-EhO7ucU%3D|dw-only|||EUR|false|Europe%2FRome|true; cqcid=ac7xyGSFa0uwGFOprroe5H5QXA; cquid=||; sid=yH9z1WALHb6PjRv4pdBylBWWIln-EhO7ucU; dwanonymous_106322550253ae9980e0f038b6061a90=ac7xyGSFa0uwGFOprroe5H5QXA; __cq_dnt=0; dw_dnt=0; dwsid=LpyGZBeWZIolKH6o7wulkvN11-iJj2qPE2A_CSV6bV9vMoYJuI5Rs7wMChI4L7vN8P39GSVfxr6tqvC-k08Npw==; _fbp=fb.1.1614469712825.107895784; _ga=GA1.2.1803300725.1614469713; _gid=GA1.2.861391635.1614469713; _gat_UA-18276494-1=1; __cq_uuid=ac7xyGSFa0uwGFOprroe5H5QXA; __cq_seg=0~0.00\\u00211~0.00\\u00212~0.00\\u00213~0.00\\u00214~0.00\\u00215~0.00\\u00216~0.00\\u00217~0.00\\u00218~0.00\\u00219~0.00; fanplayr=%7B%22uuid%22%3A%221614469713240-1fd49dc41d2cb94b2ead2d66%22%2C%22uk%22%3A%225.Xmtjk1AMbxAfjTOlHF2.1614469712%22%2C%22sk%22%3A%220d49057ca3e063a13ce0972891ea73f8%22%2C%22se%22%3A%22e1.fanplayr.com%22%2C%22tm%22%3A1%2C%22t%22%3A1614469713834%7D',
    }

    while 1:
        try:

            print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Getting page", 'yellow'))

            productPage = s.get('https://www.aw-lab.com/trackorder', headers=mainheaders, timeout=10)
            soup = Bs(productPage.text, 'html.parser')
            cftoken = soup.find('input', {'name':'csrf_token'})['value']

        
            if productPage.status_code not in (200, 302):
                print(f'Error getting page: [{str(productPage.status_code)}]')
                print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Error getting page: [{str(productPage.status_code)}]", 'red'))

            else:
                print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Successfully got page!", 'green'))

        except Exception as e:
            print(f'Error diocane: {str(e)}')

        try:

            orderPayload = {
            'dwfrm_orderstatus_orderno_d0cyrliwwuxk': ordernumber,
            'dwfrm_orderstatus_email': email,
            'dwfrm_orderstatus_postal': zipcode,
            'dwfrm_orderstatus_search': 'Applica',
            'csrf_token': cftoken
            }
            
            print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Getting the order!", 'yellow'))
            response = s.post("https://www.aw-lab.com/trackorder-result", headers=trackresultheaders, data=orderPayload, timeout=10).content            
            soup = Bs(response, 'html.parser')

            try:

                checkerVF = soup.find('div', {'class':'b-account'})
                print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Successfully found the order!", 'green'))

                orderstatus1 = soup.find('div', {'class':'b-account-orders__status'}).text
                orderstatus = orderstatus1.replace('\n', '')
            
                if orderstatus == 'Fulfilled and Invoiced':


                    productname1 = soup.find('div', {'class':'b-product__name'}).text
                    productname = productname1.replace('\n', '')
                    
                    tracking = soup.find('a', {'class':'b-account-orders__tracking-link'})['href']
                    
                    price1 = soup.find('td', {'class':'b-order-summary__total-value'}).text
                    price = price1.replace('\n', '')

                    orderdate1 = soup.find('td', {'data-title':'Data'}).text
                    orderdate = orderdate1.replace('\n', '')

                    sku1 = soup.find('div', {'class':'b-product__attribute'}).text
                    sku = sku1.replace('\n', '')
                    
                    itemimage = f'https://www.aw-lab.com/dw/image/v2/BCLG_PRD/on/demandware.static/-/Sites-awlab-master-catalog/default/dw5e715e5a/images/tile/{sku}_0.jpg?sw=727'

                    embed = discord.Embed(title=f"**SUCCESSFULLY CHECKED - {sku}**", color=55552)
                    embed.url = 'https://www.aw-lab.com/trackorder-result'
                    embed.add_field(name='**Order Number**', value=f'||{ordernumber}||', inline=False)
                    embed.add_field(name='**E-mail**', value=f'||{email}||', inline=False)
                    embed.add_field(name='**Zipcode**', value=f'||{zipcode}||', inline=False)
                    embed.add_field(name='**Product name**', value=productname, inline=False)
                    embed.add_field(name='**Price**', value=price, inline=True)
                    embed.add_field(name='**Order date**', value=orderdate, inline=True)
                    embed.add_field(name='**ORDER STATUS**', value=orderstatus, inline=False)
                    embed.add_field(name='**Shipment status**', value=f"[Click here!]({tracking})", inline=False)
                    embed.set_thumbnail(url=itemimage)
                    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
                    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Message successfully sent!", 'blue'))
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                    break

                if orderstatus == 'Return Received':

                    tracking = soup.find('a', {'class':'b-account-orders__tracking-link'})['href']
                    
                    price1 = soup.find('td', {'class':'b-order-summary__total-value'}).text
                    price = price1.replace('\n', '')

                    orderdate1 = soup.find('td', {'data-title':'Data'}).text
                    orderdate = orderdate1.replace('\n', '')

                    embed = discord.Embed(title=f"**SUCCESSFULLY CHECKED**", color=55552)
                    embed.url = 'https://www.aw-lab.com/trackorder-result'
                    embed.add_field(name='**Order Number**', value=f'||{ordernumber}||', inline=False)
                    embed.add_field(name='**E-mail**', value=f'||{email}||', inline=False)
                    embed.add_field(name='**Zipcode**', value=f'||{zipcode}||', inline=False)
                    embed.add_field(name='**Price**', value=price, inline=True)
                    embed.add_field(name='**Order date**', value=orderdate, inline=True)
                    embed.add_field(name='**ORDER STATUS**', value=orderstatus, inline=False)
                    embed.add_field(name='**Shipment status**', value=f"[Click here!]({tracking})", inline=False)
                    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
                    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Message successfully sent!", 'blue'))
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                    break
                if orderstatus == 'Released':
                    
                    price1 = soup.find('td', {'class':'b-order-summary__total-value'}).text
                    price = price1.replace('\n', '')

                    orderdate1 = soup.find('td', {'data-title':'Data'}).text
                    orderdate = orderdate1.replace('\n', '')
                
                    sku1 = soup.find('div', {'class':'b-product__attribute'}).text
                    sku = sku1.replace('\n', '')
                    
                    itemimage = f'https://www.aw-lab.com/dw/image/v2/BCLG_PRD/on/demandware.static/-/Sites-awlab-master-catalog/default/dw5e715e5a/images/tile/{sku}_0.jpg?sw=727'

                    embed = discord.Embed(title=f"**SUCCESSFULLY CHECKED**", color=55552)
                    embed.url = 'https://www.aw-lab.com/trackorder-result'
                    embed.add_field(name='**Order Number**', value=f'||{ordernumber}||', inline=False)
                    embed.add_field(name='**E-mail**', value=f'||{email}||', inline=False)
                    embed.add_field(name='**Zipcode**', value=f'||{zipcode}||', inline=False)
                    embed.add_field(name='**Price**', value=price, inline=True)
                    embed.add_field(name='**Order date**', value=orderdate, inline=True)
                    embed.add_field(name='**ORDER STATUS**', value=orderstatus, inline=False)
                    embed.set_thumbnail(url=itemimage)
                    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
                    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Message successfully sent!", 'blue'))
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                    break

                if orderstatus == 'Cancelled':
                    
                    price1 = soup.find('td', {'class':'b-order-summary__total-value'}).text
                    price = price1.replace('\n', '')

                    orderdate1 = soup.find('td', {'data-title':'Data'}).text
                    orderdate = orderdate1.replace('\n', '')
    
                    embed = discord.Embed(title=f"**SUCCESSFULLY CHECKED**", color=55552)
                    embed.url = 'https://www.aw-lab.com/trackorder-result'
                    embed.add_field(name='**Order Number**', value=f'||{ordernumber}||', inline=False)
                    embed.add_field(name='**E-mail**', value=f'||{email}||', inline=False)
                    embed.add_field(name='**Zipcode**', value=f'||{zipcode}||', inline=False)
                    embed.add_field(name='**Price**', value=price, inline=True)
                    embed.add_field(name='**Order date**', value=orderdate, inline=True)
                    embed.add_field(name='**ORDER STATUS**', value=orderstatus, inline=False)
                    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
                    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Message successfully sent!", 'blue'))
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                    break


                else:

                    embed = discord.Embed(title=f"**ORDER NOT FOUND!**", color=0xFF0000)
                    embed.url = 'https://www.aw-lab.com/trackorder-result'
                    embed.add_field(name='**Order Number**', value=f'||{ordernumber}||', inline=False)
                    embed.add_field(name='**E-mail**', value=f'||{email}||', inline=False)
                    embed.add_field(name='**Zipcode**', value=f'||{zipcode}||', inline=False)
                    embed.add_field(name='**REASON**', value='Order number not found, recheck details or dm APU#0001', inline=False)
                    embed.set_footer(text="Developed by APU", icon_url='https://cdn.discordapp.com/avatars/603138882464382996/d74c8084926e7e40eac508935df61050.png?size=256')
                    print(colored(f"[{datetime.now().strftime('%H:%M:%S')}] - [APUTOOL] - Order not found!", 'red'))
                    embed.timestamp = datetime.utcnow()
                    await ctx.send(embed=embed)
                    break
            
            except:
                print('Error while checking order')

            break
  
        except Exception as e:
            print(f'Error: {str(e)}')


#-------------------------------------------------------------------------------#   


bot.run('put-here-your-token-bot')