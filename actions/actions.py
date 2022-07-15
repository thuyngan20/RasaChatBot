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
# from rasa_sdk.interfaces import Action
import random

DATABASE = ['bún bò','mì quảng gà','mì quảng tôm thịt','bánh canh cá lóc',
            'bánh canh chả','bánh canh xương chả','cơm sườn',
            'hủ tiếu','gỏi cuốn','cháo bò','miến lươn','bún lòng xào nghệ',
            'bún riêu','cơm tấm','bánh ướt lòng gà','bánh hỏi lòng heo']

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
            cust_sex = "bạn"

        if (cust_sex == "anh") | (cust_sex == "chị"):
           bot_position = "em"
        elif (cust_sex == "cô") | (cust_sex == "chú"):
            bot_position = "cháu"
        else:
            cust_sex = "bạn"
            bot_position = "SHB"

        if not cust_name:
            #dispatcher.utter_template("utter_greet_name",tracker)
            return []

        print (name_cap(cust_name))
        return [SlotSet('cust_name', " "+name_cap(cust_name)),SlotSet('cust_sex', name_cap(cust_sex)),SlotSet('bot_position', name_cap(bot_position))]

class actionRecommend(Action):

    def name(self) -> Text:
        return "action_food_recommend"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        food = []
        for i in range(2):
          food_number = random.randrange(len(DATABASE))
          food.append(DATABASE[food_number])

        dispatcher.utter_message(text="Tôi nghĩ bạn nên thử  {} ,hoặc {} cũng là một sự lựa chọn tuyệt vời, món nào cũng ngon!".format(food[0], food[1]))

        return []


# class ActionGreet(Action):
#     def name(self):
#         return 'action_greet'

#     def run(self, dispatcher, tracker, domain):
#         dispatcher.utter_button_message('some text that can be ignored', button)
#     return []

