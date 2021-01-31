import datetime
import numpy as np
import random
import pandas as pd
from scipy.optimize import brute
import pickle
import telegrambot
from threading import Thread
from telegrambot import telegram_chatbot, process_update
import glob
import os
from dialogues import *



user_state_base = '/Users/kowshik/KnowKowshik/USER_STATES/'
'''
deletion of all files 
'''
def delete_user_states(user_state_base,user):
    
    '''
    Delete logs for a particular user 
    '''
    
    filelist = glob.glob(user_state_base+'*'+user+'*')
    if len(filelist)>0:
        for filePath in filelist:
            os.remove(filePath) 
            
user = ''
delete_user_states(user_state_base,user)


class DIALOGUE():
    def __init__(self, user, bot , conv, dialogues, user_state_base ):
        self.user = str(user)
        self.bot = bot
        self.conv = conv
        self.dialogues = dialogues
        self.STATE_FAIL = False
        self.user_state_base = user_state_base
        self.create_user_states()
        
        
    def create_user_states(self):
        try:
            newest = max(glob.glob(self.user_state_base+str(self.user)+'*'), key=os.path.getctime)
        except:
            self.STATE = 'START'
            self.known_users =[]
            self.dump_state()            
            
    def dump_state(self):
        
        '''
        Dump update logs
        '''
        sv = [self.STATE,self.known_users]
        str_to_add = str(datetime.datetime.now()).split('.')[0]
        with open(self.user_state_base +str(self.user)+'::'+str_to_add+'::'+self.STATE +'.pkl', 'wb') as f:
            pickle.dump(sv, f)
            
    def get_state(self):
        newest = max(glob.glob(self.user_state_base+str(self.user)+'*'), key=os.path.getctime)
        with open(newest, 'rb') as f:
            sv = pickle.load(f)
        self.STATE_ = sv[0] 
        self.known_users_ = sv[1] 
            
        
    def interpret_update(self):
        update_id,user_id,is_bot,name,chat_id,data,question_text,options,call_back_options,date = self.conv
        if self.STATE_ == 'START':
            return(data, is_bot)
        elif self.STATE_ in ['GREET1','GREET2','GREET3','WRITINGS','PROCESS','PROFJOURN', 'PERJOURN' ,'Internships_state','Freelancing_state','Competitions_state','opensource_state' ]:
            return(data,is_bot)

    def expected_input(self,data):
        if self.STATE_ in ['GREET1','GREET2','GREET3','WRITINGS','PROCESS','PROFJOURN', 'PERJOURN' ,'Internships_state','Freelancing_state','Competitions_state','opensource_state']:
            if data in self.dialogues[self.STATE_]['acceptable']:
                return(True)
            else:
                return(False)
        else:
            return(False)               
        
    def new_user(self):
        if self.user not in self.known_users_:
            return(True)
        else:
            return(False)
        
    def add_user_to_know_users(self):
        self.known_users.append(self.user)
        return
    
    def greet_first_user_one(self):
        self.get_state()
        self.known_users = self.known_users_
        if self.STATE_ == 'START' and self.new_user():
            is_bot =  self.interpret_update()
            self.bot.send_message(self.dialogues['GREET1']['text1'],self.user)
            self.bot.send_markup(self.dialogues['GREET1']['text2'],self.dialogues['GREET1']['options'] ,self.user)
            self.STATE = 'GREET1'
            self.STATE_FAIL = False
            return
        else:
            return
        
    def greet_first_user_two(self):
        self.get_state()
        self.known_users = self.known_users_
        if self.STATE_ == 'GREET1' and self.new_user():
            data,is_bot =  self.interpret_update()
            if self.expected_input(data):
                if data == self.dialogues['GREET1']['options'][0][0]:
                    self.bot.send_markup(self.dialogues['GREET2']['text'],self.dialogues['GREET2']['options'], self.user)
                    self.STATE = 'GREET2'
                    self.STATE_FAIL = False
                    return
                else:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False
                    return  
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True
                return
        else:
            return
        
    def greet_first_user_three(self):
        self.get_state()
        self.known_users = self.known_users_
        if self.STATE_ == 'GREET2' and self.new_user():
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                self.bot.send_message(self.dialogues['GREET3'][data]['text'],self.user)
                self.bot.send_message(dialogues['GREET3']['text2'],self.user)
                self.bot.send_markup(dialogues['GREET3']['text3'],self.dialogues['GREET3']['options'], self.user)
                self.STATE = 'START'
                self.STATE_FAIL = False
                self.add_user_to_know_users()
                return
            else:
                self.STATE = 'GREET1'
                self.STATE_FAIL = True
                return
        else:
            return
 

    def process_request(self):
        self.get_state()
        if self.STATE_ == 'START' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if data != self.dialogues['reject']:
                self.bot.send_markup(self.dialogues['PROCESS']['text'],self.dialogues['PROCESS']['options'], self.user)
                self.STATE = 'PROCESS'
                self.STATE_FAIL = False
            else:
                self.bot.send_message(self.dialogues['BYE'],self.user)
                self.STATE = 'START'
                self.STATE_FAIL = False
                
                


    def process_request_individual(self):
        self.get_state()
        if self.STATE_ == 'PROCESS' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                
                if data == self.dialogues['PROCESS']['options'][0][0]:
                    self.bot.send_document('kowshik_latest_ds.pdf' , self.dialogues['RESUME']['text'] , self.user)
                    self.bot.send_markup(dialogues['END']['text'],self.dialogues['END']['options'], self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False 
                    return
                    
                elif data == self.dialogues['PROCESS']['options'][1][0]:
                    self.bot.send_message(self.dialogues['WRITINGS']['text1'], self.user)                    
                    self.bot.send_message(self.dialogues['WRITINGS']['text2'], self.user)   
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                    return
                elif data == self.dialogues['PROCESS']['options'][2][0]:
                    self.bot.send_message(self.dialogues['PROFJOURN']['text1'], self.user) 
                    self.bot.send_markup(self.dialogues['PROFJOURN']['text2'],self.dialogues['PROFJOURN']['options'], self.user)
                    self.STATE = 'PROFJOURN'
                    self.STATE_FAIL = False 
                    return                    
                elif data == self.dialogues['PROCESS']['options'][3][0]:  
                    self.bot.send_message(self.dialogues['PERJOURN']['text1'], self.user) 
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                    return   
                    
                    
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True

            
    def process_writings(self):
        self.get_state()
        if self.STATE_ == 'WRITINGS' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == 'Reinforcement learning':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user)
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == 'Game Theory':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user)
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == 'Temporal Models':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user) 
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == 'NLP':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user)
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == 'History':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user)
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == 'others':
                    self.bot.send_message(self.dialogues['WRITINGSEND'][data], self.user)
                    self.bot.send_markup(self.dialogues['WRITINGS']['text3'],self.dialogues['WRITINGS']['options'], self.user)
                    self.STATE = 'WRITINGS'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['reject']:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False                                                
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True
               
    def process_perjourn(self):
        self.get_state()
        if self.STATE_ == 'PERJOURN' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == self.dialogues['PERJOURN']['options'][0][0]:
                    self.bot.send_message(self.dialogues['PERJOURN']['0'], self.user)
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PERJOURN']['options'][1][0]:
                    self.bot.send_message(self.dialogues['PERJOURN']['1'], self.user)
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PERJOURN']['options'][2][0]:
                    self.bot.send_message(self.dialogues['PERJOURN']['2'], self.user)
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PERJOURN']['options'][3][0]:
                    self.bot.send_message(self.dialogues['PERJOURN']['3'], self.user)
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PERJOURN']['options'][4][0]:
                    self.bot.send_message(self.dialogues['PERJOURN']['4'], self.user)
                    self.bot.send_markup(self.dialogues['PERJOURN']['text2'],self.dialogues['PERJOURN']['options'], self.user)
                    self.STATE = 'PERJOURN'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PERJOURN']['options'][5][0]:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False                                                
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True    

                
               
    def process_profjourn(self):
        self.get_state()
        if self.STATE_ == 'PROFJOURN' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == 'Internships':
                    self.bot.send_message(self.dialogues['PROFJOURN']['Internships']['text1'], self.user)
                    self.bot.send_message(self.dialogues['PROFJOURN']['Internships']['text2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 
                elif data == 'Freelancing':
                    self.bot.send_message(self.dialogues['PROFJOURN']['Freelancing']['text1'], self.user)
                    self.bot.send_message(self.dialogues['PROFJOURN']['Freelancing']['text2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Freelancing']['text3'], self.dialogues['PROFJOURN']['Freelancing']['options'], self.user)
                    self.STATE = 'Freelancing_state'
                    self.STATE_FAIL = False 
                elif data == 'Competitions':
                    self.bot.send_message(self.dialogues['PROFJOURN']['Competitions']['text1'], self.user)
                    self.bot.send_message(self.dialogues['PROFJOURN']['Competitions']['text2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Competitions']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Competitions_state'
                    self.STATE_FAIL = False 
                elif data == 'Publications/Patents':
                    self.bot.send_message(self.dialogues['PROFJOURN']['Publications/Patents']['text1'], self.user)
                    self.bot.send_message(self.dialogues['PROFJOURN']['Publications/Patents']['text2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['text2'],self.dialogues['PROFJOURN']['options'], self.user)
                    self.STATE = 'PROFJOURN'
                    self.STATE_FAIL = False 
                elif data == 'Open-Source':
                    self.bot.send_message(self.dialogues['PROFJOURN']['Open-Source']['text1'] , self.user)
                    self.bot.send_message(self.dialogues['PROFJOURN']['Open-Source']['text2'] , self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Open-Source']['text3'],self.dialogues['PROFJOURN']['Open-Source']['options'], self.user)
                    self.STATE = 'opensource_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['reject']:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False                                                
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True     
                


    def process_internships(self):
        self.get_state()
        if self.STATE_ == 'Internships_state' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == self.dialogues['PROFJOURN']['Internships']['options'][0][0]:
                    self.bot.send_message(self.dialogues['Internships_state']['0'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 
                    
                elif data == self.dialogues['PROFJOURN']['Internships']['options'][1][0]:
                    self.bot.send_message(self.dialogues['Internships_state']['1'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 

                elif data == self.dialogues['PROFJOURN']['Internships']['options'][2][0]:
                    self.bot.send_message(self.dialogues['Internships_state']['2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 
                    
                elif data == self.dialogues['PROFJOURN']['Internships']['options'][3][0]:
                    self.bot.send_message(self.dialogues['Internships_state']['3'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 
                    
                elif data == self.dialogues['PROFJOURN']['Internships']['options'][4][0]:
                    self.bot.send_message(self.dialogues['Internships_state']['4'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Internships']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Internships_state'
                    self.STATE_FAIL = False 
                    
                elif data == self.dialogues['PROFJOURN']['Internships']['options'][5][0]:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False       
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True     


    def process_Freelancing(self):
        self.get_state()
        if self.STATE_ == 'Freelancing_state' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == self.dialogues['PROFJOURN']['Freelancing']['options'][0][0]:
                    self.bot.send_message(self.dialogues['Freelancing_state']['0'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Freelancing']['text3'], self.dialogues['PROFJOURN']['Freelancing']['options'], self.user)
                    self.STATE = 'Freelancing_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Freelancing']['options'][1][0]:
                    self.bot.send_message(self.dialogues['Freelancing_state']['1'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Freelancing']['text3'], self.dialogues['PROFJOURN']['Freelancing']['options'], self.user)
                    self.STATE = 'Freelancing_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Freelancing']['options'][2][0]:
                    self.bot.send_message(self.dialogues['Freelancing_state']['2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Freelancing']['text3'], self.dialogues['PROFJOURN']['Freelancing']['options'], self.user)
                    self.STATE = 'Freelancing_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Freelancing']['options'][3][0]:
                    self.bot.send_message(self.dialogues['Freelancing_state']['3'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Freelancing']['text3'], self.dialogues['PROFJOURN']['Freelancing']['options'], self.user)
                    self.STATE = 'Freelancing_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Freelancing']['options'][4][0]:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False       
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True     

                
                
    def process_Competitions(self):
        self.get_state()
        if self.STATE_ == 'Competitions_state' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == self.dialogues['PROFJOURN']['Competitions']['options'][0][0]:
                    self.bot.send_message(self.dialogues['Competitions_state']['0'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Competitions']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Competitions_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Competitions']['options'][1][0]:
                    self.bot.send_message(self.dialogues['Competitions_state']['1'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Competitions']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Competitions_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Competitions']['options'][2][0]:
                    self.bot.send_message(self.dialogues['Competitions_state']['2'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Competitions']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Competitions_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Competitions']['options'][3][0]:
                    self.bot.send_message(self.dialogues['Competitions_state']['3'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Competitions']['text3'], self.dialogues['PROFJOURN']['Internships']['options'], self.user)
                    self.STATE = 'Competitions_state'
                    self.STATE_FAIL = False
                elif data == self.dialogues['PROFJOURN']['Competitions']['options'][4][0]:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'START'
                    self.STATE_FAIL = False       
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True  

                 
                
    def process_opensource(self):
        self.get_state()
        if self.STATE_ == 'opensource_state' and (not self.new_user()):
            data,is_bot =  self.interpret_update()
            if self.expected_input(data) or self.STATE_FAIL:
                if data == self.dialogues['PROFJOURN']['Open-Source']['options'][0][0]:
                    self.bot.send_message(self.dialogues['opensource_state']['0'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Open-Source']['text3'],self.dialogues['PROFJOURN']['Open-Source']['options'], self.user)
                    self.STATE = 'opensource_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Open-Source']['options'][1][0]:
                    self.bot.send_message(self.dialogues['opensource_state']['1'], self.user)
                    self.bot.send_markup(self.dialogues['PROFJOURN']['Open-Source']['text3'],self.dialogues['PROFJOURN']['Open-Source']['options'], self.user)
                    self.STATE = 'opensource_state'
                    self.STATE_FAIL = False 
                elif data == self.dialogues['PROFJOURN']['Competitions']['options'][2][0]:
                    self.bot.send_message(self.dialogues['BYE'],self.user)
                    self.STATE = 'opensource_state'
                    self.STATE_FAIL = False       
            else:
                self.STATE = 'START'
                self.STATE_FAIL = True  
                
                
    def generate_dialogue_flow(self):
        self.greet_first_user_one()
        self.greet_first_user_two()
        self.greet_first_user_three()
        self.process_request()
        self.process_request_individual()
        self.process_writings()
        self.process_perjourn()
        self.process_profjourn()
        self.process_internships()
        self.process_Freelancing()
        self.process_Competitions()
        self.process_opensource()
        return
    
    def save_state(self):
        if not self.STATE_FAIL:
            self.dump_state()
        else:
            self.bot.send_message(self.dialogues['ERROR'],self.user)
            self.dump_state()
            self.generate_dialogue_flow()
            self.dump_state()

    def load_state(self):
        self.get_state()
            
user_state_base = '/Users/kowshik/KnowKowshik/USER_STATES/'
delete_user_states(user_state_base,'')

def dialogue_thread():
    DIAL= DIALOGUE(user,bot,conv,dialogues,user_state_base)
    DIAL.generate_dialogue_flow()
    DIAL.save_state()

bot = telegram_chatbot("config.cfg")
update_id = None
while True:
    updates = bot.get_updates(offset=update_id)
    updates = updates["result"]
    if updates:
        for item in updates[-1:]:
            conv = process_update(item)
            user = conv[1]
            update_id = item["update_id"]
            Thread(target=dialogue_thread).start()
            