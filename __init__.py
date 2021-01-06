#import time
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.first.my.intent')
    def handle_skill_first_my(self, message):
        self.speak_dialog('skill.first.my')

    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        t = extract_duration(self.get_response('skill.study'))[0]
        self.speak_dialog('skill.study.confirmation', {'time': str(t)})
        duration = t*60
        return duration
        #for i in range(duration):
        #    time.sleep(1)
        #self.speak_dialog('skill.study.end')
        
      #   time = extract_duration(self.get_response('skill.study'))[0]
      #  self.speak_dialog('skill.study.confirmation', {'time': str(time)})
   

def create_skill():
    return MyFirstSkill()
