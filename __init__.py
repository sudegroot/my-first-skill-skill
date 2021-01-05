from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration
from mycroft.core.mycroft_alarm.mycroftai import AlarmSkill

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


def create_skill():
    return MyFirstSkill()
