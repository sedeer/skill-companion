from adapt.intent import IntentBuilder
from mycroft import MycroftSkill, intent_handler

class WelcomeHomeSkill(MycroftSkill):
    def __init__(self):
        """ The __init__ method is called when the Skill is first constructed.
        It is often used to declare variables or perform setup actions, however
        it cannot utilise MycroftSkill methods as the class does not yet exist.
        """
        super().__init__()

    def initialize(self):
        """ Perform any final setup needed for the skill here.
        This function is invoked after the skill is fully constructed and
        registered with the system. Intents will be registered and Skill
        settings will be available."""
        self.user = self.settings.get('user')

    @intent_handler(IntentBuilder('WelcomeHomeIntent').require('WelcomeHome'))
    def handle_welcome_home_intent(self, message):
        """ Skills can log useful information. These will appear in the CLI and
        the skills.log file."""
        self.log.info("%s is home!" % self.user )
        self.speak_dialog("welcome.home", data={'user': self.user})

    def stop(self):
        pass

def create_skill():
    return WelcomeHomeSkill()
