#import time
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)


    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        time = extract_duration(self.get_response('skill.study'))[0]
        self.speak_dialog('skill.study.confirmation', {'time': str(time)})
        
      #  t = extract_duration(self.get_response('skill.study'))[0]
      #  self.speak_dialog('skill.study.confirmation', {'time': str(t)})
      #  duration = t*60
      #  time.sleep(int(duration))
      #  self.speak_dialog('skill.study.end') 
       
     
         
   

def create_skill():
    return MyFirstSkill()
