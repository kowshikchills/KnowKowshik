import requests
import json
import configparser as cfg
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, CallbackQuery

class telegram_chatbot():
    
    def __init__(self, config):
        self.token = self.read_token_from_config_file(config)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, offset=None):
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset + 1)
        r = requests.get(url)
        return json.loads(r.content)
    
    def send_message(self, msg, chat_id):
        url = self.base + "sendMessage?chat_id={}&text={}&parse_mode=html".format(chat_id, msg)
        if msg is not None:
            requests.get(url)
            
    def send_photo(self, link, caption, chat_id):
        url = self.base + "sendPhoto?chat_id={}&caption={}".format(chat_id, caption)
        file = {'photo': open(link,'rb')}
        if file is not None:
            requests.post(url,files=file)
            
    def send_document(self, link, caption, chat_id):
        url = self.base + "sendDocument?chat_id={}&caption={}".format(chat_id, caption)
        file = {'document': open(link,'rb')}
        if file is not None:
            requests.post(url,files=file)
            
    def send_question(self, text, buttons, chat_id):
        url = self.base + "sendMessage"
        keyboard_ = [InlineKeyboardButton(i[0], callback_data=i[1]) for i in buttons]
        keyboard = [keyboard_[i:i + 2] for i in range(0, len(buttons), 2)][::-1]     
        reply_markup = InlineKeyboardMarkup(keyboard)
        data = {"chat_id": chat_id,
                "text": text, 
                "reply_markup": json.dumps(reply_markup.to_dict())}
        requests.post(url, data=data)
        
    def send_markup(self, text, buttons, chat_id):
        url = self.base + "sendMessage"
        reply_markup =  ReplyKeyboardMarkup(buttons, one_time_keyboard=True)
        data = {"chat_id": chat_id,
                "text": text, 
                "reply_markup": json.dumps(reply_markup.to_dict())}
        requests.post(url, data=data) 
        
        
    def read_token_from_config_file(self, config):
        parser = cfg.ConfigParser()
        parser.read(config)
        return parser.get('creds', 'token')

def process_update(item):
    try:
        if 'callback_query' in item.keys():
            update_id = item['update_id']
            user_id = item['callback_query']['from']['id']
            is_bot = item['callback_query']['from']['is_bot']
            name = item['callback_query']['from']['first_name'] 
            chat_id = item['callback_query']['message']['chat']['id']
            data = item['callback_query']['data']
            question_text = item['callback_query']['message']['text']
            options = [i['text'] for i in sum(item['callback_query']['message']['reply_markup']['inline_keyboard'], [])]
            call_back_options = [i['callback_data'] for i in sum(item['callback_query']['message']['reply_markup']['inline_keyboard'], [])]
            date = item['callback_query']['message']['date']
        else:
            
            update_id = item['update_id']
            user_id = item['message']['from']['id']
            is_bot = item['message']['from']['is_bot']
            name = item['message']['from']['first_name'] 
            chat_id = item['message']['chat']['id']
            data = item['message']['text']
            question_text = None
            options = None
            call_back_options = None
            date = item['message']['date']

        return(update_id,user_id,is_bot,name,chat_id,data,question_text,options,call_back_options,date)
    except:
        update_id = None
        user_id = None
        is_bot = None
        name = None
        chat_id = None
        data = None
        question_text = None
        options = None
        call_back_options = None
        date = None
        return(update_id,user_id,is_bot,name,chat_id,data,question_text,options,call_back_options,date)
    
        
  
    
    
    