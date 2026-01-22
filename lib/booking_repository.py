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
        rows = self._connection.execute(
            'INSERT INTO bookings (start_date, end_date, flag, user_id, space_id) VALUES (%s, %s, %s, %s, %s) RETURNING id', [booking.start_date, booking.end_date, booking.flag, booking.user_id, booking.space_id]
        )
        row = rows[0]
        booking.id = row["id"]
        return booking
    #date values returned as a string not date objects

    # As the guest, see all my bookings in the booking bit of the dashboard.
    def get_bookings_by_guest_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM bookings WHERE user_id = %s',
            [user_id]
        )
        bookings = []
        for row in rows:
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

    def get_pending_bookings_by_space_id(self, bookable_spaces):
        pending_bookings = []
        for space_id in bookable_spaces:
            print(space_id)
            rows = self._connection.execute(
            "SELECT * FROM bookings WHERE space_id = %s AND flag = 'pending'",
            [space_id]
            )
            print(rows)
            for row in rows:
                item = Booking(
                row["id"],
                row["start_date"],
                row["end_date"],
                row["flag"],
                row["user_id"],
                row["space_id"]
                )
                pending_bookings.append(item)
        return pending_bookings
      # now lists every pending booking under space_id
      
    def update_flag(self, booking_id, new_flag):
        self._connection.execute('UPDATE bookings SET flag = %s WHERE id = %s', (new_flag, booking_id))
    # now lists every pending booking under space_id

    def price_of_booking(self, space_id):
        pass