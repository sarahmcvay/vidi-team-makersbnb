### Payment Planning  
Considered a few suppliers, decided on Stripe
change .gitignore stripe secret key and stripe perishable key

### Booking Flow Logic
- User (guest) requests booking
- User (host) approves booking
- User (guest) booking is approved
- User (guest) goes to confirmation page, buttons to pay on arrival or pay now. 
    --> click "pay now" 
    --> Flask backend creates Stripe Checkout Session
- User (guest) pays 
    --> Payment completed
    --> Stripe redirectos to success 
- User (guest) final confirmation recieved. 
- Booking marked as "paid"

### Database Change 
```SQL
ALTER TABLE bookings
ADD COLUMN payment_status VARCHAR(225) DEFAULT 'unpaid' -- unpaid / paid
ADD COLUMN strip_session_id VARCHAR(225)
```

### Test Cards
4242 4242 4242 4242 
any date / any CVC

