from lib.booking import Booking

class BookingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self): 
        rows = self._connection.execute(
            'SELECT * FROM bookings'
        )
        bookings = []
        for row in rows:
            # print(type(row["start_date"]))

            item = Booking(
                row["id"],
                row["start_date"],
                row["end_date"],
                row["flag"],
                row["user_id"],
                row["space_id"]
            )
            bookings.append(item)
        return bookings
    
    def find(self, booking_id):
        rows = self._connection.execute(
            'SELECT * FROM bookings WHERE id = %s',
            [booking_id]
        )
        row = rows[0]
        return Booking(
            row["id"],
            row["start_date"],
            row["end_date"],
            row["flag"],
            row["user_id"],
            row["space_id"]
        )

    def create(self, booking):
        self._connection.execute(
            'INSERT INTO bookings (start_date, end_date, flag, user_id, space_id) VALUES (%s, %s, %s, %s, %s)', [booking.start_date, booking.end_date, booking.flag, booking.user_id, booking.space_id]
        )
        return None