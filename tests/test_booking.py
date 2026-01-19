from lib.booking import Booking

def test_booking_constructs():
    booking = Booking(1, "2026-01-01", "2026-01-02", "Test", 1, 1)
    assert booking.id == 1
    assert booking.start_date == "2026-01-01"
    assert booking.end_date == "2026-01-02"
    assert booking.flag == "Test"
    assert booking.user_id == 1
    assert booking.space_id == 1

def test_artists_format_nicely():
    booking = Booking(1, "2026-01-01", "2026-01-02", "Test", 1, 1)
    assert str(booking) == "Booking(1, 2026-01-01, 2026-01-02, Test, 1, 1)"

def test_bookings_are_equal():
    booking1 = Booking(1, "2026-01-01", "2026-01-02", "Test", 1, 1)
    booking2 = Booking(1, "2026-01-01", "2026-01-02", "Test", 1, 1)
    assert booking1 == booking2