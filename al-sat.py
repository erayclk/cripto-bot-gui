import threading
import tkinter
import websocket
import json
import pprint
import talib
import numpy as np
from binance.client import Client
from binance.enums import *
import tkinter as tk
from tkinter import font
import pywhatkit
from datetime import datetime

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
btcSOCKET = "wss://stream.binance.com:9443/ws/btcusdt@kline_1m"
bnbSOCKET = "wss://stream.binance.com:9443/ws/bnbusdt@kline_1m"
xrpSOCKET= "wss://stream.binance.com:9443/ws/xrpusdt@kline_1m"
adaSOCKET= "wss://stream.binance.com:9443/ws/adausdt@kline_1m"
dogeSOCKET= "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"
trxSOCKET= "wss://stream.binance.com:9443/ws/trxusdt@kline_1m"
solSOCKET= "wss://stream.binance.com:9443/ws/solusdt@kline_1m"
ltcSOCKET= "wss://stream.binance.com:9443/ws/ltcusdt@kline_1m"
maticSOCKET= "wss://stream.binance.com:9443/ws/maticusdt@kline_1m"




RSI_PERIOD = 2
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30

TRADE_SYMBOL = "ETHUSD"
TRADE_QUANTITY = 0.01

closes = []
btccloses=[]
bnbcloses=[]
xrpcloses=[]
adacloses=[]
dogecloses=[]
trxcloses=[]
solcloses=[]
ltccloses=[]
maticcloses=[]


def numaraOnay():
    global  numara
    n=telNo.get()
    numara=n
    print(numara)
in_position = False

last_rsi = None  # Son RSI değerini saklamak için değişken
btclast_rsi = None
bnblast_rsi= None
xrplast_rsi=None
adalast_rsi=None
dogelast_rsi=None
trxlast_rsi=None
sollast_rsi=None
ltclast_rsi=None
maticlast_rsi=None

def cc1():
    cc1Sonuc =cc1s.get()

def cc2():
    cc2Sonuc =cc2s.get()
    print(cc2Sonuc)

def cc3():
    cc3Sonuc =cc3s.get()
    print(cc3Sonuc)


def cc4():
    cc4Sonuc =cc4s.get()
    print(cc4Sonuc)


def cc5():
    cc5Sonuc =cc5s.get()
    print(cc5Sonuc)

def cc6():
    cc6Sonuc =cc6s.get()
    print(cc6Sonuc)

def cc7():
    cc7Sonuc =cc7s.get()
    print(cc7Sonuc)

def cc8():
    cc8Sonuc =cc8s.get()
    print(cc8Sonuc)

def cc9():
    cc9Sonuc =cc9s.get()
    print(cc9Sonuc)

def cc10():
    cc10Sonuc =cc10s.get()
    print(cc10Sonuc)

def check_sell_or_buy(last_rsi):
    global in_position
    if last_rsi > RSI_OVERBOUGHT:
        if in_position:
            print("Sat")
            in_position = False
    elif last_rsi < RSI_OVERSOLD:
        if not in_position:
            print("Al")
            in_position = True

def on_open(ws):
    print("Bağlantı kuruldu")

def on_close(ws):
    print("Bağlantı kapatıldı")

def on_message(ws, message):
    global last_rsi, closes
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        closes.append(float(close))
        print(closes)

        if len(closes) >= RSI_PERIOD:
            np_closes = np.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("RSI:", rsi)
            last_rsi = rsi[-1]
            print("Son RSI:", last_rsi)


def btcon_message(btcws, message):
    global btclast_rsi, btccloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        btccloses.append(float(close))
        print(btccloses)

        if len(btccloses) >= RSI_PERIOD:
            np_closes = np.array(btccloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("RSI:", rsi)
            btclast_rsi = rsi[-1]
            print("Son RSI:", btclast_rsi)

def bnbon_message(bnbws, message):
    global bnblast_rsi, bnbcloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        bnbcloses.append(float(close))
        print(bnbcloses)

        if len(bnbcloses) >= RSI_PERIOD:
            np_closes = np.array(bnbcloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("bnb RSI:", rsi)
            bnblast_rsi = rsi[-1]
            print("bnb Son RSI:", bnblast_rsi)


def xrpon_message(xrpws, message):
    global xrplast_rsi, xrpcloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        xrpcloses.append(float(close))
        print(xrpcloses)

        if len(xrpcloses) >= RSI_PERIOD:
            np_closes = np.array(xrpcloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("xrp RSI:", rsi)
            xrplast_rsi = rsi[-1]
            print("xrp Son RSI:", bnblast_rsi)


def adaon_message(adaws, message):
    global adalast_rsi, adacloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        adacloses.append(float(close))
        print(adacloses)

        if len(adacloses) >= RSI_PERIOD:
            np_closes = np.array(adacloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("ada RSI:", rsi)
            adalast_rsi = rsi[-1]
            print("ada Son RSI:", adalast_rsi)

def dogeon_message(dogews, message):
    global dogelast_rsi, dogecloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        dogecloses.append(float(close))
        print(dogecloses)

        if len(dogecloses) >= RSI_PERIOD:
            np_closes = np.array(dogecloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("doge RSI:", rsi)
            dogelast_rsi = rsi[-1]
            print("doge Son RSI:", dogelast_rsi)


def trxon_message(trxws, message):
    global trxlast_rsi, trxcloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        trxcloses.append(float(close))
        print(trxcloses)

        if len(trxcloses) >= RSI_PERIOD:
            np_closes = np.array(trxcloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("trx RSI:", rsi)
            trxlast_rsi = rsi[-1]
            print("trx Son RSI:", trxlast_rsi)

def solon_message(solxws, message):
    global sollast_rsi, solcloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        solcloses.append(float(close))
        print(solcloses)

        if len(solcloses) >= RSI_PERIOD:
            np_closes = np.array(solcloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("sol RSI:", rsi)
            sollast_rsi = rsi[-1]
            print("sol Son RSI:", sollast_rsi)


def ltcon_message(ltcxws, message):
    global ltclast_rsi, ltccloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        ltccloses.append(float(close))
        print(ltccloses)

        if len(ltccloses) >= RSI_PERIOD:
            np_closes = np.array(ltccloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("ltc RSI:", rsi)
            ltclast_rsi = rsi[-1]
            print("ltc Son RSI:", ltclast_rsi)


def maticon_message(maticws, message):
    global maticlast_rsi, maticcloses
    json_message = json.loads(message)
    candle = json_message['k']
    close = candle['c']
    is_candle_closed = candle['x']
    if is_candle_closed:
        print("Kapanmış mum değeri:", close)
        maticcloses.append(float(close))
        print(maticcloses)

        if len(maticcloses) >= RSI_PERIOD:
            np_closes = np.array(ltccloses)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("matic RSI:", rsi)
            maticlast_rsi = rsi[-1]
            print("matic Son RSI:", maticlast_rsi)





def update_gui(window):
    global last_rsi
    if closes:
        btcFiyat.set(str(closes[-1]))
        if last_rsi is not None:
            if last_rsi > 30 and last_rsi < 70:
                ethALSAT.set("İşleme girme")
            elif last_rsi < 30 and last_rsi > 0:
                ethALSAT.set("Satın Al")
            elif last_rsi > 70 and last_rsi < 100:
                ethALSAT.set("Sat!")
            else:
                ethALSAT.set("Hesaplanıyor...")
    if btccloses:
        bbtcFiyat.set(str(btccloses[-1]))
        if btclast_rsi is not None:
            if btclast_rsi > 30 and btclast_rsi < 70:
                btcALSAT.set("İşleme girme")
            elif btclast_rsi < 30 and btclast_rsi > 0:
                btcALSAT.set("Satın Al")
            elif btclast_rsi > 70 and btclast_rsi < 100:
                btcALSAT.set("Sat!")
            else:
                btcALSAT.set("Hesaplanıyor...")

    if bnbcloses:
        bnbFiyat.set(str(bnbcloses[-1]))
        if bnblast_rsi is not None:
            if bnblast_rsi > 30 and bnblast_rsi < 70:
                bnbALSAT.set("İşleme girme")
            elif bnblast_rsi < 30 and bnblast_rsi >= 0:
                bnbALSAT.set("Satın Al")
            elif bnblast_rsi > 70 and bnblast_rsi <= 100:
                bnbALSAT.set("Sat!")
            else:
                bnbALSAT.set("Hesaplanıyor...")

    if xrpcloses:
        xrpFiyat.set(str(xrpcloses[-1]))
        if xrplast_rsi is not None:
            if xrplast_rsi > 30 and xrplast_rsi < 70:
                xrpALSAT.set("İşleme girme")
            elif xrplast_rsi < 30 and xrplast_rsi >= 0:
                xrpALSAT.set("Satın Al")
            elif xrplast_rsi > 70 and xrplast_rsi <= 100:
                xrpALSAT.set("Sat!")
            else:
                xrpALSAT.set("Hesaplanıyor...")
    if adacloses:
        adaFiyat.set(str(adacloses[-1]))
        if adalast_rsi is not None:
            if adalast_rsi > 30 and adalast_rsi < 70:
                adaALSAT.set("İşleme girme")
            elif adalast_rsi < 30 and adalast_rsi >= 0:
                adaALSAT.set("Satın Al")
            elif adalast_rsi > 70 and adalast_rsi <= 100:
                adaALSAT.set("Sat!")
            else:
                adaALSAT.set("Hesaplanıyor...")


    if dogecloses:
        dogeFiyat.set(str(dogecloses[-1]))
        if dogelast_rsi is not None:
            if dogelast_rsi > 30 and dogelast_rsi < 70:
                dogeALSAT.set("İşleme girme")
            elif dogelast_rsi < 30 and dogelast_rsi >= 0:
                dogeALSAT.set("Satın Al")
            elif dogelast_rsi > 70 and dogelast_rsi <= 100:
                dogeALSAT.set("Sat!")
            else:
                dogeALSAT.set("Hesaplanıyor...")

    if trxcloses:
        trxFiyat.set(str(trxcloses[-1]))
        if trxlast_rsi is not None:
            if trxlast_rsi > 30 and trxlast_rsi < 70:
                trxALSAT.set("İşleme girme")
            elif trxlast_rsi < 30 and trxlast_rsi >= 0:
                trxALSAT.set("Satın Al")
            elif trxlast_rsi > 70 and trxlast_rsi <= 100:
                trxALSAT.set("Sat!")
            else:
                trxALSAT.set("Hesaplanıyor...")

    if solcloses:
        solFiyat.set(str(solcloses[-1]))
        if sollast_rsi is not None:
            if sollast_rsi > 30 and sollast_rsi < 70:
                solALSAT.set("İşleme girme")
            elif sollast_rsi < 30 and sollast_rsi >= 0:
                solALSAT.set("Satın Al")
            elif sollast_rsi > 70 and sollast_rsi <= 100:
                solALSAT.set("Sat!")
            else:
                solALSAT.set("Hesaplanıyor...")


    if ltccloses:
        ltcFiyat.set(str(ltccloses[-1]))
        if ltclast_rsi is not None:
            if ltclast_rsi > 30 and ltclast_rsi < 70:
                ltcALSAT.set("İşleme girme")
            elif ltclast_rsi < 30 and ltclast_rsi >= 0:
                ltcALSAT.set("Satın Al")
            elif ltclast_rsi > 70 and ltclast_rsi <= 100:
                ltcALSAT.set("Sat!")
            else:
                ltcALSAT.set("Hesaplanıyor...")


    if maticcloses:
        maticFiyat.set(str(maticcloses[-1]))
        if maticlast_rsi is not None:
            if maticlast_rsi > 30 and maticlast_rsi < 70:
                maticALSAT.set("İşleme girme")
            elif maticlast_rsi < 30 and maticlast_rsi >= 0:
                maticALSAT.set("Satın Al")
            elif maticlast_rsi > 70 and maticlast_rsi <= 100:
                maticALSAT.set("Sat!")
            else:
                maticALSAT.set("Hesaplanıyor...")

    cc1Sonuc = cc1s.get()
    if cc1Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if ethALSAT == "İşleme girme":
            pass
        elif ethALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "eth al", saat, dakika)
        elif ethALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "eth sat", saat, dakika)

    cc2Sonuc = cc2s.get()
    if cc2Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if btcALSAT == "İşleme girme":
            pass
        elif btcALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "btc al", saat, dakika)
        elif btcALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "btc sat", saat, dakika)

    cc3Sonuc = cc3s.get()
    if cc3Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if bnbALSAT == "İşleme girme":
            pass
        elif bnbALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "bnb al", saat, dakika)
        elif bnbALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "bnb sat", saat, dakika)

    cc4Sonuc = cc4s.get()
    if cc4Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if xrpALSAT == "İşleme girme":
            pass
        elif xrpALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "xrp al", saat, dakika)
        elif xrpALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "xrp sat", saat, dakika)

    cc5Sonuc = cc5s.get()
    if cc5Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if adaALSAT == "İşleme girme":
            pass
        elif adaALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "xrp al", saat, dakika)
        elif adaALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "xrp sat", saat, dakika)

    cc6Sonuc = cc6s.get()
    if cc6Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if dogeALSAT == "İşleme girme":
            pass
        elif dogeALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "doge al", saat, dakika)
        elif dogeALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "doge sat", saat, dakika)

    cc7Sonuc = cc7s.get()
    if cc7Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if trxALSAT == "İşleme girme":
            pass
        elif trxALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "trx al", saat, dakika)
        elif trxALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "trx sat", saat, dakika)

    cc8Sonuc = cc8s.get()
    if cc8Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if solALSAT == "İşleme girme":
            pass
        elif solALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "sol al", saat, dakika)
        elif solALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "sol sat", saat, dakika)

    cc9Sonuc = cc9s.get()
    if cc9Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if ltcALSAT == "İşleme girme":
            pass
        elif ltcALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "ltc al", saat, dakika)
        elif ltcALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "ltc sat", saat, dakika)

    cc10Sonuc = cc10s.get()
    if cc10Sonuc:
        now = datetime.now()
        saat = now.hour
        dakika = now.minute + 1

        if maticALSAT == "İşleme girme":
            pass
        elif maticALSAT.get() == "Satın Al":
            pywhatkit.sendwhatmsg(numara, "matic al", saat, dakika)
        elif maticALSAT.get() == "Sat!":
            pywhatkit.sendwhatmsg(numara, "matic sat", saat, dakika)
    window.after(1000, update_gui, window)

def run_bot():
    ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
    ws.run_forever()

def btcrun_bot():
    btcws = websocket.WebSocketApp(btcSOCKET, on_open=on_open, on_close=on_close, on_message=btcon_message)
    btcws.run_forever()

def bnbrun_bot():
    bnbws=websocket.WebSocketApp(bnbSOCKET, on_open=on_open, on_close=on_close, on_message=bnbon_message)
    bnbws.run_forever()

def xrprun_bot():
    xrpws = websocket.WebSocketApp(xrpSOCKET, on_open=on_open, on_close=on_close, on_message=xrpon_message)
    xrpws.run_forever()

def adarun_bot():
    adaws = websocket.WebSocketApp(adaSOCKET, on_open=on_open, on_close=on_close, on_message=adaon_message)
    adaws.run_forever()

def dogerun_bot():
    adaws = websocket.WebSocketApp(dogeSOCKET, on_open=on_open, on_close=on_close, on_message=dogeon_message)
    adaws.run_forever()

def trxrun_bot():
    trxws = websocket.WebSocketApp(trxSOCKET, on_open=on_open, on_close=on_close, on_message=trxon_message)
    trxws.run_forever()

def solrun_bot():
    solws = websocket.WebSocketApp(solSOCKET, on_open=on_open, on_close=on_close, on_message=solon_message)
    solws.run_forever()

def ltcrun_bot():
    ltcws = websocket.WebSocketApp(ltcSOCKET, on_open=on_open, on_close=on_close, on_message=ltcon_message)
    ltcws.run_forever()


def maticrun_bot():
    maticws = websocket.WebSocketApp(maticSOCKET, on_open=on_open, on_close=on_close, on_message=maticon_message)
    maticws.run_forever()

def run_gui():
    global btcFiyat, ethALSAT ,bbtcFiyat,btcALSAT,bnbFiyat,bnbALSAT,xrpFiyat,xrpALSAT,adaFiyat,adaALSAT,dogeFiyat,dogeALSAT,trxFiyat,trxALSAT,solFiyat,solALSAT,ltcFiyat,ltcALSAT,maticALSAT,maticFiyat
    global cc1s,cc2s,cc3s,cc4s,cc5s,cc6s,cc7s,cc8s,cc9s,cc10s,telNo
    window = tk.Tk()
    window.title("Crypto Bot")
    window.geometry("650x623")

    frame1 = tk.Frame(window, bg="red", height=175, width=950)

    foto = tk.PhotoImage(file="template.gif")
    etiket1 = tk.Label(window, image=foto)
    etiket1.place(x=-1, y=0)

    entry_font = font.Font(family="Arial", size=20)
    telNo = tk.Entry(window, width=25, font=entry_font)
    telNo.place(x=95, y=50)

    telNObuton=tkinter.Button(text="✓",command=numaraOnay)
    telNObuton.place(x=555,y=50)


    cc1s=tkinter.BooleanVar()
    c1 = tk.Checkbutton(window, text='ETH', font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc1s,command=cc1)
    c1.place(x=0, y=175)

    btcFiyat = tk.StringVar()
    btcEtiketFiyat = tk.Label(window, textvariable=btcFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    btcEtiketFiyat.place(x=150, y=175)

    ethALSAT = tk.StringVar()
    ethEtiketALSAT = tkinter.Label(window, textvariable=ethALSAT, font=("Arial", 20), relief=tk.GROOVE)
    ethEtiketALSAT.place(x=450, y=175)

    cc2s = tkinter.BooleanVar()
    c2=tk.Checkbutton(window,text="BTC",font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc2s,command=cc2)
    c2.place(x=0,y=220)

    bbtcFiyat=tk.StringVar()
    bbtcEtiketFiyat = tk.Label(window, textvariable=bbtcFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    bbtcEtiketFiyat.place(x=150, y=220)

    btcALSAT = tk.StringVar()
    btcEtiketALSAT = tkinter.Label(window, textvariable=btcALSAT, font=("Arial", 20), relief=tk.GROOVE)
    btcEtiketALSAT.place(x=450, y=220)


    cc3s = tkinter.BooleanVar()
    c3 = tk.Checkbutton(window, text="BNB", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc3s,command=cc3)
    c3.place(x=0, y=265)

    bnbFiyat = tk.StringVar()
    bnbEtiketFiyat = tk.Label(window, textvariable=bnbFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    bnbEtiketFiyat.place(x=150, y=265)

    bnbALSAT = tk.StringVar()
    bnbEtiketALSAT = tkinter.Label(window, textvariable=bnbALSAT, font=("Arial", 20), relief=tk.GROOVE)
    bnbEtiketALSAT.place(x=450, y=265)

    cc4s = tkinter.BooleanVar()
    c4 = tk.Checkbutton(window, text="XRP", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc4s,command=cc4)
    c4.place(x=0, y=305)

    xrpFiyat =tk.StringVar()
    xrpEtiketFiyat = tk.Label(window, textvariable=xrpFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    xrpEtiketFiyat.place(x=150, y=305)

    xrpALSAT = tk.StringVar()
    xrpEtiketALSAT = tkinter.Label(window, textvariable=xrpALSAT, font=("Arial", 20), relief=tk.GROOVE)
    xrpEtiketALSAT.place(x=450, y=305)

    cc5s = tkinter.BooleanVar()
    c5 = tk.Checkbutton(window, text="ADA", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc5s,command=cc5)
    c5.place(x=0, y=350)

    adaFiyat = tk.StringVar()
    adaEtiketFiyat = tk.Label(window, textvariable=adaFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    adaEtiketFiyat.place(x=150, y=350)

    adaALSAT = tk.StringVar()
    adaEtiketALSAT = tkinter.Label(window, textvariable=adaALSAT, font=("Arial", 20), relief=tk.GROOVE)
    adaEtiketALSAT.place(x=450, y=350)

    cc6s = tkinter.BooleanVar()
    c6 = tk.Checkbutton(window, text="DOGE", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc6s,command=cc6)
    c6.place(x=0, y=395)

    dogeFiyat = tk.StringVar()
    dogeEtiketFiyat = tk.Label(window, textvariable=dogeFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    dogeEtiketFiyat.place(x=150, y=395)

    dogeALSAT = tk.StringVar()
    dogeEtiketALSAT = tkinter.Label(window, textvariable=dogeALSAT, font=("Arial", 20), relief=tk.GROOVE)
    dogeEtiketALSAT.place(x=450, y=395)


    cc7s = tkinter.BooleanVar()
    c7 = tk.Checkbutton(window, text="TRX", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc7s,command=cc7)
    c7.place(x=0, y=440)

    trxFiyat = tk.StringVar()
    trxEtiketFiyat = tk.Label(window, textvariable=trxFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    trxEtiketFiyat.place(x=150, y=440)

    trxALSAT = tk.StringVar()
    trxEtiketALSAT = tkinter.Label(window, textvariable=trxALSAT, font=("Arial", 20), relief=tk.GROOVE)
    trxEtiketALSAT.place(x=450, y=440)

    cc8s = tkinter.BooleanVar()
    c8 = tk.Checkbutton(window, text="SOL", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc8s,command=cc8)
    c8.place(x=0, y=485)

    solFiyat = tk.StringVar()
    solEtiketFiyat = tk.Label(window, textvariable=solFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    solEtiketFiyat.place(x=150, y=485)

    solALSAT = tk.StringVar()
    solEtiketALSAT = tkinter.Label(window, textvariable=solALSAT, font=("Arial", 20), relief=tk.GROOVE)
    solEtiketALSAT.place(x=450, y=485)

    cc9s = tkinter.BooleanVar()
    c9 = tk.Checkbutton(window, text="LTC", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc9s,command=cc9)
    c9.place(x=0, y=530)

    ltcFiyat = tk.StringVar()
    ltcEtiketFiyat = tk.Label(window, textvariable=ltcFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    ltcEtiketFiyat.place(x=150, y=530)

    ltcALSAT = tk.StringVar()
    ltcEtiketALSAT = tkinter.Label(window, textvariable=ltcALSAT, font=("Arial", 20), relief=tk.GROOVE)
    ltcEtiketALSAT.place(x=450, y=530)

    cc10s = tkinter.BooleanVar()
    c10 = tk.Checkbutton(window, text="MATIC", font=("Arial", 20), height=1, width=6, relief=tk.GROOVE,variable=cc10s,command=cc10)
    c10.place(x=0, y=575)

    maticFiyat = tk.StringVar()
    maticEtiketFiyat = tk.Label(window, textvariable=maticFiyat, font=("Arial", 20), relief=tk.GROOVE, height=1, width=16)
    maticEtiketFiyat.place(x=150, y=575)

    maticALSAT = tk.StringVar()
    maticEtiketALSAT = tkinter.Label(window, textvariable=maticALSAT, font=("Arial", 20), relief=tk.GROOVE)
    maticEtiketALSAT.place(x=450, y=575)




    update_gui(window)  # GUI'nin güncellenmesini başlat

    window.mainloop()





bot_thread = threading.Thread(target=run_bot)
btcbot_thread=threading.Thread(target=btcrun_bot)
bnbbot_thread=threading.Thread(target=bnbrun_bot)
xrpbot_thread=threading.Thread(target=xrprun_bot)
adabot_thread=threading.Thread(target=adarun_bot)
dogebot_thread=threading.Thread(target=dogerun_bot)
trxbot_thread=threading.Thread(target=trxrun_bot)
solbot_thread=threading.Thread(target=solrun_bot)
ltcbot_thread=threading.Thread(target=ltcrun_bot)
maticbot_thread=threading.Thread(target=maticrun_bot)


gui_thread = threading.Thread(target=run_gui)


bot_thread.start()
btcbot_thread.start()
bnbbot_thread.start()
xrpbot_thread.start()
adabot_thread.start()
dogebot_thread.start()
trxbot_thread.start()
solbot_thread.start()
ltcbot_thread.start()
maticbot_thread.start()



gui_thread.start()
