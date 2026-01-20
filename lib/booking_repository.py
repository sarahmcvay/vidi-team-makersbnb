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
                str(row["start_date"]),
                str(row["end_date"]),
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
            str(row["start_date"]),
            str(row["end_date"]),
            row["flag"],
            row["user_id"],
            row["space_id"]
        )