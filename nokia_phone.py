
def welcome():

    action = input(' Welcome      press 1 for main menu ')
    if action is "1":
        main_menu ()
    else:
        print('thanks for using nokia mobile')

    def main_menu ():
        action = input("""
        1-> Phone_Book 
        2-> Messages
        3-> Chat
        4-> Call_register
        5-> Tone
        6_> settings
        7-> Call_divert
        8-> Games
        9-> Calculator
        10-> Reminders
        11-> Clocks
        12-> Profiles
        13-> SIM_services
        """)

        def phone_book():
            menu = ("""
            1-> Search
            2-> service
            3-> Add_name
            4-> Erase
            5-> Edit
            6-> Assign_tone
            7-> Send_Business_card
            8-> options
            9-> Speed_dials
            10-> Voice tags
            """)

        def messages():
            menu = ("""
            1-> Write_messages
            2-> Inbox
            3-> Outbox
            4-> Picture_messages
            5-> Templates
            6-> Smileys
            7-> Message_settings
            8-> Info_service
            9-> Voice_mialBox_number
            10-> Service_command_editor
            """)

        def chat():
            menu = ()

        def Call_register():
            menu = ("""
            1-> Missed_calls
            2-> Received_calls
            3-> Dailed_numbers
            4-> Erase_recent_call_lists
            5-> Show_call_duration
            6-> Show-call-cost
            7-> Call_cost_settings
            8-> Prepaid_credit
            """)

        def tones():
            menu = ("""
            1-> Ringing_tone
            2-> Ringing_volume
            3-> Incoming_call_alert
            4-> Composer
            5-> Message_alert_tone
            6-> keypad_tones
            7-> Warning_and_game_tone
            8-> Vibrating_alert
            9-> Screen_saver
            """)

        def Settings():
            menu = ("""
            1-> Call_settings
            2-> """)
