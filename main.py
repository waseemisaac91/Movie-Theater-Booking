"""
Movie Theater Booking System
Starter Code Template
"""

from functools import reduce

# ==========================================
# GLOBAL DATA STRUCTURES
# ==========================================

# MOVIES structure: dict with movie titles as keys
# Genres use a set() to prevent duplicates. Showtimes use tuples/dicts.
MOVIES_DB = {}

# SNACK_MENU: dict of item name -> price
SNACK_MENU = {
    "Popcorn (Large)": 6.00,
    "Popcorn (Small)": 4.00,
    "Cola": 3.50,
    "Water": 2.00,
    "Candy": 3.00
}

# CUSTOMERS_DB: dict mapping customer name -> list of past order dicts
CUSTOMERS_DB = {}


# ==========================================
# MOHAMMED: FEATURES 1 & 2 (Movies & Search)
# ==========================================

def add_movie(movies_db, title, genres, showtimes):
    """
    Feature 1: Adds a new movie to the system.
    - genres: should be converted to/stored as a set() to prevent duplicate genres.
    - showtimes: list of dicts, e.g., [{"time": "19:30", "price": 10.0, "seats": 50, "sold": 0}]
    """
    formatted_showtimes = []
    
    for showtime_data in showtimes:
        new_showtime = add_showtime(
            showtime_data["time"],
            showtime_data["price"],
            showtime_data["seats"]
        )

        if new_showtime is not None:
            formatted_showtimes.append(new_showtime)

    movie_information = {
        "title": title,
        "genres": set(genres),
        "showtimes": formatted_showtimes
    }

    MOVIES_DB[title] = movie_information

    return movie_information

def add_showtime(start_time, ticket_price, auditorium_capacity):
    """
    Feature 1 Helper: Creates and returns a single showtime dictionary/tuple.
    """
    if ticket_price <= 0:
        return None

    if auditorium_capacity <= 0 or auditorium_capacity > 100:
        return None

    showtime= {
        "time": start_time,
        "price": ticket_price,
        "seats": auditorium_capacity
    }
    return showtime

def search_by_genre(movies_db, genre_name):
    """
    Feature 2: Returns a list of movies matching a genre.
    - Must use filter() or lambda.
    - Must gracefully return an empty list/message if genre doesn't exist.
    """
    genre_name= genre_name.lower()
    result= list(filter(lambda movie: genre_name in movie["genres"], 
                        MOVIES_DB.values()))
    return result

def search_by_max_price(movies_db, max_price):
    """
    Feature 2: Returns showtimes/movies priced at or below max_price.
    - Must use filter() and lambda.
    """
    max_price= float(max_price)
    result_price= list(filter(lambda movie: any(showtime["price"] <= max_price
                                                for showtime in movie["showtimes"]),
                                                MOVIES_DB.values()))
    return result_price


# ==========================================
# DANA: FEATURES 3 & 4 (Booking & Snacks)
# ==========================================

def create_active_order(customer_name):
    """
    Initializes a new empty order dictionary for a customer.
    """
    pass

def book_tickets(order, movie_title, showtime_index, quantity, movies_db):
    """
    Feature 3: Books tickets for a selected movie and showtime.
    - MUST NOT crash if requested seats > available seats.
    - Must decrease available seats or mark them for checkout update.
    """
    pass

def add_snack_to_order(order, snack_menu, snack_name, quantity):
    """
    Feature 4: Adds snack bar items to the active customer order.
    - Must handle invalid snack choices gracefully.
    """
    pass


# ==========================================
# Waseem: FEATURES 5, 6, 7 (Checkout & Reports)
# ==========================================

def calculate_fees_recursive(subtotal, fee_rates=[0.05, 0.02, 0.01]):
    """
    Feature 5 (Course Requirement): RECURSIVE function to calculate fee total.
    - Step 1: Apply 5% service fee on subtotal.
    - Step 2: Apply 2% booking fee on new amount.
    - Step 3: Apply 1% city tax on new amount.
    Base case: fee_rates list is empty.
    """
    pass

def calculate_order_subtotal(order):
    """
    Feature 5 Helper: Calculates subtotal using map() / reduce() or lambda.
    - Sum of (ticket_quantity * ticket_price) + sum of snack items.
    """
    pass

def print_receipt(customer_name, movie_info, tickets_info, snacks_list, subtotal, final_total):
    """
    Feature 5: Displays neatly formatted itemized receipt aligned in columns.
    """
    pass

def checkout(order, movies_db, customers_db):
    """
    Feature 5: Completes order payment, prints receipt, updates seat count,
    updates total movie sales, and saves order to customer history.
    - MUST NOT crash if no movie is selected in the order yet.
    """
    pass

def get_customer_history(customers_db, customer_name):
    """
    Feature 6: Pulls up customer history.
    - MUST NOT crash if customer does not exist in system.
    """
    pass

def get_popularity_report(movies_db):
    """
    Feature 7: Generates top-selling movies report ranked by tickets sold.
    - Use map(), reduce(), or lambda sorting.
    """
    pass


# ==========================================
# MAIN INTERACTIVE MENU (CLI)
# ==========================================

def main():
    print("=== Downtown Cinema Management System ===")
    # Interactive menu loop goes here
    
    # add movie and showtime
    for i in range(3):
        new_showtime =add_showtime(
            input("Enter the start time: "),
            float(input("Enter the ticket price: ")),
            int(input("Enter the number of seats: ")))
        added_movie = add_movie(
            MOVIES_DB,
            input("Enter the movie title: "),
            input("Enter genres separated by commas: ").split(","),
            [new_showtime])
    

        print(added_movie)
    print(MOVIES_DB)

    # search genre
    genre_name = input("Enter the genre you want to search for: ")
    result = search_by_genre(MOVIES_DB, genre_name)
    print(result)

    # search max price
    max_price = input("Enter the max price you want to search for: ")
    result_price = search_by_max_price(MOVIES_DB, max_price)
    print(result_price)

if __name__ == "__main__":
    main()
