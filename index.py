import os
import re
import random
from tkinter import Tk, Label, Button, Frame, Entry
from PIL import ImageTk, Image
from tkinter.font import Font


from models import Database


database = Database('byron_trade.db')
database.connect()

current_file_path = os.path.abspath(__file__)
image_path = os.path.join(os.path.dirname(current_file_path), 'crypto_trade.jpg')
image_path = re.sub(r"\\", "/", image_path)
image = Image.open(image_path)
image = image.resize((1100, 650), Image.ANTIALIAS)

class ByronTrade(Tk):
    def __init__(self):
        super().__init__()
        self.title('A Crypto Trading Platform by Byron')
        self.geometry('1100x650')
        self.bg_image = ImageTk.PhotoImage(image)
        self.protocol('WM_DELETE_WINDOW', self.on_exit)

        self.bg_label = Label(self, image=self.bg_image)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.assetCheck()
        self.createUI()

    def on_exit(self):
        database.disconnect()
        self.destroy()

    def assetCheck(self):
        database.table_exist('Asset')

        try:
            btc_desc  = "Bitcoin', 'BTC', 'Bitcoin (BTC) is the pioneering decentralized digital currency, introduced in 2009 by an anonymous entity called Satoshi Nakamoto. Operating on a peer-to-peer network, it enables secure value transfers without intermediaries. With a limited supply of 21 million coins, Bitcoin is regarded as a store of value and an alternative investment. As the most prominent cryptocurrency, it influences the broader crypto market and serves as a benchmark for other digital assets. However, its value can be highly volatile, requiring traders to stay informed on market trends."
            eth_desc  = "Ethereum (ETH) is a decentralized blockchain platform introduced in 2015 by Vitalik Buterin. It enables developers to create and deploy smart contracts and decentralized applications (DApps). As the second-largest cryptocurrency by market capitalization, Ethereum has a substantial impact on the blockchain ecosystem. Its native cryptocurrency, Ether (ETH), is used to pay for transactions and execute smart contracts on the platform. Ethereum's versatility and active developer community have made it a crucial player in the world of blockchain technology and decentralized finance (DeFi)."
            usdt_desc = "Tether (USDT) is a stablecoin cryptocurrency introduced in 2014, designed to maintain a stable value by pegging it to fiat currencies like the US Dollar. As one of the most widely used stablecoins, USDT provides a stable store of value and serves as a bridge between cryptocurrencies and traditional financial systems. Its value remains close to $1 USD, making it a popular choice for traders seeking to mitigate price volatility. USDT plays a crucial role in crypto trading, as it allows users to move funds in and out of the crypto market without relying on traditional banking systems."
            xrp_desc  = "XRP is a digital asset and cryptocurrency native to the XRP Ledger, created by Ripple Labs in 2012. As an open-source decentralized platform, XRP aims to facilitate fast and low-cost cross-border transactions. It operates on a unique consensus algorithm, distinguishing it from traditional proof-of-work cryptocurrencies. XRP's primary use case is to serve as a bridge currency for financial institutions and banks, streamlining international remittances and reducing settlement times. With its focus on scalability and efficiency, XRP has become a key player in the world of fintech and blockchain-based solutions."
            bnb_desc  = "BNB (Binance Coin) is the native cryptocurrency of the Binance exchange, one of the largest and most popular cryptocurrency exchanges in the world. Introduced in 2017, BNB operates on the Binance Smart Chain (BSC) and was initially created to facilitate reduced trading fees for Binance users. However, it has evolved into a multi-faceted utility token, powering various use cases within the Binance ecosystem. BNB is used for trading fee discounts, participating in token sales on the Binance Launchpad, and accessing a range of DeFi applications on the BSC network. Its growing adoption and utility have contributed to its significant presence in the crypto space, making it a key player in the crypto exchange and decentralized finance (DeFi) sectors."
            usdc_desc = "USDC (USD Coin) is a stablecoin cryptocurrency launched in 2018 as a joint venture between Circle and Coinbase. Pegged to the US Dollar, USDC offers a stable and secure digital asset, maintaining a 1:1 ratio with USD. As an ERC-20 token on the Ethereum blockchain, USDC enables swift and low-cost transactions within the crypto ecosystem. It has gained widespread adoption in various applications, including trading, lending, and decentralized finance (DeFi) protocols. USDC provides a reliable bridge between traditional financial systems and the world of cryptocurrencies, offering stability and liquidity for users seeking to transact and store value without exposure to price volatility."

            database.insert_data('Asset', (1, 'Bitcoin', 'BTC', btc_desc, 29737.43, 19432993))
            database.insert_data('Asset', (2, 'Ethereum', 'ETH', eth_desc, 1895.45, 120200810))
            database.insert_data('Asset', (3, 'Tether', 'USDT', usdt_desc, 1, 83750478228))
            database.insert_data('Asset', (4, 'XRP', 'XRP', xrp_desc, 0.7654, 52544091958))
            database.insert_data('Asset', (5, 'BNB', 'BNB', bnb_desc, 240.07, 155848363))
            database.insert_data('Asset', (6, 'USD Coin', 'USDC', usdc_desc, 0.9999, 26973502516))
        except Exception as e:
            if str(e) == 'UNIQUE constraint failed: Asset.RANK':
                pass

    def createUI(self):
        # Registration/Login Page
        self.headFont = Font(size=20, weight='bold')  # Increase the font size

        self.frame = Frame(self.bg_label, bg='#302F41')
        self.frame.place(relx=0.5, rely=0.5, anchor='center')

        header = Label(self.frame, text='Welcome to Byron Trade!', font=self.headFont, bg='#302F41', fg='white')  # Apply the custom font
        header.pack()

        register_button = Button(self.frame, text='Create an account', command=self.registerUI, height=2, width=30)
        register_button.pack(side='left')

        login_button = Button(self.frame, text='Login to your account', command=self.loginUI, height=2, width=30)
        login_button.pack(side='left')

    def clearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def generateID(self):
        random_number = random.randint(1, 999999)
        return random_number
    
    def errorUI(self, message):
        pass

    def registerUI(self):
        self.clearFrame()
        
        
        database.table_exist('User')

        def user_create(fname, lname, email, password):
            user_id  = self.generateID()
            fname    = fname.get()
            lname    = lname.get()
            email    = email.get()
            password = password.get()
            database.insert_data("User", (user_id, fname, lname, email, password))

        header = Label(self.frame, text='Registration Form', font=self.headFont, bg='#302F41', fg='white')  # Apply the custom font
        header.pack()

        fname_label = Label(self.frame, text='Enter your First Name:', bg='#302F41', fg='white')
        fname_label.pack()
        fname = Entry(self.frame)
        fname.pack()

        lname_label = Label(self.frame, text='Enter your Last Name:', bg='#302F41', fg='white')
        lname_label.pack()
        lname = Entry(self.frame)
        lname.pack()

        email_label = Label(self.frame, text='Enter your Email Address:', bg='#302F41', fg='white')
        email_label.pack()
        email = Entry(self.frame)
        email.pack()

        password_label = Label(self.frame, text='Enter your Password:', bg='#302F41', fg='white')
        password_label.pack()
        password = Entry(self.frame)
        password.pack()

        label = Label(self.frame, text=" ", height=1, bg='#302F41')
        label.pack()
        submit = Button(self.frame, text='Register', command=lambda: user_create(fname, lname, email, password), height=1, width=30)
        submit.pack()

    def loginUI(self):
        self.clearFrame()

        database.table_exist('User')

        def auth(email, password):
            email    = email.get()
            password = password.get()
            
            if email and password:
                rows = database.select_condition(['Password',], 'User', 'email', email)
                for row in rows:
                    if password == row[0]:
                        self.dashboardUI()
                    else:
                        self.errorUI('Bad Credentials!')
            else:
                self.errorUI('Ensure all fields are filled!')

        header = Label(self.frame, text='Login Form', font=self.headFont, bg='#302F41', fg='white')  # Apply the custom font
        header.pack()

        email_label = Label(self.frame, text='Enter your Email Address:', bg='#302F41', fg='white')
        email_label.pack()
        email = Entry(self.frame)
        email.pack()

        password_label = Label(self.frame, text='Enter your Password:', bg='#302F41', fg='white')
        password_label.pack()
        password = Entry(self.frame)
        password.pack()

        label = Label(self.frame, text="", height=1, bg='#302F41')
        label.pack()
        submit = Button(self.frame, text='Login', command=lambda: auth(email, password), height=1, width=30)
        submit.pack()

    def dashboardUI(self):
        self.clearFrame()

        register_button = Button(self.frame, text='Open an account', command=self.openAccountUI, height=2, width=30)
        register_button.pack()
        label = Label(self.frame, text="", height=1, bg='#302F41')
        label.pack()

        register_button = Button(self.frame, text='Invest', command=self.registerUI, height=2, width=30)
        register_button.pack()
        label = Label(self.frame, text="", height=1, bg='#302F41')
        label.pack()

        register_button = Button(self.frame, text='Portfolio Viewing', command=self.assetListViewUI, height=2, width=30)
        register_button.pack()
        label = Label(self.frame, text="", height=1, bg='#302F41')
        label.pack()

        register_button = Button(self.frame, text='Money in/out', command=self.registerUI, height=2, width=30)
        register_button.pack()

    def assetListViewUI(self):
        self.clearFrame()

        assets_label = Label(self.frame, text='Click Crypto Asset to view information')
        assets_label.pack()

        asset_rows = database.select_data(['RANK', 'NAME', 'SYMBOL', 'PRICE', 'TOTAL_SUPPLY'], 'Asset')
        for row in asset_rows:
            print(row)

    def openAccountUI(self):
        self.clearFrame()
        
        self.frame.configure(width=1100, height=650)

        def createOrRetrieveAccount():
            database.create_table('Account')

        account_info_frame = Frame(self.frame, bg='red')
        account_info_frame.pack(anchor='left')

        account_info_label = Label(account_info_frame, text='Full Name: ')

        sub_frame = Frame(self.frame)
        sub_frame.place(relx=0.5, rely=0.5, anchor='center')


        


if __name__ == '__main__':
    app = ByronTrade()
    app.mainloop()
