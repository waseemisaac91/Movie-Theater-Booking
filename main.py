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

def calculate_fees_recursive(subtotal, fee_rates=(0.05, 0.02, 0.01)):
    if len(fee_rates) == 0:

        return subtotal


    # Apply the first fee in the list to the current running total

    current_rate = fee_rates[0]

    new_amount = subtotal + (subtotal * current_rate)

    # Recursive case: apply the remaining fees to the new amount

    return calculate_fees_recursive(new_amount, fee_rates[1:])
6

def calculate_order_subtotal(order, movies_db, snack_menu):

    """

    Feature 5 Helper: Calculates subtotal using map() / reduce().

    - Sum of (ticket_quantity * ticket_price) + sum of snack items.



    Expected `order` shape:

        {

            "customer": str,

            "movie": str or None,

            "showtime_index": int or None,

            "ticket_quantity": int,

            "snacks": [{"name": str, "quantity": int}, ...]

        }

    """

    ticket_cost = 0.0

    movie_title = order.get("movie")

    showtime_index = order.get("showtime_index")



    if movie_title and showtime_index is not None:

        movie = movies_db.get(movie_title)

        if movie:

            showtimes = movie.get("showtimes", [])

            if 0 <= showtime_index < len(showtimes):

                showtime = showtimes[showtime_index]

                ticket_cost = showtime["price"] * order.get("ticket_quantity", 0)



    snacks = order.get("snacks", [])

    # map(): turn each snack line into its line-total cost

    snack_costs = list(

        map(lambda item: snack_menu.get(item["name"], 0) * item["quantity"], snacks)

    )

    # reduce(): sum all the snack line-totals into one number

    snack_total = reduce(lambda acc, cost: acc + cost, snack_costs, 0.0)

    return ticket_cost + snack_total


def print_receipt(customer_name, movie_info, tickets_info, snacks_list, subtotal, final_total):

    """

    Feature 5: Displays a neatly formatted, column-aligned itemized receipt.



    - movie_info: {"title": str, "time": str}

    - tickets_info: {"quantity": int, "price": float}

    - snacks_list: [{"name": str, "quantity": int, "line_total": float}, ...]

    """

    WIDTH = 30

    LABEL_WIDTH = 22



    print("=" * 10 + " RECEIPT " + "=" * 10)

    print(f"Customer: {customer_name}")



    if movie_info:

        print(f"Movie:    {movie_info['title']} ({movie_info['time']})")



    print("-" * WIDTH)



    if tickets_info and tickets_info.get("quantity", 0) > 0:

        qty = tickets_info["quantity"]

        price = tickets_info["price"]

        label = f"Tickets ({qty} x ${price:.2f})"

        amount = f"${qty * price:.2f}"

        print(f"{label:<{LABEL_WIDTH}}{amount:>8}")



    for snack in snacks_list:

        label = f"{snack['name']} x{snack['quantity']}"

        amount = f"${snack['line_total']:.2f}"

        print(f"{label:<{LABEL_WIDTH}}{amount:>8}")



    print("-" * WIDTH)

    print(f"{'Subtotal:':<{LABEL_WIDTH}}{'$' + format(subtotal, '.2f'):>8}")

    print(f"{'Total with fees:':<{LABEL_WIDTH}}{'$' + format(final_total, '.2f'):>8}")

    print("=" * WIDTH)



def checkout(order, movies_db, customers_db, snack_menu):

    """

    Feature 5: Completes order payment, prints receipt, updates seat count,

    updates total movie sales, and saves order to customer history.


    """

    customer_name = order.get("customer")

    movie_title = order.get("movie")

    showtime_index = order.get("showtime_index")

    # Guard: no movie selected yet

    if not movie_title or showtime_index is None:

        print("⚠️  Cannot check out: no movie/showtime has been selected for this order yet.")

        return None



    movie = movies_db.get(movie_title)

    if movie is None:

        print(f"⚠️  Cannot check out: movie '{movie_title}' was not found in the system.")

        return None



    showtimes = movie.get("showtimes", [])

    if not (0 <= showtime_index < len(showtimes)):

        print(f"⚠️  Cannot check out: showtime for '{movie_title}' is invalid.")

        return None



    showtime = showtimes[showtime_index]

    ticket_qty = order.get("ticket_quantity", 0)



    # Build the priced snack list for the receipt

    snacks_list = [

        {

            "name": item["name"],

            "quantity": item["quantity"],

            "line_total": snack_menu.get(item["name"], 0) * item["quantity"],

        }

        for item in order.get("snacks", [])

    ]



    subtotal = calculate_order_subtotal(order, movies_db, snack_menu)

    final_total = calculate_fees_recursive(subtotal)



    movie_info = {"title": movie_title, "time": showtime["time"]}

    tickets_info = {"quantity": ticket_qty, "price": showtime["price"]}



    print_receipt(customer_name, movie_info, tickets_info, snacks_list, subtotal, final_total)



    # Update seat count and popularity counter for this showing

    showtime["seats"] = max(0, showtime["seats"] - ticket_qty)

    showtime["sold"] = showtime.get("sold", 0) + ticket_qty



    # Record this order in the customer's history

    order_record = {

        "movie": movie_title,

        "time": showtime["time"],

        "ticket_quantity": ticket_qty,

        "snacks": snacks_list,

        "subtotal": subtotal,

        "total": final_total,

    }

    customers_db.setdefault(customer_name, []).append(order_record)



    return order_record


def get_customer_history(customers_db, customer_name):

    """

    Feature 6: Pulls up a customer's order history.

    - MUST NOT crash if the customer does not exist in the system.

    """

    history = customers_db.get(customer_name)



    if not history:

        print(f"No order history found for customer '{customer_name}'.")

        return []



    print(f"=== Order History for {customer_name} ===")

    for i, past_order in enumerate(history, start=1):

        print(

            f"{i}. {past_order['movie']} ({past_order['time']}) - "

            f"{past_order['ticket_quantity']} ticket(s) - "

            f"Total: ${past_order['total']:.2f}"

        )

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

    # Interactive menu loop goes here
    
    # add movie and showtime
    for i in range(3):
        new_showtime =add_showtime(
            input("Enter the start time: "),
            float(input("Enter the ticket price: ")),
            int(input("Enter the number of seats: ")))
        if new_showtime is not None:
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

    # ---------------------------------------------------

    # Features 3 & 4 (Dana): booking + snacks

    # ---------------------------------------------------
    
    customer_name = input("Enter the customer name for this order: ")

    active_order = create_active_order(customer_name)

    movie_title = input("Enter the movie title to book: ")

    showtime_index = int(input("Enter the showtime index (0, 1, 2...): "))

    quantity = int(input("Enter number of tickets: "))

    book_tickets(active_order, movie_title, showtime_index, quantity, MOVIES_DB)

    snack_name = input("Enter a snack name to add (leave blank to skip): ")

    if snack_name:

        snack_qty = int(input("Enter snack quantity: "))

        add_snack_to_order(active_order, SNACK_MENU, snack_name, snack_qty)


    # ---------------------------------------------------

    # Features 5, 6 & 7 (Waseem): checkout + reports

    # ---------------------------------------------------

    checkout(active_order, MOVIES_DB, CUSTOMERS_DB, SNACK_MENU)

    get_customer_history(CUSTOMERS_DB, customer_name)

    get_popularity_report(MOVIES_DB)


if __name__ == "__main__":
    main()

