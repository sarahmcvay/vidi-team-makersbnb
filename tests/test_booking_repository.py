from lib.booking_repository import BookingRepository
from lib.booking import Booking

"""
When we call #all, 
We return a list of all the booking objects reflecting the seed data
"""
def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)

    bookings = repository.all()

    assert bookings == [
        Booking(1, '2026-02-10', '2026-02-11', 'flag1', 1, 2),
        Booking(2, '2026-03-15', '2026-03-17', 'flag2', 2, 1),
        Booking(3, '2026-01-24', '2026-01-26', 'flag3', 3, 3),
    ]

"""
When we call #find, 
We can find and then return a single booking object, reflecting the seed data
"""
def test_find_single_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)

    item = repository.find(1)
    assert item == Booking(1, '2026-02-10', '2026-02-11', 'flag1', 1, 2)

