from telnetlib import DO
from typing import Any, Text, Dict, List
from xxlimited import foo
from rasa_core.actions import Action
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.core.channels.channel import InputChannel
from rasa_sdk.events import SlotSet
import random

DATABASE = ['Bun bo','Mi quang','Banh canh','Com suon',
            'Hu tieu','Goi cuon','An hai','An nan','An chay',
            'An gi cung duoc','BeefSteak','Hotpot','Grill']

def name_cap(text):
    tarr = text.split()
    for idx in range(len(tarr)):
        tarr[idx] = tarr[idx].capitalize()
    return ' '.join(tarr)

class action_save_cust_info(Action):
    def name(self):
        return 'action_save_cust_info'

    def run(self, dispatcher, tracker, domain):
        user_id = (tracker.current_state())["sender_id"]
        print(user_id)
        cust_name = next(tracker.get_latest_entity_values("cust_name"), None)
        cust_sex = next(tracker.get_latest_entity_values("cust_sex"), None)
        bot_position = "SHB"

        if (cust_sex is  None):
            cust_sex = "Quý khách"

        if (cust_sex == "anh") | (cust_sex == "chị"):
           bot_position = "em"
        elif (cust_sex == "cô") | (cust_sex == "chú"):
            bot_position = "cháu"
        else:
            cust_sex = "Quý khách"
            bot_position = "SHB"

        if not cust_name:
            #dispatcher.utter_template("utter_greet_name",tracker)
            return []

        print (name_cap(cust_name))
        return [SlotSet('cust_name', " "+name_cap(cust_name)),SlotSet('cust_sex', name_cap(cust_sex)),SlotSet('bot_position', name_cap(bot_position))]

class actionRecommend(Action):

    def name(self) -> Text:
        return "utter_food"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = []
        for i in range(2):
          food_number = random.randrange(len(DATABASE))
          food.append(DATABASE[food_number])

        print("food")

        dispatcher.utter_message(text="I think today you can try '{}' or besides may be is '{}'. It so tasty!".format(food[0], food[1]))

        return []
