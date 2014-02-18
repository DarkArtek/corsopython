# The HTTP Library

Implement client and server to:

- Store Book information (auth required)
- Search books by title and author (auth optional)
- Booking of books (auth required)
- Limit books creations to admin only


## Store book information

User can *create* a book by 'POST'ing to a http API using a CLI client:


      python libray_client.py store -- title "The songliness" --author "Chatwin" --user pippo --paswword pass

The client uses the standard output to inform the user about the operation completion and/or errors.

## Search book by title anmd author

User can *search* the online catalogue by 'GET'ing using an HTTP Api

      python library_client.py search --term "Montalbano"


## Booking

User can book an item using the CLI
 
     python library_client.py book --title "The songlines" --user pippo --password pass

The client warns the user if the book is not available or if it has already been booked by the calling user.

1) free -> book it
2) someone else has booked it
3) the calling user has already booked it
4) the book is not found
  