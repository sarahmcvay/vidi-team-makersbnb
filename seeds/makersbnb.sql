DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
DROP TABLE IF EXISTS spaces;
DROP SEQUENCE IF EXISTS spaces_id_seq;
DROP TABLE IF EXISTS bookings;
DROP SEQUENCE IF EXISTS bookings_id_seq;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

CREATE TABLE spaces (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    price DECIMAL(8,2),
    description TEXT,
    img_link TEXT,
    user_id INTEGER
);

CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE,
    status VARCHAR(255),
    user_id INTEGER,
    space_id INTEGER
);
