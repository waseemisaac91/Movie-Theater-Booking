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
        "seats": auditorium_capacity,
        "sold": 0          # <-- add this line
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
    tickets: list of dicts, e.g. [{"movie": ..., "showtime": ..., "quantity": ...}]
    snacks: list of tuples (name, quantity, unit_price)
    """
    return {
        "customer": customer_name,
        "tickets": [],
        "snacks": []
    }


def book_tickets(order, movie_title, showtime_index, quantity, movies_db):
    """
    Feature 3: Books tickets for a selected movie and showtime.
    - MUST NOT crash if requested seats > available seats.
    - Decreases available seats (via 'sold') when the booking succeeds.
    Returns True on success, False on failure (never raises an exception).
    """
    # 1. Movie must exist
    if movie_title not in movies_db:
        print(f"\nError: Movie '{movie_title}' does not exist in the system.\n")
        return False

    showtimes = movies_db[movie_title]["showtimes"]

    # 2. Showtime index must be valid
    if not (0 <= showtime_index < len(showtimes)):
        print("\nError: That showtime does not exist for this movie.\n")
        return False

    showtime = showtimes[showtime_index]
    seats_available = showtime["seats"] - showtime["sold"]

    # 3. Quantity must be sane
    if quantity <= 0:
        print("\nError: Number of tickets must be at least 1.\n")
        return False

    # 4. Enough seats left? (the core requirement)
    if quantity > seats_available:
        print(f"\nError: Only {seats_available} seat(s) left for "
              f"'{movie_title}' at {showtime['time']}.\n")
        return False

    # 5. All checks passed -> commit the booking
    showtime["sold"] += quantity
    order["tickets"].append({
    "movie": movie_title,
    "showtime": showtime,
    "quantity": quantity
})

    print(f"\nBooked {quantity} ticket(s) for '{movie_title}' at {showtime['time']}.\n")
    return True


def add_snack_to_order(order, snack_menu, snack_name, quantity):
    """
    Feature 4: Adds snack bar items to the active customer order.
    - Must handle invalid snack choices gracefully (no crash).
    Returns True on success, False on failure.
    """
    # 1. Snack must exist on the menu
    if snack_name not in snack_menu:
        print(f"\nError: '{snack_name}' is not on the snack menu.\n")
        return False

    # 2. Quantity must be sane
    if quantity <= 0:
        print("\nError: Quantity must be at least 1.\n")
        return False

    # 3. Add to order
    price = snack_menu[snack_name]
    order["snacks"].append((snack_name, quantity, price))
    print(f"\nAdded {quantity} x {snack_name} to the order.\n")
    return True

# ==========================================
# Waseem: FEATURES 5, 6, 7 (Checkout & Reports)
# ==========================================

def calculate_fees_recursive(subtotal, fee_rates=(0.05, 0.02, 0.01)):
    if len(fee_rates) == 0:

        return subtotal


    # Apply the first fee in the list to the current running total

    current_rate = fee_rates[0]

    new_amount = subtotal + (subtotal * current_rate)

    # Recursive case: apply the remaining fees to the new amount

    return calculate_fees_recursive(new_amount, fee_rates[1:])

def calculate_order_subtotal(order, movies_db, snack_menu):

    # tickets: sum(quantity * price) over every booked ticket line
        ticket_costs = list(map(
            lambda t: t["quantity"] * t["showtime"]["price"],
            order.get("tickets", [])
        ))
        ticket_total = reduce(lambda acc, c: acc + c, ticket_costs, 0.0)
    
        # snacks: tuples (name, quantity, price)
        snack_costs = list(map(lambda s: s[1] * s[2], order.get("snacks", [])))
        snack_total = reduce(lambda acc, c: acc + c, snack_costs, 0.0)
    
        return ticket_total + snack_total


def print_receipt(customer_name, tickets_info, snacks_list, subtotal, final_total):

    WIDTH = 30
    LABEL_WIDTH = 22

    print("=" * 10 + " RECEIPT " + "=" * 10)
    print(f"Customer: {customer_name}")
    print("-" * WIDTH)

    for t in tickets_info:
        label = f"{t['movie']} ({t['showtime']['time']}) x{t['quantity']}"
        amount = f"${t['quantity'] * t['showtime']['price']:.2f}"
        print(f"{label:<{LABEL_WIDTH}}{amount:>8}")

    for name, qty, price in snacks_list:
        label = f"{name} x{qty}"
        amount = f"${qty * price:.2f}"
        print(f"{label:<{LABEL_WIDTH}}{amount:>8}")

    print("-" * WIDTH)
    print(f"{'Subtotal:':<{LABEL_WIDTH}}{'$' + format(subtotal, '.2f'):>8}")
    print(f"{'Total with fees:':<{LABEL_WIDTH}}{'$' + format(final_total, '.2f'):>8}")
    print("=" * WIDTH)



def checkout(order, movies_db, customers_db, snack_menu):

    customer_name = order.get("customer")
    tickets = order.get("tickets", [])
    snacks = order.get("snacks", [])

    if not tickets:
        print("⚠️  Cannot check out: no tickets have been booked for this order yet.")
        return None

    subtotal = calculate_order_subtotal(order, movies_db, snack_menu)
    final_total = calculate_fees_recursive(subtotal)

    print_receipt(customer_name, tickets, snacks, subtotal, final_total)

    # NOTE: seats/sold were already updated inside book_tickets() —
    # do NOT touch them again here, or you'd double-count.

    order_record = {
        "tickets": [
            {"movie": t["movie"], "time": t["showtime"]["time"], "quantity": t["quantity"]}
            for t in tickets
        ],
        "snacks": [{"name": n, "quantity": q, "line_total": q * p} for n, q, p in snacks],
        "subtotal": subtotal,
        "total": final_total,
    }
    customers_db.setdefault(customer_name, []).append(order_record)
    return order_record

def get_customer_history(customers_db, customer_name):

    history = customers_db.get(customer_name)

    if not history:
        print(f"No order history found for customer '{customer_name}'.")
        return []

    print(f"=== Order History for {customer_name} ===")
    for i, past_order in enumerate(history, start=1):
        movies_str = ", ".join(
            f"{t['movie']} ({t['quantity']})" for t in past_order["tickets"]
        )
        print(f"{i}. {movies_str} - Total: ${past_order['total']:.2f}")

    return history


def get_popularity_report(movies_db, top_n=5):

    """

    Feature 7: Generates a top-selling movies report ranked by tickets sold.

    """

    def total_sold_for_movie(showtimes):

        return reduce(lambda acc, st: acc + st.get("sold", 0), showtimes, 0)

    # map(): (title, total_tickets_sold) for every movie

    sales = list(

        map(

            lambda entry: (entry[0], total_sold_for_movie(entry[1].get("showtimes", []))),

            movies_db.items(),

        )

    )


    # filter(): only keep movies that have actually sold at least one ticket

    sold_movies = list(filter(lambda pair: pair[1] > 0, sales))

    # sort by tickets sold, highest first

    ranked = sorted(sold_movies, key=lambda pair: pair[1], reverse=True)

    top_movies = ranked[:top_n]

    if not top_movies:

        print("No ticket sales have been recorded yet.")

        return []

    print("=== Top-Selling Movies ===")

    for rank, (title, sold) in enumerate(top_movies, start=1):

        print(f"{rank}. {title} - {sold} ticket(s) sold")


    return top_movies


# ==========================================
# MAIN INTERACTIVE MENU (CLI)
# ==========================================

def main():

        print("=== Downtown Cinema Management System ===")
    
        num_movies = int(input("How many movies do you want to add? "))
        for _ in range(num_movies):
            title = input("\nEnter the movie title: ")
            genres = input("Enter genres separated by commas: ").split(",")
    
            num_showtimes = int(input("How many showtimes for this movie? "))
            showtimes = []
            for s in range(num_showtimes):
                print(f" Showtime #{s}:")
                st_time = input("  Start time (e.g. 19:30): ")
                price = float(input("  Ticket price: "))
                seats = int(input("  Number of seats: "))
                st = add_showtime(st_time, price, seats)
                if st is not None:
                    showtimes.append(st)
                else:
                    print("  (Invalid price/seats — showtime skipped)")
    
            add_movie(MOVIES_DB, title, genres, showtimes)
    
        print("\nCurrent movies:")
        for m in MOVIES_DB.values():
            print(f"- {m['title']} | genres: {m['genres']}")
            for idx, st in enumerate(m["showtimes"]):
                print(f"    [{idx}] {st['time']} - ${st['price']:.2f} - {st['seats']} seats")
    
        genre_name = input("\nEnter the genre you want to search for: ")
        print(search_by_genre(MOVIES_DB, genre_name))
    
        max_price = input("Enter the max price you want to search for: ")
        print(search_by_max_price(MOVIES_DB, max_price))
    
        # --- Booking + snacks ---
        customer_name = input("\nEnter the customer name for this order: ")
        active_order = create_active_order(customer_name)
    
        movie_title = input("Enter the movie title to book: ")
        if movie_title in MOVIES_DB:
            n_showtimes = len(MOVIES_DB[movie_title]["showtimes"])
            showtime_index = int(input(f"Enter the showtime index (0-{n_showtimes-1}): "))
        else:
            showtime_index = int(input("Enter the showtime index: "))
        quantity = int(input("Enter number of tickets: "))
        book_tickets(active_order, movie_title, showtime_index, quantity, MOVIES_DB)
    
        snack_name = input("Enter a snack name to add (leave blank to skip): ")
        if snack_name:
            snack_qty = int(input("Enter snack quantity: "))
            add_snack_to_order(active_order, SNACK_MENU, snack_name, snack_qty)
    
        # --- Checkout + reports ---
        checkout(active_order, MOVIES_DB, CUSTOMERS_DB, SNACK_MENU)
        get_customer_history(CUSTOMERS_DB, customer_name)
        get_popularity_report(MOVIES_DB)


if __name__ == "__main__":
    main()

