#import time
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration
from mycroft.messagebus import Message

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.first.my.intent')
    def handle_skill_first_my(self, message):
        self.speak_dialog('skill.first.my')

        
        
    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        time = self.get_response('skill.study')
        # self.speak_dialog('skill.study.confirmation', {'time': str(time)})
        self.bus.emit(Message("recognizer_loop:utterance", {'utterances': ["set a timer for %s" %time], 'lang': 'en-us'}))

      #  t = extract_duration(self.get_response('skill.study'))[0]
      #  self.speak_dialog('skill.study.confirmation', {'time': str(t)})
      #  duration = t*60
      #  time.sleep(duration)
      #  self.speak_dialog('skill.study.end') 
       
     
         
   

def create_skill():
    return MyFirstSkill()
