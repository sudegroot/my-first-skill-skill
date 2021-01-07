#import time
from mycroft import MycroftSkill, intent_handler
from mycroft.messagebus import Message

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    #def initialize(self):
        #self.add_event('skill.mycrofttimer.expired',
                       #self.handler_time_up)

    @intent_handler('skill.first.my.intent')
    def handle_skill_first_my(self, message):
        self.speak_dialog('skill.first.my')

    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        time = self.get_response('skill.study')
        # We receive the response from the user on how long they want to study for example '5 minutes"
        # We use the message bus, where we put the message on the bus and format the string with 'set a timer'
	# so that the Timer Skill from mycroft will recognize it and set the timer accordingly.
        self.bus.emit(Message("recognizer_loop:utterance", {'utterances': ["set a timer for %s" %time], 'lang': 'en-us'}))

    #def handler_time_up(self, message):
        #self.bus.emit(Message('speak',{"utterance": 'This is a test',
        #"lang": 'en-us'}))


def create_skill():
    return MyFirstSkill()
