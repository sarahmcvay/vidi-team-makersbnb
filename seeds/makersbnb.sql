DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE,
    password VARCHAR(255)
);

CREATE SEQUENCE IF NOT EXISTS spaces_id_seq;
CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(8,2),
    details TEXT,
    img_link TEXT,
    user_id INTEGER
);

CREATE SEQUENCE IF NOT EXISTS bookings_id_seq;
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    flag VARCHAR(255),
    user_id INTEGER,
    space_id INTEGER
);

-- seed data

INSERT INTO spaces (name, price, details, img_link, user_id) VALUES
    ('Cosy 4 bedroom Cabin in the Woods', 100.00, 'Escape the noise and reconnect with nature in our charming, four-bedroom cabin tucked away in a private grove of towering pines. Whether you''re planning a multi-generational family getaway or a quiet retreat with friends, this is your perfect basecamp for forest adventures and fireside stories.', 'https://plus.unsplash.com/premium_photo-1689609950112-d66095626efb?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8aG91c2V8ZW58MHx8MHx8fDA%3D', 1),
    ('6 Bedrooms Rustic Lakeside Escape', 200.00, 'Reconnect with what matters at this expansive six-bedroom retreat, perfectly perched on the water''s edge where the forest meets the shore. Designed for large families and groups who crave both space and togetherness, this rustic escape offers a front-row seat to golden sunrises and the gentle rhythm of lake life.', 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8aG91c2V8ZW58MHx8MHx8fDA%3D', 2),
    ('Ultra Modern 3 Bedroom Penthouse with a Swimming Pool.', 300.00, 'Elevate your perspective in this stunning three-bedroom penthouse, where cutting-edge architecture meets the clouds. Bathed in floor-to-ceiling glass and featuring a private, heated infinity pool overlooking the city lights', 'https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8aG91c2V8ZW58MHx8MHx8fDA%3D', 3);

INSERT INTO bookings (start_date, end_date, flag, user_id, space_id) VALUES
    ('2026-02-10', '2026-02-11', 'pending', 1, 2),
    ('2026-03-15', '2026-03-17', 'rejected', 2, 1),
    ('2026-01-24', '2026-01-26', 'accepted', 3, 3);
-- The booking table is seperate from the space, it is pending, approved or rejected.
