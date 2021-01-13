import time
from datetime import datetime, timedelta
from mycroft import MycroftSkill, intent_handler
from mycroft.util.parse import extract_duration, extract_number
from mycroft.util.time import now_local

class MyFirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        self.tasknames = ['task one', 'task two', 'task three']

    @intent_handler('skill.study.intent')
    def handle_skill_study(self, message):
        
        # Give a welcome message to the user
        self.speak_dialog('skill.welcome')
        participantnumber = self.get_response('skill.participant.number')
        
        # Get the tasks the user wants to accomplish
        tasks = []
        task1 = self.get_response('tasks.task1')
        self.speak_dialog('tasks.task1.confirmation', data={"task1": task1})
        tasks.append(task1)
        
        another_task = self.ask_yesno('tasks.another.task')
        while another_task != 'yes' and another_task != 'no':
            self.speak_dialog('skill.task.could.not.understand')
            another_task = self.ask_yesno('tasks.another.task')            
        if another_task == "yes":
            task2 = self.get_response('tasks.task2')
            tasks.append(task2)
        elif another_task == "no":
            self.speak_dialog('tasks.moveon')

        last_task = self.ask_yesno('tasks.last.task')
        while last_task != 'yes' and last_task != 'no':
            self.speak_dialog('skill.last.task.could.not.understand')
            last_task = self.ask_yesno('tasks.last.task')
        if last_task == "yes":
            task3 = self.get_response('tasks.task3')
            tasks.append(task3)
        elif last_task == "no":
            self.speak_dialog('tasks.moveon')

        if len(tasks) == 1:
            number_of_tasks = "1 task"
        if len(tasks) > 1:
            number_of_tasks = "{} tasks".format(len(tasks))

        self.speak_dialog('tasks.confirmation', data={"number_of_tasks": number_of_tasks})

        # Get the amount of blocks from the user
        # a selection is used, to minimize pronunciation errors. This way, the answer is compared to the options and the option that matches the answer the most is chosen.
        # For example, if mycroft thinks a user says 'free brooks', he will pick three blocks as answer.

        self.speak_dialog('blocks.amount.of.blocks')
        blocks = extract_number(self.ask_selection(['one block', 'two blocks', 'three blocks'], 'blocks.selection'))
        while not blocks:
            self.speak_dialog('skill.blocks.could.not.understand')
            blocks = extract_number(self.ask_selection(['one block', 'two blocks', 'three blocks'], 'skill.blocks.could.not.understand'))

         
        # If the user selects one block, Mycroft responds with the singular "block" 
        if blocks == 1:
            amount_of_blocks = "1 block"
        
        # If the user selects multiple blocks, Mycroft responds with the plural "blocks"
        if blocks > 1:
            amount_of_blocks = "{} blocks".format(str(blocks))
            
        # Get the current time to calculate the time when the user will be done in the future
        now = now_local()
        currenttime = now.strftime("%H:%M")
        
        # Calculate the time when the user is done based on the amount of blocks selected
        # Each block is 25 minutes and each break is 5 minutes
        
        minutes = blocks*25 + (blocks-1)*5
        futuretime = now + timedelta(minutes=minutes)
        futuretime = futuretime.strftime("%H:%M")
        
        # Respond to the user with the amount of blocks they have chosen, what the curren time is
        # and when their study session will be finished
        self.speak_dialog('blocks.confirmation', data={'currenttime': currenttime,
                                                        'amount_of_blocks': amount_of_blocks,
                                                        'futuretime': futuretime})

        
        # The time.sleep() function takes an input of seconds
        # If you want the code to sleep for several minutes you should multiply the values with 60
        # Currently everythting is in second for debugging purposes
        for i in range(blocks):
            time.sleep(25)
            if i <  blocks-1:
                self.speak_dialog('study.break.begin')
                time.sleep(5)
                self.speak_dialog('study.break.end')
            if i == blocks-1:
                break
        self.speak_dialog('study.end')
        
    @intent_handler('tasks.change.task.intent')
    def change_task(self, message):
        selection = self.ask_selection(self.tasknames, 'tasks.what.task')

        if selection == 'task one':
            task1 = self.get_response('tasks.change.task', data={"selection": selection})
            self.speak_dialog('tasks.task1.confirmation', data={"task1": task1})

        if selection == 'task two':
            task2 = self.get_response('tasks.change.task', data={"selection": selection})
            self.speak_dialog('tasks.task2.confirmation', data={"task2": task2})

        if selection == 'task three':
            task3 = self.get_response('tasks.change.task', data={"selection": selection})
            self.speak_dialog('tasks.task3.confirmation', data={"task3": task3})    



def create_skill():
    return MyFirstSkill()
