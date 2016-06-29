#! /usr/bin/env python
#encoding: utf-8

import requests
import os
import time

def main():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    try:
        HashrateData = requests.get("https://ethermine.org/api/miner/8B283ba96C1c6F1fb94789a43F33053D59952EEA")
        HashrateDataTXT = HashrateData.text
        HashrateStart = r'''"reportedHashRate":"'''
        HashrateEnd = r''' MH/s"'''
        Hashrate = float((HashrateDataTXT.split(HashrateStart))[1].split(HashrateEnd)[0])

        UnpaidBalanceStart = '''"unpaid":'''
        UnpaidBalanceEnd = ''',"activeWorkers":1'''
        UnpaidBalance = float((HashrateDataTXT.split(UnpaidBalanceStart))[1].split(UnpaidBalanceEnd)[0])

        EtherPriceData = requests.get("https://coinmarketcap-nexuist.rhcloud.com/api/eth")
        EtherPriceDataTXT = EtherPriceData.text
        EtherPriceStart = r'''{"usd":'''
        EtherPriceEnd = r''',"eur":'''
        EtherMarketCap = float((EtherPriceDataTXT.split(EtherPriceStart))[1].split(EtherPriceEnd)[0])
        EtherPrice = float((EtherPriceDataTXT.split(EtherPriceStart))[2].split(EtherPriceEnd)[0])

        BitcoinPriceData = requests.get("https://api.bitcoinaverage.com/exchanges/USD")
        BitcoinPriceDataTXT = BitcoinPriceData.text
        BitcoinPriceStart = r'''"ask": '''
        BitcoinPriceEnd = r''','''
        BitcoinPrice = float((BitcoinPriceDataTXT.split(BitcoinPriceStart))[1].split(BitcoinPriceEnd)[0])

        ETHperMH = 0.2312074866310160427807486631016
        EarningsMonth = (ETHperMH * Hashrate) * EtherPrice
        Unpaidformatted = str(("{0:.0f}".format(UnpaidBalance)))
        UnpaidUSD = EtherPrice * float(Unpaidformatted)

        #Wallets
        Wallet1Data = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=0x8B283ba96C1c6F1fb94789a43F33053D59952EEA&tag=latest&apikey=GNMNHGPQBXXT5VA2R47QZ7ZINSQNWD8AV9")
        Wallet1DataTXT = Wallet1Data.text
        Wallet1Start = '''"result":"'''
        Wallet1End = '''"}'''
        Wallet1Ammount = float((Wallet1DataTXT.split(Wallet1Start))[1].split(Wallet1End)[0])
        Wallet1AmmountB = str(Wallet1Ammount)[0:10] #10 digits
        Wallet1AmmountC = float(Wallet1AmmountB) * 10
        Wallet1USD = float(Wallet1AmmountC) * EtherPrice

        Wallet2Data = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=0x769F2177A1dcE05b120A8409Ab8D70d19E8Ab9bC&tag=latest&apikey=GNMNHGPQBXXT5VA2R47QZ7ZINSQNWD8AV9")
        Wallet2DataTXT = Wallet2Data.text
        Wallet2Start = '''"result":"'''
        Wallet2End = '''"}'''
        Wallet2Ammount = float((Wallet2DataTXT.split(Wallet2Start))[1].split(Wallet2End)[0])
        Wallet2AmmountB = str(Wallet2Ammount)[0:10] #10 digits
        Wallet2AmmountC = float(Wallet2AmmountB) * 10
        Wallet2USD = float(Wallet2AmmountC) * EtherPrice



        #INTERFACE
        print "[+]------------------------- MINING INFORMATION by b0lsh3v1k -------------------------[+]\n"
        print "[POOL]\n"
        print "     Hashrate: " + str(Hashrate) + " MH/s"
        print "     Unpaid Balance: 0." + Unpaidformatted + " ETH ("  + str(UnpaidUSD)[0:8] + " $)" #Limited to 18 decimals ETH and 8 digits USD
        print "     Estimated monthly earnings: " + str(EarningsMonth)[0:8] + " $"
        print "\n[ETHER]\n"
        print "     Ether Price: " + str(EtherPrice) + " $"
        print "     Wallet [1] ammount: " + str(Wallet1AmmountC) + " ETH (" + str(Wallet1USD)[0:8] + " $)"
        print "     Wallet [2] ammount: " + str(Wallet2AmmountC) + " ETH (" + str(Wallet2USD)[0:8] + " $)"
        print ("     Ether Market Capita: ${:,.2f}".format(EtherMarketCap)) + " $" #commas every 3 digits for better reading
        print "\n[BITCOIN]\n"
        print "     Bitcoin Price: " + str(BitcoinPrice) + " $"
        print "\n[+]-----------------------------------------------------------------------------------[+]"
    except:
        print "[+]------------------------- MINING INFORMATION by b0lsh3v1k -------------------------[+]\n"
        print "[POOL]\n"
        print "     [MINER DISCONNECTED]"
        print "\n[ETHER]\n"
        print "     Ether Price: " + str(EtherPrice) + " $"
        print "     Wallet [1] ammount: " + str(Wallet1AmmountC) + " ETH (" + str(Wallet1USD)[0:8] + " $)"
        print "     Wallet [2] ammount: " + str(Wallet2AmmountC) + " ETH (" + str(Wallet2USD)[0:8] + " $)"
        print ("     Ether Market Capita: ${:,.2f}".format(EtherMarketCap)) + " $" #commas every 3 digits for better reading
        print "\n[BITCOIN]\n"
        print "     Bitcoin Price: " + str(BitcoinPrice) + " $"
        print "\n[+]-----------------------------------------------------------------------------------[+]"

main()
while True:
    time.sleep(15) #15s updates
    main()
