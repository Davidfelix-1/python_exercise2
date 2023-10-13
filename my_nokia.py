def my_nokia():
    print("welcome nokia mobile")


def main_menu():
    print("""
    1-> phone_book
    2-> messages
    3-> chat
    4-> call_register
    5-> tones
    6-> setting
    7-> call_divert
    8-> games
    9-> calculator
    10-> reminders
    11-> clock
    12-> profiles
    13-> sim_services
    """)


def phone_book():
    selection = int(input(" select option : "))
    if selection == 1:
        print("""
        1-> search
        2-> service_numbers
        3-> add name
        4-> erase
        5-> edit
        6-> send b'card
        7-> options
        8-> speed dials
        9-> voice tags
        """)


def message():
    selection = int(input(" select option:  "))
    if selection == 2:
        print("""
        1-> write message
        2-> inbox
        3-> outbox
        4-> picture message
        5-> templates
        6-> smileys
        7-> message settings
        7->1 set 1
         -->1 message center number
         -->2 message sent as
         -->3 message validity
        7->2 common
         -->1 delivery reports
         -->2 reply via same centre
         -->3 character support
        8-> info service
        9-> voice mailbox number
        10-> service command editor
        """)


def chat():
    selection = int(input(" select option:   "))
    if selection == 3:
        print("""chat""")
    if selection == 4:
        print("""
        1-> missed calls
        2-> received calls
        3-> dailed numbers
        4-> erase recent calls lists
        5-> show call duration
        5->1 last call duration
         ->2 all calls duration
         ->3 received calls duration
         ->4 dialed calls duration
         ->5 clear call timers
        6-> show call costs
         ->1 last call cost
         ->2 all calls cost
         ->3 clear counters
        7-> call cost settings
         ->1 call cost limit
         ->2 show costs in
        8-> prepaid credit
         """)


def tone():
    selection = int(input(" select option : "))
    if selection == 5:
        print("""
        1-> ringing tone
        2-> ringing volume
        3-> incoming call alert
        4-> composer
        5-> message alert tone
        6-> keypad tone
        7-> warning and game tones
        8-> vibrating alert
        9-> screen saver
        """)


def settings():
    selection = int(input(" select option:  "))
    if selection == 6:
        print("""
        1-> call settings
         ->1 authomatic redial
         ->2 speed dialing
         ->3 call waiting options
         ->4 own number sending
         ->5 phone line in use
         ->6 automatic answer
        2-> phone settings
         ->1 language
         ->2 cell info display
         ->3 welcome note
         ->4 network selection
         ->5 lights
         ->6 confirm SIM service actions
        3-> security settings 
         ->1 PIN code request
         ->2 call barring service
         ->3 fixed dialing
         ->4 closed user group
         ->5 phone security
         ->6 change access codes
        4-> restore factory settings 
        """)


def call_divert():
    selection = int(input(" select option:  "))
    if selection == 7:
        print("""
        1-> call divert
        """)


def games():
    selection = int(input("select option: "))
    if selection == 8:
        print("""
        1-> games
        """)


def calculator():
    selection = int(input("select option:  "))
    if selection == 9:
        print("""
        1-> calculator
        """)


def reminder():
    selection = int(input("select option:  "))
    if selection == 10:
        print("""
        1-> reminder 
        """)


def clock():
    selection = int(input("select option:  "))
    if selection == 11:
        print("""
        1-> alarm clock
        2-> clock settings
        3-> dt setting
        4-> stopwatch
        5-> countdown timer
        6-> auto update of date and time
        """)


def profile():
    selection = int(input(" select option:   "))
    if selection == 12:
        print("""
        1-> profile
        """)


def sim_services():
    selection = int(input(" select option:   "))
    if selection == 13:
        print("""
        1-> SIM services
        """)

