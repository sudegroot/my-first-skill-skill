from mycroft import MycroftSkill, intent_handler


class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('skill.first.my.intent')
    def handle_skill_first_my(self, message):
        self.speak_dialog('skill.first.my')

    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        time = self.get_response('skill.study')
        self.speak_dialog('skill.study.confirmation', {'time': time})


def create_skill():
    return MyFirstSkill()
