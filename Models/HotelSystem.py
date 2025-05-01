# Define el HotelSystem class
class HotelSystem:
    # Initialize el HotelSystem object
    def __init__(self):
        # Create an empty list to 34an n3mel store lel objects
        self.rooms = []
        #  Create an empty list to 34an n3mel store lel objects
        self.guests = []
        #  Create an empty list to 34an n3mel store lel objects
        self.reservations = []

    # n3mel method 34an ndawar 3la el reservation by name
    def find_reservation_by_name(self, name):
        # ndawar f kol el names b for loop
        for i in self.reservations:
            # n5aly el name kolo lowercase
            if name.lower() in i.guest.full_name.lower():
                # return el name lw nafso
                return i
        # Return wla 7aga lw m4 mawgood
        return None

    # Define method 34an n find reservation b el id
    def find_reservation_by_id(self, reservation_id):
        # n dawar f el list 3la el id using for loop
        for r in self.reservations:
            # Check lw el id matches el id ely badawar 3aleh
            if r.reservation_id == reservation_id:
                # Return lw matches
                return r
        # Return None lw m4 mawgood
        return None

    # Define a method 34an kol el rooms 
    def list_available_rooms(self):
        # ndawar f kol el rooms 
        for i in self.rooms:
            # Check if el room fadya
            if not i.is_occupied:
                # Print room's information
                print(i.get_room_info())

    #method to generate a bill for a reservation
    def generate_bill(self, reservation_id):
        # Find the reservation object using the provided reservation ID
        reservation = self.find_reservation_by_id(reservation_id)
        # Check if the reservation exists
        if reservation is not None:
            # Calculate and return the total bill for the reservation
            return reservation.calculate_total()
        else:
            # Return 0 if the reservation does not exist
            return 0

    # Define a method to generate a report of room occupancy
    def get_occupancy_report(self):
        # Initialize a counter for the total number of rooms
        total = 0
        # Initialize a counter for the number of occupied rooms
        occupied = 0
        # Iterate through all rooms in the rooms list
        for room in self.rooms:
            # Increment the total room counter
            total = total + 1
            # Check if the room is occupied
            if room.is_occupied:
                # Increment the occupied room counter
                occupied = occupied + 1
        # Return a formatted string showing the number of occupied and total rooms
        return "Occupied Rooms: " + str(occupied) + " / Total Rooms: " + str(total)
