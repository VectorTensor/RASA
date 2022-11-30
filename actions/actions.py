# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
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

location_db ={
    "pokhara": 1500,
    "chitwan": 1700,
    "birgunj":2500,
    "ilam": 3000
}

class GiveLoacations(Action):
    def name(self) -> Text:
        return "return_locations"


    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        locations = ' '.join(location_db.keys()     )
        dispatcher.utter_message(text="locations -> "+locations)
        return []

class Cost(Action):
    def name(self) -> Text:
        return "cost_check"


    def run(self, dispatcher: CollectingDispatcher, tracker:Tracker, domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        locations = ' '.join(location_db.keys())
        value = next(tracker.get_latest_entity_values("location"), None)

        if  value == None:
            dispatcher.utter_message(text="Please enter a location "+ locations)
            return []

        
        if value != None:
            location = value.lower()

        else:
            location = value
        if location in location_db:
            dispatcher.utter_message(text="The cost for this location travel is "+ str(location_db[location]) +" per day")

        else:
            dispatcher.utter_message(text="we dont provide travel to this location. The locations we provide are "+ locations)
        return []