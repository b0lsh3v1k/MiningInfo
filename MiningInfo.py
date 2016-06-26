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


        #INTERFACE
        print "[+]------------------------- MINING STATISTICS by b0lsh3v1k -------------------------[+]\n"
        print "[POOL]\n"
        print "     Hashrate: " + str(Hashrate) + " MH/s"
        print "     Unpaid Balance: 0." + str(("{0:.0f}".format(UnpaidBalance))) + " ETH" #Limited to 18 decimals
        print "     Estimated monthly earnings: " + str(EarningsMonth) + " $"
        print "\n[ETHER]\n"
        print "     Ether Price: " + str(EtherPrice) + " $"
        print ("     Ether Market Capita: ${:,.2f}".format(EtherMarketCap)) + " $" #commas every 3 digits for better reading
        print "\n[BITCOIN]\n"
        print "     Bitcoin Price: " + str(BitcoinPrice) + " $"
        print "\n[+]----------------------------------------------------------------------------------[+]"
    except:
        print "[+]------------------------- MINING STATISTICS by b0lsh3v1k -------------------------[+]\n"
        print "[POOL]\n"
        print "     Hashrate: " + "[MINER DISCONNECTED]"
        print "     Unpaid Balance: 0." + str(("{0:.0f}".format(UnpaidBalance))) + " ETH" #Limited to 18 decimals
        print "     Estimated monthly earnings: " + str(EarningsMonth) + " $"
        print "\n[ETHER]\n"
        print "     Ether Price: " + str(EtherPrice) + " $"
        print ("     Ether Market Capita: ${:,.2f}".format(EtherMarketCap)) + " $" #commas every 3 digits for better reading
        print "\n[BITCOIN]\n"
        print "     Bitcoin Price: " + str(BitcoinPrice) + " $"
        print "\n[+]----------------------------------------------------------------------------------[+]"


while True:
    time.sleep(15) #15s updates
    main()
