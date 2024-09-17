class Characters:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.dialogue = None

    def describe(self):
        print(self.name, " is here")
        print(self.description)

    def set_character(self, race):
        self.race = race

    def get_character(self):
        if self.race == "dwarf":
            print(
                "You have chosen senshi, a "
                + self.race
                + ". He is a warrior and a crafter of many weaponds!!!"
            )
        elif self.race == "Elf":
            print(
                "You have chosen marcell, a"
                + self.race
                + ". She is a Expert Level magic caster and a master of explosion magic"
            )
        else:
            print("The race is not a playable character")

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " do not speak to me FOOL!!!!")

    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)


class Enemy(Characters):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, weakness):
        self.weakness = weakness

    def get_weakness(self):
        return self.weakness

    def displayed_weakness(self):
        print("it's weakness is :", self.weakness)

    def fight(self, combat_item):
        if combat_item == self.weakness:
            print(
                "You have successfully defeated " + self.name + " with " + combat_item
            )
            return True
        else:
            print("Your attack was ineffective against " + self.name)
            return False
