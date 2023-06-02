
# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

database = {
    "harry": {
        "account_number": "1234",
        "balance": 1000
    },
    "ron": {
        "account_number": "5678",
        "balance": 2500
    }
}

class ActionCheckBalance(Action):
    def name(self) -> Text:
        return "utter_check_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        name = tracker.get_slot("name")
        
        if name in database:
            account_number = database[name]["account_number"]
            balance = database[name]["balance"]
            dispatcher.utter_message(template="utter_check_balance", name=name, account_number=account_number)
        else:
            dispatcher.utter_message("Sorry, the provided details are incorrect.")

        return []
