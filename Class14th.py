class FortniteBot:

    def __init__(self, bot_name): #constructor
        self.health = 100 #attribute

    def take_damage(self, amount): #method
        self.health -= amount