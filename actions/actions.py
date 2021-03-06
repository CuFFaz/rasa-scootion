# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionShowColors(Action):

    def name(self) -> Text:
        return "action_show_colors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Ivory", image="https://i.imgur.com/g98AbNE.png")
        dispatcher.utter_message(text="Scarlet Red", image="https://i.imgur.com/ko12o8Q.jpg")
        dispatcher.utter_message(text="Carolina Blue", image="https://i.imgur.com/ggU5pqz.jpg")
        dispatcher.utter_message(text="Boysenberry", image="https://i.imgur.com/cDWmABc.jpg")
        dispatcher.utter_message(text="Lapis Blue", image="https://i.imgur.com/gYeOOBy.jpg")

        return []
