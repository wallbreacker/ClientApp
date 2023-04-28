import json

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
import urllib
import requests
from kivy.properties import ObjectProperty
import datetime
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton


# Builder.load_file("my.kv")


class MyLayout(FloatLayout):
    scr_mngr = ObjectProperty(None)

    # def switch_to_invite(self, *args):
    #     self.current = 'invite'
    # Clock.schedule_once(scr_mngr.switch_to_invite, 1.5)

    def check_data_login(self):
        username = self.scr_mngr.enter.username.text
        password = self.scr_mngr.enter.password.text
        res = requests.post('http://192.168.1.139:5000/users', headers={'Content-type': 'application/json'},
                            data=json.dumps({'nickname': username, 'password': password}, ))
        if res.status_code == 200:
            self.scr_mngr.current = 'open_screen'
            time = datetime.datetime.now()
            orderId = str(time)
            res = requests.post('http://192.168.1.139:5000/order', headers={'Content-type': 'application/json'},
                                data=json.dumps({'orderId': orderId, 'nickname': username, 'orderStatus': 0}, ))
            print(res)
        else:
            print("User or password incorrect")

        print(username)
        print(password)


    def start_order(self):
        self.scr_mngr.current = 'main_menu'


    # def add_item_in_cart(self):
    #     self.scr_mngr.current = 'card_baran_okor_bez_kosti'



class AddPanel(BoxLayout):
    pass


class AddCartButton(Button):
    pass


class CartSummLabel(Label):
    pass


# class LogoScreen(Screen):
#     pass


# class CatalogueScreen(Screen):
#     pass


# class InviteScreen(Screen):
# def on_press(self):
#     url = 'http://192.168.0.131:5000/'
#     UrlRequest(url, on_success=self.handle_success, on_error=self.handle_error)
#
# def handle_success(self, request, response):
#     print('Request was successful!')
#     print('Response:', response)
#
# def handle_error(self, request, error):
#     print('Request failed!')
#     print('Error:', error)
# pass

#
# class EnterScreen(Screen):
# def check_data_login(self):
#     nickname = self.my_screen_manager.enter.nickname.text
#     password = self.my_screen_manager.enter.password.text

#     # res = requests.post('http://192.168.0.131:5000/users', headers={'Content-type': 'application/json'},
#     #                      data=json.dumps({'nickname': 'qwert19', 'password': 'qwerty'},))
#     print(req)

# def pressed(self):
# params = urllib.urlencode({'nickname': nickname, 'password': password})
# req = UrlRequest('http://192.168.0.131:5000/users', req_headers={'Content-type': 'application/json'},
#                  req_body=params,
#                  on_success=self.handle_success, on_error=self.handle_error)
#     pass
#
#
# class RegistrationScreen(Screen):
#     pass
#
#
# class UserNotFoundScreen(Screen):
#     pass
#
#
# class MainMenu(Screen):
#     pass
#
#
# class CartScreen(Screen):
#     pass


# class MyScreenManager(ScreenManager):
#     pass


class MainApp(MDApp):
    # sm = MyScreenManager()
    # sm.add_widget(LogoScreen(name="logo"))
    # sm.add_widget(InviteScreen(name="invite"))
    # sm.add_widget(EnterScreen(name="enter"))
    # sm.add_widget(RegistrationScreen(name="registration"))
    # sm.add_widget(UserNotFoundScreen(name="user_not_found"))
    # sm.add_widget(MainMenu(name="main_menu"))
    # sm.add_widget(CartScreen(name="cart_screen"))
    # # sm.add_widget(CatalogueScreen(name='catalogue'))

    def build(self):
        return Builder.load_file('my.kv')


MainApp().run()
