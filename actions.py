from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatoAPI as zomatopy
import json

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_resto'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":}
		zomato = zomatopy.initialize_app(config)

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)

		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		city_id = d1["location_suggestions"][0]["city_id"]

		cuisines_dict=zomato.get_cuisines(city_id)
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response = ""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found:\t "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]