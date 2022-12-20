# Carregar Libs
import os
import sys

absolute_path = os.path.abspath(__file__+"/../Lib/site-packages")
sys.path.insert(0, absolute_path)

import requests
from bs4 import BeautifulSoup
import csv

# VARIAVEIS
dataF=[]
count=0
frases=["PARA ZERAR O ESTOQUE!!","SUPER OFERTA!!","O MELHOR PREÇO DO MERCADO!!","DESCONTOS IMPERDÍVEIS!!"]


# INPUT TXT
try:
    with open('urls.txt') as f:
        urls = f.readlines()
except:
    input("Problema com arquivo urls.txt, favor verificar\n Clique enter para sair")

for i in range(len(urls)):
    urls[i]=urls[i].replace('\n','').replace(',','')

burp0_headers = {"Cache-Control": "max-age=0", "Sec-Ch-Ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Windows\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Service-Worker-Navigation-Preload": "true", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
burp0_cookies = {"VtexWorkspace": "master%3A-", "vtex_segment": "eyJjYW1wYWlnbnMiOm51bGwsImNoYW5uZWwiOiIxIiwicHJpY2VUYWJsZXMiOm51bGwsInJlZ2lvbklkIjpudWxsLCJ1dG1fY2FtcGFpZ24iOm51bGwsInV0bV9zb3VyY2UiOm51bGwsInV0bWlfY2FtcGFpZ24iOm51bGwsImN1cnJlbmN5Q29kZSI6IkJSTCIsImN1cnJlbmN5U3ltYm9sIjoiUiQiLCJjb3VudHJ5Q29kZSI6IkJSQSIsImN1bHR1cmVJbmZvIjoicHQtQlIiLCJjaGFubmVsUHJpdmFjeSI6InB1YmxpYyJ9", "_gcl_au": "1.1.1710445001.1670958650", "VtexRCSessionIdv7": "f850df4d-f396-4c05-9386-cf509cd39f8b", "_hjFirstSeen": "1", "_hjIncludedInSessionSample": "1", "_hjSession_3081151": "eyJpZCI6Ijg5ODMwMjU5LTBmNjItNGNkZC04YTc1LWQ3NzJmYzc4MDQ0NyIsImNyZWF0ZWQiOjE2NzA5NTg2NTE4MzIsImluU2FtcGxlIjp0cnVlfQ==", "_hjIncludedInPageviewSample": "1", "_hjAbsoluteSessionInProgress": "0", "_gid": "GA1.3.1129376679.1670958652", "_fbp": "fb.2.1670958652703.1680458679", "vtex_binding_address": "casaevideonewio.myvtex.com/", "checkout.vtex.com": "__ofid=9db2ca31649c4610b8f58d485741ec7f", "VtexRCMacIdv7": "59808115-9a30-46f6-b51c-da1b32ba9f5f", "_tt_enable_cookie": "1", "_ttp": "YFcKF6CNQwZaTd1s2_q0n32PKBT", "_pm_id": "601481670958654041", "_pm_sid": "613441670958654042", ".ASPXAUTH": "3C91D0AE719FDBA3945960569CA3B2F5EDD6B97FE54A595AF902520A1A2B223DE819172946841B54B7391ECCA8E123687DCC378058C0826142717EA847FD596EB963A8713062B37987ACC732470FAF2E10E219E51583584564F2C44058D6BCB7DCD4DCA9984CACEC5F870F7E7C349D9CA64901DEFD46733FFAAE7AEBC38D88CCCEC0668A8380EDED55F8A546038C9DE77F5A3CBE2618619E0725E87DB07BA4E0222C68F7", "mmapi.p.bid": "%22prodphxcgus02%22", "mmapi.p.srv": "%22prodphxcgus02%22", "_clck": "1xrrj3u|1|f7d|0", "nav_id": "8d341afa-af9a-449c-a215-82a71c3ac3b6", "voxusmediamanager_id": "16709586603500.5396189691842159yqg60v2min", "legacy_p": "8d341afa-af9a-449c-a215-82a71c3ac3b6", "chaordic_browserId": "8d341afa-af9a-449c-a215-82a71c3ac3b6", "legacy_c": "8d341afa-af9a-449c-a215-82a71c3ac3b6", "legacy_s": "8d341afa-af9a-449c-a215-82a71c3ac3b6", "_lr_uf_-r6s12a": "953034ce-7f8d-405b-9ffe-f2ad89cd7638", "__kdtv": "t%3D1670958661167%3Bi%3D5a00bbc55dc345589877893f592c6139cd8a5019", "_kdt": "%7B%22t%22%3A1670958661167%2C%22i%22%3A%225a00bbc55dc345589877893f592c6139cd8a5019%22%7D", "voxusmediamanager_acs": "true", "vtex_session": "eyJhbGciOiJFUzI1NiIsImtpZCI6IjFCQzkwMTBCQjhCMjg1OUQ5QTdDNDFFQTA5NUExNzA4MzNGNERBQkEiLCJ0eXAiOiJqd3QifQ.eyJhY2NvdW50LmlkIjoiYTE0YTUxM2QtYTI5Yy00YWU3LWJmMmItOTVmM2M4MWRkNzVmIiwiaWQiOiJlM2E4ODQ4MS1iOTZkLTQ2ZmYtYjAwOC0yZjQ0MGEzMjU5NDMiLCJ2ZXJzaW9uIjozLCJzdWIiOiJzZXNzaW9uIiwiYWNjb3VudCI6InNlc3Npb24iLCJleHAiOjE2NzE2NDk5MDYsImlhdCI6MTY3MDk1ODcwNiwiaXNzIjoidG9rZW4tZW1pdHRlciIsImp0aSI6ImIxYTg2OTJlLTNkZmItNDZkNS05NDQ1LWQwMzFkZjliZGVkYiJ9.R_jny-2gLfVOdTYb4r0FaBu4ZwqRLpn_irV5Tnp_L3Gvs5XnOobj3AGQWMNXRnNhGhOSfbqNCrDhCOdaEnaSWA", "_hjSessionUser_3081151": "eyJpZCI6ImVkNTQ5ZGY5LTZlMzItNTRiNy1iMTlmLTE0OTM1MTI2YmNmMSIsImNyZWF0ZWQiOjE2NzA5NTg2NTE4MTYsImV4aXN0aW5nIjp0cnVlfQ==", "_ga": "GA1.3.651995566.1670958652", "_gat_UA-2290799-3": "1", "_ga_91WN04T3MY": "GS1.1.1670958656.1.1.1670958721.58.0.0", "_ga_8TBCGMN516": "GS1.1.1670958656.1.1.1670958721.58.0.0", "_uetsid": "dcd612a07b1911ed918479f69ffb4899", "_uetvid": "dcd66c007b1911edb95c7f1d98729b93", "cto_bundle": "bUn2Ul9hNmJyN1dPZHBwJTJCRkZwUnRodmQyOUJwYjNETk9PNlRoZnlLJTJCWDNtZXZZJTJCTHMwJTJGMWtsejJlc1BIbU5FZGlheWpnZXNWSFdzd20zdVUyY0RocnRQWElJVkxuUWhpJTJGQ0lSMFZCejVTblIwR0lqJTJCRDhvc2R0Sm1kd04lMkJYWW03cnZYQzUlMkJoNk1BRHRiWXg2RHFVbjI3MWlKaFNINzNFSUxKQ2F2TXg5TVFVN2dRJTNE", "mmapi.p.pd": "%222EQQyMn_-mmEoG17fuJkHRig3Qbl7HoM8fDsSXaJruA%3D%7CAwAAAApDH4sIAAAAAAAEAGNheHnOQ_-gmAsnA3NBRgWjEAOjE8O_TS2qjAzhW-xf2d695bGf5dAhEM0ABP-hgIHNJbMoNbmE8aAYI0gcDGCSIBoqxOgKAICU9OphAAAA%22", "_lr_tabs_-r6s12a%2Fcasavideo": "{%22sessionID%22:0%2C%22recordingID%22:%225-5cbf8b11-e36b-462a-b98a-af6ee45527d7%22%2C%22lastActivity%22:1670958721917}", "_lr_hb_-r6s12a%2Fcasavideo": "{%22heartbeat%22:1670958721917}", "_clsk": "wleta7|1670958722047|3|1|l.clarity.ms/collect"}

f=0
for url in urls:
    # GET INFOS PRODUTO
    r=requests.get(url, headers=burp0_headers, cookies=burp0_cookies)
    soup = BeautifulSoup(r.text, 'html.parser')

    # NOME
    nome=soup.find(class_='vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--quickview').get_text()
    # SEM DESCONTO
    try:
        preco1=soup.find(class_='vtex-product-price-1-x-currencyContainer vtex-product-price-1-x-currencyContainer--prices').get_text()
    except:
        preco1=0

    # COM DESCONTO / Final
    preco2=soup.find(class_='vtex-product-price-1-x-installmentsTotalValue').get_text()
    
    

    data=[nome,preco1,preco2]
    # Contador Frases
    if f==4:
        f=0

    # OUTPUT 
    # FRASE + PRECO1
    print(frases[f],"\n\n"+data[0]) 
    f+=1   
    # PRECO 2
    if preco1!=0:
        print("\n\nDe:",preco1,"\nPor:",preco2)
    else:
        print("\n\nPor:",preco2)

    # Convert Link to YBox Link
    login_url = "https://springmedia.hasoffers.com:443/offers/ajax_generate_link/3912/2110?params=%7B%22url%22%3A%22"+url+"%22%7D&options=%7B%7D"
    login_cookies = {"PHPSESSID": "e25a648a79e8558de08d8737fed4671d", "EUcomp": "1", "swidth": "1920", "_ga": "GA1.3.793853560.1670960449", "_gid": "GA1.3.1763759985.1670960449", "__zlcmid": "1DPlRooSlzxOhci", "_dd_s": "logs=1&id=d39a459f-5a79-4d3b-902b-f90ba63ae2ef&created=1670960447303&expire=9999999999999"}
    login_headers = {"Sec-Ch-Ua": "\"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Sec-Ch-Ua-Mobile": "?0", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.63 Safari/537.36", "Sec-Ch-Ua-Platform": "\"Windows\"", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Referer": "https://springmedia.hasoffers.com/admin/offers/view/3912", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}
    import json
    urlnew=requests.get(login_url, headers=login_headers, cookies=login_cookies).text    
    urljson = json.loads(urlnew)
    urlybox=[urljson['click_url']]

    # Convert Ybox Link to Bitly Link
    import bitlyshortener
    token=['e78e9c13c376bed962b5d6de4a065e0864a0f03f']
    shortener = bitlyshortener.Shortener(tokens=token, max_cache_size=256)
    urlbitly=shortener.shorten_urls(urlybox)

    # Print Final Link Bitly
    print("\n\nLink:",urlbitly[0])

    print("#############################################")
    # Loop + Contador
    count+=1

fim=input("Finalizado Clique enter para sair")


