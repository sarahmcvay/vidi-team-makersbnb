from datetime import date, timedelta
from lib.booking import Booking
import calendar

def parse_date(value):
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)

def ensure_date(value):
    if isinstance(value, date):
        return value
    return date.fromisoformat(value)


def booking_dates(booking):
    start = ensure_date(booking.start_date)
    end = ensure_date(booking.end_date)

    current = start
    dates = []

    while current < end:
        dates.append(current)
        current += timedelta(days=1)

    return dates


def calendar_dates_by_status(bookings, space_id):
    approved = []
    pending = []

    for booking in bookings:
        if booking.space_id != space_id:
            continue

        for d in booking_dates(booking):
            if booking.flag == "accepted":
                approved.append(d.isoformat())
            elif booking.flag == "pending":
                pending.append(d.isoformat())

    return approved, pending


def unavailable_dates(bookings):
    unavailable = set()

    for booking in bookings:
        for d in booking_dates(booking):
            unavailable.add(d)

    return unavailable


def unavailable_dates_for_space(bookings, space_id):
    space_bookings = [
        b for b in bookings if b.space_id == space_id
    ]
    return unavailable_dates(space_bookings)


def month_calendar(year, month, unavailable_dates):
    _, days_in_month = calendar.monthrange(year, month)

    return [
        {
            "date": date(year, month, day),
            "available": date(year, month, day) not in unavailable_dates
        }
        for day in range(1, days_in_month + 1)
    ]