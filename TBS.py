import json
import random

#You should implement a tickets booking system for cinemas.

#You should be able to:

#log in and out as a user
#Get the list of cinemas showing a particular movie
#Get the schedule of a particular cinema
#See a number of available seats
#Book the ticket(s) on a movie

#There should be:

#A list of the movies
movies = ['Billy Elliot', 'Kung Fu Panda', 'Oldboy', 'Hot Fuzz',
          'Менің атым Қожа', 'Whiplash', 'Pineapple Express',
          'Memories of Murder', 'Joint Security Area', 'Boy']

time = ['10:10', '10:20', '11:00', '11:10', '12:00', '12:20',
        '12:40', '12:55', '13:05', '13:55', '14:05', '14:10',
        '14:30', '15:00', '15:05', '16:05', '16:10', '16:35',
        '17:05', '17:30', '17:55', '19:00', '19:15', '19:25',
        '19:40', '19:55', '20:05', '20:10', '20:20', '20:55',
        '23:10', '23:25', '23:30', '23:45', '23:50']

#Each cinema should have more than one hall (кинозал).
halls = ['green', 'blue', 'red', 'orange']


#Each hall should have seats number (make this number small 3-5, for the simplicity)
#Once the ticket is booked, the information about the available seats should be updated.
#When you run the program, the random number of seats should be sold (occupied) right from the beginning.

def book_seat():
    seat = input("\nPlease, %s, choose your seat's row and letter: " % get_stored_username())
    if not bool(seat.rstrip()):
        seat = input("\nPlease, %s, choose your seat's row and letter: " % get_stored_username())
    return seat

def seats_avaliable():
    arr = []
    for x in book_seat():
        arr.append(x)

    c = 'ABCDE'
    r = range(0, 3)

    from pprint import pprint as pp
    x = [{ltr:'______' for ltr in c} for y in r]

    x[0]['A'] = 'booked'
    x[0]['D'] = 'booked'
    x[0]['C'] = 'booked'
    x[1]['E'] = 'booked'
    x[1]['B'] = 'booked'
    x[2]['D'] = 'booked'

    print('\n')
    pp(x)
    
    seats_remaining = sum(sum(1 for z in y.values() if z is '______')for y in x)
    print('\n%s seats are still avaliable' % seats_remaining)
    
    x[int(arr[0])][arr[1]] = 'booked'
    print('\n')
    pp(x)

    seats_remaining = sum(sum(1 for z in y.values() if z is '______')for y in x)
    print('\n%s seats are still avaliable' % seats_remaining)

#Each cinema should have a schedule (you should make different schedules for different cinemas)
def show_movies_list():
    arr = []
    print()
    random.shuffle(movies)
    for y in movies[: : random.randint(1, 3)]:
        print('\t ' + y)
        movie_list = arr.append(y)
    return movie_list

def hall_gen():
    harr = []
    random.shuffle(halls)
    for z in halls[: : random.randint(1, 3)]:
        harr.append(z)
    return harr

def time_gen():
    tarr = []
    random.shuffle(time)
    for i in  sorted(time[0 : : random.randint(9, 12)]):
        tarr.append(i)
    return tarr

def show_halls_and_time_list():
    tarr = []
    print()
    for z in hall_gen():
        print('\t\t\t' + z)
        for i in  time_gen():
            print('\t\t\t\t' + i)
        
def choose_moovie():
    movie = input("\nPlease, choose moovie: ")
    for x in movies:
        if (x == movie):
            print("\n%s is shown in the following hall(s): " % movie)
            show_halls_and_time_list()

def choose_hall_and_time():
    ht = []
    arr = []
    choose_hall = input('\nNow, please choose hall: ')
    ht.append(choose_hall)
    choose_time = input('and time: ')
    ht.append(choose_time)
    
    for x in hall_gen():
        arr.append(x)
    for x in halls:
        for y in time:
            if (ht[0] == x and ht[1] == y):
                seats_avaliable()
                
#A list of the cinemas
def show_list_of_cinemas():
    cinemas = ('Chaplin', 'Cinemax', 'Kinopark', 'Lumiera', 'Arman 3D')
    for x in cinemas:
        print(x)
    des = input('\n%s, choose a cinema from the list above: ' % get_stored_username())
    for x in cinemas:
        if (x == des):
            print("\n%s has a following schedule today: " % x)
            show_movies_list()
            break
        
#During the execution of the program, there should be a possibility to create customers (users).
def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    print('Your name is not in our list. ')
    username = input('Please, type it again, so we will add it: ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        return username
    
def greet_user():
    username = get_stored_username()
    if username:
        correct = input("Please, enter your name: ")
        if correct == str(username):
            print("Welcome, " + username + "!")
        else:
            username = get_new_username()
            print("\nWe'll remember you when you come back, " + username + "!") 
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")        

greet_user()
show_list_of_cinemas()
choose_moovie()
choose_hall_and_time()
