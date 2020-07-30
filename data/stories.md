## complete path
* greet
  - utter_greet
* resto_search
  - utter_ask_location
* resto_search{"location":"delhi"}
  - slot{"location":"delhi"}
  - utter_ask_cuisine
* resto_search{"cuisine":"south indian"}
  - slot{"cuisine":"south indian"}
  - action_search_resto
  - slot{"location":"delhi"}
* affirm
  - utter_goodbye
  - export

## complete path 2
* greet
  - utter_greet
* resto_search
  - utter_ask_location
* resto_search{"location":"delhi"}
  - slot{"location":"delhi"}
  - utter_ask_cuisine
* resto_search{"cuisine":"mexican"}
  - slot{"cuisine":"mexican"}
  - action_search_resto
* goodbye
  - utter_goodbye

## complete path 3
* greet
  - utter_greet
* resto_search
  - utter_ask_location
* resto_search{"location":"rome"}
  - slot{"location":"rome"}
  - utter_ask_cuisine
* resto_search{"cuisine":"chinese"}
  - slot{"cuisine":"chinese"}
  - action_search_resto
* affirm
  - utter_goodbye

## location specific
* greet
  - utter_greet
* resto_search{"location":"rome"}
  - slot{"location":"rome"}
  - utter_ask_cuisine
* resto_search{"cuisine":"chinese"}
  - slot{"cuisine":"chinese"}
  - action_search_resto
* affirm
  - utter_goodbye

## cuisine specific
* greet
  - utter_greet
* resto_search{"cuisine":"chinese"}
  - slot{"cuisine":"chinese"}
  - utter_ask_location
* resto_search{"location":"rome"}
  - slot{"location":"rome"}
  - action_search_resto
* affirm
  - utter_goodbye

## complete info path
* greet
  - utter_greet
* resto_search{"cuisine":"asian", "location":"pondicherry"}
  - slot{"cuisine":"asian"}
  - slot{"location":"pondicherry"}
  - action_search_resto
* affirm
  - utter_goodbye