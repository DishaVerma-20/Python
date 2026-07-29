"""
Create a class Movie with the following:

Attributes:
movie_name —> name of the movie
total_seats —> total seats available in the theatre
ticket_price —> price per ticket
booked_seats —> starts at 0

Methods:
book_ticket(num_tickets) — books the given number of tickets. If enough seats are available,
confirm the booking and show the total amount to pay. If not,
show "Sorry, not enough seats available"

show_status() — displays movie name, seats available, and seats booked so far
"""

class Movie:

    def __init__(self, movie_name:str, total_seats:int, ticket_price:int) -> None:
        self.movie_name = movie_name
        self.total_seats = total_seats
        self.ticket_price = ticket_price
        self.booked_seats = 0

    def book_ticket(self, num_tickets) -> None:
        seat_available = self.total_seats - self.booked_seats
        if num_tickets>seat_available:
            print("Sorry, not enough seats available")
        else:
            self.booked_seats += num_tickets
            print("Booking is confirmed!")
            print(num_tickets*self.ticket_price)

    def show_status(self) -> None:
        print("Movie Name: ", self.movie_name)
        print("Seats available: ", self.total_seats - self.booked_seats)
        print("Booked seats: ", self.booked_seats)

m1 = Movie("Chand Mera Dil", 50, 250)
m1.book_ticket(21)
m1.show_status()
m1.book_ticket(30) # not enough seats available
m1.show_status()