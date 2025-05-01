class Room:
    def init(self, room_id, room_type, room_floor, room_number, price_per_night, available):
        self.room_id = room_id
        self.room_type = room_type
        self.room_floor = room_floor
        self.room_number = room_number
        self.price_per_night = price_per_night
        self.available = available

    def mark_as_occupied(self):
        self.available = False

    def mark_available(self):
        self.available = True

    def get_room_info(self):
        return {
            "Room ID": self.room_id,
            "Room Type": self.room_type,
            "Room Floor": self.room_floor,
            "Room Number": self.room_number,
            "Price Per Night": self.price_per_night,
            "Available": self.available
        }
class Payment:
    def init(self, payment_id: int, room: Room, amount: float):
        self.payment_id = payment_id
        self.room = room
        self.amount = amount

    def get_payment_info(self):
        return {
            "Payment ID": self.payment_id,
            "Room ID": self.room.room_id,
            "Amount": self.amount
        }