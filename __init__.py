import time
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
   
        
    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        blocks = extract_duration(self.get_response('skill.study'))[0]
        self.speak_dialog('skill.study.confirmation', {'time': str(blocks)})
        blocks = int(blocks)
        for i in range(blocks):
            time.sleep(1500)
            if i <  blocks-1:
                self.speak_dialog('skill.breakbegin')
                time.sleep(300)
                self.speak_dialog('skill.breakend') 
            if i == blocks-1:
                break
        self.speak_dialog('skill.end') 



def create_skill():
    return MyFirstSkill()
