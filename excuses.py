import numpy as np
class Excuses:
    def __init__(self):
        pass
    @staticmethod
    def listofExcuses():
        lst = ["I'm not feeling well.",
               "I'm recovering from an illness.",
               "I need to prioritize my health right now.",
               "There's a family emergency I need to attend to.",
               "I have a personal matter that requires immediate attention.",
               "I'm dealing with a sudden crisis.",
               "My workload at work is overwhelming at the moment.",
               "I have a work-related deadline that I can't postpone.",
               "A last-minute work meeting came up.",
               "I'm experiencing technical difficulties.",
               "I already have a prior commitment during this time.",
               "I'm attending an important event that I can't reschedule.",
               "I made plans before this commitment came up.",
               "I'm out of town and won't be able to make it.",
               "I'm stuck in traffic or facing transportation issues.",
               "Well! My babysitter canceled, and I can't find alternative care.",
               "I need some personal time to refresh.",
               "I'm feeling overwhelmed and need to take a mental health day.",
               "I have a prior commitment to self-care or therapy.",
               "I'm truly sorry, but I've been dealing with a persistent health issue that has been quite debilitating, and I'm unable to fulfill my commitment at this time.",
               "I regret to inform you that there's an unexpected family emergency that has arisen, requiring my immediate attention and presence, making it impossible for me to meet my obligations.",
               "I sincerely apologize, but I'm currently swamped with an extraordinarily heavy workload at my job, and I have pressing deadlines that must take precedence over other commitments.",
               "Unfortunately, I'm experiencing a significant technical glitch with my computer and internet, and despite my best efforts, I'm unable to access the necessary resources to fulfill my commitment.",
               "Regrettably, I had made prior commitments during the same timeframe, and I'm unable to reschedule or rearrange them, conflicting with the obligation that has come up.",
               "I deeply regret to inform you that I'm currently out of town on a pre-planned trip, and it's logistically impossible for me to return in time to meet this commitment.",
               "I'm facing a situation where I need to provide urgent childcare for a family member, and it's imperative that I prioritize their well-being, preventing me from fulfilling this obligation.",
               "I want to be transparent with you that I've been struggling with overwhelming stress and burnout recently, and I believe taking a short break for self-care is necessary for my overall well-being, affecting my ability to meet this commitment.",
               "I am tired! Talk to you in a while.",
               "Give some time to refresh! Thank you.",
               "Take some rest! I make it a point to schedule regular check-ups with my doctor.",
               "You need some time to refresh. Quality sleep is a game-changer. Aim for 7-9 hours a night.",
               "Taking care of your mental health is just as important as physical health. It's okay to seek help if you're feeling overwhelmed or anxious.",
               "Find some time for yourself! Being socially connected is important for our well-being. Let's make an effort to spend time with friends and family regularly.",
               "Take rest! If you have any specific health concerns or questions, don't hesitate to reach out to a healthcare professional. They can provide personalized guidance.",
               ]
        return np.random.choice(lst)
