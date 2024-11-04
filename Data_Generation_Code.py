import csv


def generate_reservation_data(num_rows, guest_ids, room_numbers):
    reservations = []
    for i in range(1, num_rows + 1):
        reservation = [
            i,  
            random.choice(guest_ids), 
            random.choice(room_numbers),  
            (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),  
            (datetime.now() + timedelta(days=random.randint(2, 10))).strftime('%Y-%m-%d'), 
            round(random.uniform(50, 500), 2) 
        ]
        reservations.append(reservation)
    return reservations

def generate_hotel_data(num_rows):
    hotels = []
    for i in range(1, num_rows + 1):
        hotel = [
            i,  
            f"Hotel {i}",
            f"{random.randint(100, 999)} {random.choice(['Main', 'Elm', 'Oak', 'Maple'])} St",
            f"{random.randint(1000000000, 9999999999)}",
            f"info{random.randint(100, 999)}@hotel{i}.com",
            random.randint(1, 5),
            f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}",
            f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}"
        ]
        hotels.append(hotel)
    return hotels

def generate_guest_data(num_rows):
    guests = []
    for i in range(1, num_rows + 1):
        guest = [
            i,  
            f"Guest {i}",
            f"Smith{i}",
            f"guest{i}@example.com",
            f"{random.randint(100000000, 999999999)}",
            f"{random.randint(1950, 2000)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
        ]
        guests.append(guest)
    return guests

def generate_reservation_data(num_rows, guest_ids, room_numbers):
    reservations = []
    for i in range(1, num_rows + 1):
        reservation = [
            i, 
            random.choice(guest_ids),
            random.choice(room_numbers),
            (datetime.now() + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
            (datetime.now() + timedelta(days=random.randint(2, 10))).strftime('%Y-%m-%d'),
            round(random.uniform(50, 500), 2)
        ]
        reservations.append(reservation)
    return reservations


def generate_room_data(num_rows, type_ids):
    rooms = []
    for i in range(1, num_rows + 1):
        room = [
            i,  
            random.choice(type_ids),  
            random.choice([True, False]),  
            random.choice(['City View', 'Sea View', 'Mountain View']),  
            random.choice(['Available', 'Occupied'])
        ]
        rooms.append(room)
    return rooms


def generate_room_type_data(num_rows):
    room_types = []
    for i in range(1, num_rows + 1):
        room_type = [
            i,  
            f"Room Type {i}",
            f"Description of room type {i}",
            random.randint(1, 6),
            round(random.uniform(50, 500), 2)
        ]
        room_types.append(room_type)
    return room_types


def generate_staff_data(num_rows, hotel_ids):
    staff = []
    for i in range(1, num_rows + 1):
        staff_member = [
            i,  
            f"Staff {i}", 
            f"Smith {i}",  
            random.choice(['Manager', 'Receptionist', 'Chef']),
            random.choice(hotel_ids)  
        ]
        staff.append(staff_member)
    return staff


def generate_amenity_data():
    amenities = [["Pool"], ["Gym"], ["Spa"]]
    return amenities

def generate_menu_data():
    menus = []
    menu_types = ["Breakfast", "Lunch", "Dinner"]
    for i, menu_type in enumerate(menu_types, start=1):
        menu = [
            i, 
            menu_type,
            f"{menu_type} Menu"
        ]
        menus.append(menu)
    return menus


def generate_food_item_data(num_rows, valid_menu_ids):
    food_items = []
    for i in range(1, num_rows + 1):
        menu_id = random.choice(valid_menu_ids) if valid_menu_ids else None

        food_item = [
            i,  
            f"Food Item {i}",
            f"Description of food item {i}",
            round(random.uniform(5, 50), 2),
            random.choice(["Appetizer", "Main Course", "Dessert"]),
            menu_id
        ]
        food_items.append(food_item)
    return food_items


from datetime import datetime, timedelta

def generate_order_data(num_rows, guest_ids, reservation_ids):
    orders = []
    for i in range(1, num_rows + 1):
        order = [
            i,  # order_id
            random.choice(guest_ids),
            random.choice(reservation_ids),
            (datetime.now() + timedelta(days=random.randint(1, 30))).strftime('%Y-%m-%d'),
            f"{random.randint(0, 23)}:{random.randint(0, 59)}:{random.randint(0, 59)}",
            random.choice(["Pending", "Confirmed", "Cancelled"])
        ]
        orders.append(order)
    return orders


import random

def generate_order_items_data(num_rows, order_ids, food_ids):
    order_items = []
    for i in range(1, num_rows + 1):
        order_item = [
            i,  
            random.choice(food_ids),
            random.randint(1, 5),
            round(random.uniform(5, 50), 2)
        ]
        order_items.append(order_item)
    return order_items




def write_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

# Generate data
num_rows = 3000

hotel_data = generate_hotel_data(num_rows)
guest_data = generate_guest_data(num_rows)
room_data = generate_room_data(num_rows, list(range(1, num_rows + 1)))
room_type_data = generate_room_type_data(num_rows)
staff_data = generate_staff_data(num_rows, list(range(1, num_rows + 1)))
amenity_data = generate_amenity_data()
menu_data = generate_menu_data()
food_item_data = generate_food_item_data(num_rows, list(range(1, 2)))
order_data = generate_order_data(num_rows, list(range(1, num_rows + 1)), list(range(1, num_rows + 1)))
order_items_data = generate_order_items_data(num_rows, list(range(1, num_rows + 1)), list(range(1, num_rows + 1)))
reservation_data = generate_reservation_data(num_rows, list(range(1, num_rows + 1)), list(range(1, num_rows + 1)))


write_to_csv(hotel_data, 'Hotel.csv')
write_to_csv(guest_data, 'Guest.csv')
write_to_csv(room_data, 'Room.csv')
write_to_csv(room_type_data, 'Room_Type.csv')
write_to_csv(staff_data, 'Staff.csv')
write_to_csv(amenity_data, 'Amenity.csv')
write_to_csv(menu_data, 'Menu.csv')
write_to_csv(food_item_data, 'Food_Item.csv')
write_to_csv(order_data, 'Order.csv')
write_to_csv(order_items_data, 'Order_Items.csv')
write_to_csv(reservation_data, 'Reservation.csv')

print("CSV files generated successfully!")
