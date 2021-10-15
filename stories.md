## blokir_rekening
* greet
    - utter_greet
* blok_kartuATM
    - utter_tanya_nama
* tanya_nama
    - utter_tanya_norek
* blok_kartuATM{"norek": "1301160802"}
    - slot{"norek": "1301160802"}
    - action_blok_customer
* affirm
    - utter_did_that_help 
* gratitude
    - utter_thanks

## forget_pin
* greet
    - utter_greet
* pin
    - utter_tanya_nama
* tanya_nama
    - utter_tanya_norek
* pin{"norek": "1301160802"}
    - slot{"norek": "1301160802"}
    - action_pin_customer
* affirm
    - utter_did_that_help 
* gratitude
    - utter_thanks
    
## tanya_saldo
* greet
    - utter_greet
* saldo
    - utter_tanya_nama
* tanya_nama
    - utter_tanya_norek
* saldo{"norek": "1301160802"}
    - slot{"norek": "1301160802"}
    - action_saldo_customer
* affirm
    - utter_did_that_help 
* gratitude
    - utter_thanks

## rekening_baru
* greet
    - utter_greet
* registrasi_rekening
    - utter_tanya_type
* type_rekening
    - utter_link_registrasi
* affirm
  - utter_did_that_help 
* gratitude
  - utter_thanks
  
## say_hello_123
* greet
  - utter_greet
* info_rekening
  - utter_tanya_nama
* tanya_nama
  - utter_tanya_jenis_rekening
* jenis_rekening
  - utter_tanya_syarat
* not_yet
  - utter_jenis_rekening_silver
* affirm
  - utter_link_registrasi
* gratitude
  - utter_thanks

## say_hello_321
* greet
  - utter_greet
* info_rekening
  - utter_tanya_nama
* tanya_nama
  - utter_tanya_jenis_rekening
* jenis_rekening
  - utter_tanya_syarat
* not_yet
  - utter_jenis_rekening_gold
* affirm
  - utter_link_registrasi
* gratitude
  - utter_thanks

## deny_silver
* greet
  - utter_greet
* info_rekening
  - utter_tanya_nama
* tanya_nama
  - utter_tanya_jenis_rekening
* jenis_rekening
  - utter_tanya_syarat
* not_yet
  - utter_jenis_rekening_silver
* deny
  - utter_thanks
  
## deny_gold
* greet
  - utter_greet
* info_rekening
  - utter_tanya_nama
* tanya_nama
  - utter_tanya_jenis_rekening
* jenis_rekening
  - utter_tanya_syarat
* not_yet
  - utter_jenis_rekening_gold
* deny
  - utter_thanks
  
## say_goodbye
* goodbye
  - utter_goodbye
  
## user_denies_question
  - utter_unclear