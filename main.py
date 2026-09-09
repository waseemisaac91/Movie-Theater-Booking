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
    pass

def add_showtime(start_time, ticket_price, auditorium_capacity):
    """
    Feature 1 Helper: Creates and returns a single showtime dictionary/tuple.
    """
    pass

def search_by_genre(movies_db, genre_name):
    """
    Feature 2: Returns a list of movies matching a genre.
    - Must use filter() or lambda.
    - Must gracefully return an empty list/message if genre doesn't exist.
    """
    pass

def search_by_max_price(movies_db, max_price):
    """
    Feature 2: Returns showtimes/movies priced at or below max_price.
    - Must use filter() and lambda.
    """
    pass


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
    pass

if _name_ == "_main_":
    main()
