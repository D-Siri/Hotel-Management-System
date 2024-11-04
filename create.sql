-- Hotel Table
CREATE TABLE Hotel (
    hotel_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(15),
    email VARCHAR(255),
    stars INT,
    checkin_time TIME,
    checkout_time TIME
);

-- Guest Table
CREATE TABLE Guest (
    guest_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(15),
    date_of_birth DATE
);

-- Reservation Table
CREATE TABLE Reservation (
    booking_id SERIAL PRIMARY KEY,
    guest_id INT REFERENCES Guest(guest_id) ON DELETE CASCADE,
    room_number INT REFERENCES Room(room_number) ON DELETE CASCADE,
    check_in DATE,
    check_out DATE,
    total_price DECIMAL
);

-- Room Table
CREATE TABLE Room (
    room_number SERIAL PRIMARY KEY,
    type_id INT REFERENCES Room_Type(type_id),
    smoking BOOLEAN,
    view VARCHAR(255),
    availability VARCHAR(50)
);

-- Room Type Table
CREATE TABLE Room_Type (
    type_id SERIAL PRIMARY KEY,
    type_name VARCHAR(255),
    description VARCHAR(255),
    capacity INT,
    price DECIMAL
);

-- Staff Table
CREATE TABLE Staff (
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    role VARCHAR(255),
    hotel_id INT REFERENCES Hotel(hotel_id) ON DELETE RESTRICT
);

-- Amenity Table
CREATE TABLE Amenity (
    amenity VARCHAR(255) PRIMARY KEY
);

-- Menu Table
CREATE TABLE Menu (
    menu_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    menu_type VARCHAR(255)
);

-- Food Item Table
CREATE TABLE Food_Item (
    food_id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    price DECIMAL,
    category VARCHAR(255),
    menu_id INT REFERENCES Menu(menu_id) ON DELETE CASCADE
);

-- Order Table
CREATE TABLE "Order" (
    order_id SERIAL PRIMARY KEY,
    guest_id INT REFERENCES Guest(guest_id) ON DELETE CASCADE,
    reservation_id INT REFERENCES Reservation(booking_id) ON DELETE RESTRICT,
    order_date DATE,
    order_time TIME,
    order_status VARCHAR(255)
);

-- Order Items Table (Junction Table)
CREATE TABLE Order_Items (
    order_id INT REFERENCES "Order"(order_id) ON DELETE CASCADE,
    food_id INT REFERENCES Food_Item(food_id) ON DELETE CASCADE,
    quantity INT,
    price DECIMAL,
    PRIMARY KEY (order_id, food_id)
);