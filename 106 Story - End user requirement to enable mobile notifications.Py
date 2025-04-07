106 Story - End user requirement to enable mobile notifications
class Guest:
    def __init__(self, name, room_number):
        self.name = name
        self.room_number = room_number

    def __str__(self):
        return f"{self.name} - Room {self.room_number}"

class Hotel:
    def __init__(self):
        self.guests = []

    def add_guest(self, name, room_number):
        self.guests.append(Guest(name, room_number))
        print(f"Guest {name} added to room {room_number}.")

    def update_room_number(self, guest_name, new_room_number):
        for guest in self.guests:
            if guest.name.lower() == guest_name.lower():
                print(f"Updating {guest.name}'s room from {guest.room_number} to {new_room_number}.")
                guest.room_number = new_room_number
                return
        print(f"No guest found with name {guest_name}.")

    def show_guest_list(self):
        print("\nCurrent Guest List:")
        for guest in self.guests:
            print(guest)
        print()

# Example usage
if __name__ == "__main__":
    hotel = Hotel()

    while True:
        print("\n1. Add Guest\n2. Update Room Number\n3. Show Guest List\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Guest Name: ")
            room = input("Enter Room Number: ")
            hotel.add_guest(name, room)
        elif choice == '2':
            name = input("Enter Guest Name to Update Room: ")
            new_room = input("Enter New Room Number: ")
            hotel.update_room_number(name, new_room)
        elif choice == '3':
            hotel.show_guest_list()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
