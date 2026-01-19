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
    email VARCHAR(255),
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
INSERT INTO users (name, email, password) VALUES
    ('test1', 'test1@email.com', 'test1password'),
    ('test2', 'test2@email.com', 'test2password'),
    ('test3', 'test3@email.com', 'test3password');

INSERT INTO spaces (name, price, details, img_link, user_id) VALUES
    ('space1', 10.00, 'great house', 'http123', 1),
    ('space2', 20.00, 'ok house', 'http456', 2),
    ('space3', 30.00, 'fun house', 'http789', 3);

INSERT INTO bookings (start_date, end_date, flag, user_id, space_id) VALUES
    ('2026-02-10', '2026-02-11', 'flag1', 1, 2),
    ('2026-03-15', '2026-03-17', 'flag2', 2, 1),
    ('2026-01-24', '2026-01-26', 'flag3', 3, 3);
-- The booking table is seperate from the space, it is pending, approved or rejected.

