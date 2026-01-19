USERS
- id
- Name
- Email
- Password (hashed) 
- FK booking_id
- FK - space_id

SPACES
-id
- Name
- Price 
- Description
- img link
FK user_id(?)

 BOOKINGS
- id
- start_date
- end_date 
- status (pending, accepted, rejected)
FK - space_id
FK - user_id

constraint fk_post foreign key(post_id) references posts(id) on delete cascade