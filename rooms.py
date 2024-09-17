class Rooms:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.character = None
        self.floor = None

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(self.description)

    def set_floor(self, room_floor):
        self.floor = room_floor

    def get_floor(self):
        return self.floor

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link
        print(self.name + "linked rooms:" + repr(self.linked_rooms))

    def get_details(self):
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character


class Command_center(Rooms):
    def __init__(self, room_name):
        super().__init__(room_name)
        self.name = room_name + " command center"

    def set_character(self, final_boss):
        return super().set_character(final_boss)

    def set_token(self, token):
        self.token = token

    def get_token(self):
        return self.token

    def set_description(self, command_center_description):
        return super().set_description(command_center_description)

    def get_description(self):
        return super().get_description()
