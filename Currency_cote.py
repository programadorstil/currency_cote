'''This is a simple example application created by me using kivyMD, using the requests API
with response to currency quote, with text input and click action button.
'''
import requests
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField


class CurrencyApp(MDApp):
    def build(self):

        # returns a window object with all it's widgets
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        # image widget, copied from the website https://icons8.com/icons/set/money for example
        # image for 96x96 for example
        self.window.add_widget(Image(source="icons8-money-yours-96.png"))

        #
        self.greeting = MDLabel(
            text="Enter which currency you want to see the quote\n\nOptions EUR,USD or BTC for BRL",
            font_size=18,
            color='#00FFCE'
        )
        self.window.add_widget(self.greeting)

        # text input widget
        self.user = MDTextField(
            multiline=False,
            size_hint=(1, 0.5)
        )

        self.window.add_widget(self.user)

        # button widget
        self.button = MDRectangleFlatButton(
            text="OK",
            theme_text_color = "Custom",
            text_color = "blue",
            line_color = "blue",
            size_hint=(1, 0.5)
            # remove darker overlay of background colour
            # background_normal = ""
        )
        self.button.bind(on_press=self.event_of_button)
        self.window.add_widget(self.button)

        return self.window




    def event_of_button(self, txt):
        txt = self.user.text

        requisicao = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

        requisicao_dic = requisicao.json()
        cotacao_dolar = requisicao_dic['USDBRL']['bid']
        cotacao_euro = requisicao_dic['EURBRL']['bid']
        cotacao_btc = requisicao_dic['BTCBRL']['bid']




        if txt == "usd" or txt == "USD":
            self.greeting.text = " The current quotation of  " + txt + " is  R$ "+ cotacao_dolar
        elif txt == "eur" or txt == "EUR":
            self.greeting.text = " The current quotation of  " + txt + " is  R$ "+ cotacao_euro
        elif txt == "btc" or txt == "BTC":
            self.greeting.text = " The current quotation of  " + txt + " is  R$ "+ cotacao_btc
        else:
            print("opcao invalida")
            self.dialog = MDDialog(text = "Invalid option! try writing USD,EUR or BTC")
            self.dialog.open()
        # muda o texto para a cotação escolhida"
        #self.greeting.text = " the current price of  " + txt + " é  xxxxxx"



# run  App Class
CurrencyApp().run()