from mycroft import MycroftSkill, intent_file_handler


class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.first.my.intent')
    def handle_skill_first_my(self, message):
        self.speak_dialog('skill.first.my')


def create_skill():
    return MyFirstSkill()
