from lib.booking_repository import BookingRepository
from lib.booking import Booking
from datetime import date 

"""
When we call #all, 
We return a list of all the booking objects reflecting the seed data
"""
def test_get_all_bookings(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)

    bookings = repository.all()

    assert bookings == [
        Booking(1, date(2026, 2, 10), date(2026, 2, 11), 'pending', 1, 2),
        Booking(2, date(2026, 3, 15), date(2026, 3, 17), 'rejected', 2, 1),
        Booking(3, date(2026, 1, 24), date(2026, 1, 26), 'accepted', 3, 3),
    ]

"""
When we call #find, 
We can find and then return a single booking object, reflecting the seed data
"""
def test_find_single_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)

    item = repository.find(1)
    assert item == Booking(1, date(2026, 2, 10), date(2026, 2, 11), 'pending', 1, 2)

"""
When we call #create, 
We can create a new booking object, which will be reflected in the data
"""
def test_create_new_booking(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)
    new_booking = repository.create(Booking(None, '2026-04-12', '2026-04-14', 'pending', 4, 3))

    assert new_booking == Booking(4, '2026-04-12', '2026-04-14', 'pending', 4, 3)

    bookings = repository.all()
    assert bookings == [
        Booking(1, date(2026, 2, 10), date(2026, 2, 11), 'pending', 1, 2),
        Booking(2, date(2026, 3, 15), date(2026, 3, 17), 'rejected', 2, 1),
        Booking(3, date(2026, 1, 24), date(2026, 1, 26), 'accepted', 3, 3),
        Booking(4, date(2026, 4, 12), date(2026, 4, 14), 'pending', 4, 3),
    ]

"""
when we pass in a list of space ids
we return the list of those space bookings with pending flag 
"""
def test_get_pending_bookings_by_space_id(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = BookingRepository(db_connection)

    test_space_ids =[2]
    pending_bookings = repository.get_pending_bookings_by_space_id(test_space_ids)
    assert pending_bookings == [Booking(1, date(2026, 2, 10), date(2026, 2, 11), 'pending', 1, 2)]

    repository.create(Booking(None, '2026-04-12', '2026-04-14', 'pending', 4, 3))

    test_space_ids =[1, 2, 3]
    pending_bookings = repository.get_pending_bookings_by_space_id(test_space_ids)
    assert pending_bookings == [Booking(1, date(2026, 2, 10), date(2026, 2, 11), 'pending', 1, 2), Booking(4, date(2026, 4, 12), date(2026, 4, 14), 'pending', 4, 3)]
