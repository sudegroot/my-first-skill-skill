import time
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
        time = extract_duration(self.get_response('skill.study'))[0]
        self.speak_dialog('skill.study.confirmation', {'time': str(time)})
        
        blocks = extract_duration(self.get_response('skill.study'))[0]
        self.speak_dialog('skill.study.confirmation', {'time': str(t)})
        blocks = int(blocks)
        for i in range(blocks):
            time.sleep(1500)
            if i <  blocks-1:
                self.speak_dialog('skill.study.break.begin')
                time.sleep(300)
                self.speak_dialog('skill.study.break.end') 
            if i == blocks-1:
                break
        self.speak_dialog('skill.study.end') 



def create_skill():
    return MyFirstSkill()
