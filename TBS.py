import json
import random
from pprint import pprint as pp

#You should implement a tickets booking system for cinemas.

#There should be:
#A list of the movies
movies = ('Billy Elliot', 'Kung Fu Panda', 'Oldboy', 'Hot Fuzz',
          'Менің атым Қожа', 'Whiplash', 'Pineapple Express',
          'Memories of Murder', 'Joint Security Area', 'Boy')

time = ['10:10', '10:20', '11:00', '11:10', '12:00', '12:20',
        '12:40', '12:55', '13:05', '13:55', '14:05', '14:10',
        '14:30', '15:00', '15:05', '16:05', '16:10', '16:35',
        '17:05', '17:30', '17:55', '19:00', '19:15', '19:25',
        '19:40', '19:55', '20:05', '20:10', '20:20', '20:55',
        '23:10', '23:25', '23:30', '23:45', '23:50']

#Each cinema should have more than one hall (кинозал).
halls = ['green', 'blue', 'red', 'orange']

#Each cinema should have a schedule (you should make different schedules for different cinemas)

def show_schedule():
    for y in movies[: : random.randint(1, 3)]:
        print('\t ' + y + ':')
        random.shuffle(halls)
        for z in halls[: : random.randint(1, 4)]:
            print('\t\t\t' + z)
            random.shuffle(time)
            for i in  sorted(time[0 : : random.randint(9, 12)]):
                print('\t\t\t\t' + i)
                
#A list of the cinemas

def show_list_of_cinemas():
    cinemas = ('Chaplin', 'Cinemax', 'Kinopark', 'Lumiera', 'Arman 3D')
    for x in cinemas:
        print(x)
    des = input('\nChoose a cinema from the list above: ')
    for x in cinemas:
        if (x == des):
            show_schedule()
        else:
            show_list_of_cinemas()

#Each hall should have seats number (make this number small 3-5, for the simplicity)



#When you run the program, the random number of seats should be sold (occupied) right from the beginning.
def seats_avaliable():
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

    seats_remaining = sum(sum(1 for z in y.values() if z is '______')for y in x)
    print('%s seats are still avaliable' % seats_remaining)

    pp(x)

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
            print("We'll remember you when you come back, " + username + "!") 
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")        

#greet_user()
show_list_of_cinemas()
seats_avaliable()
#You should be able to:

#log in and out as a user
#Get the list of cinemas showing a particular movie
#Get the schedule of a particular cinema
#See a number of available seats
#Book the ticket(s) on a movie
 

#Once the ticket is booked, the information about the available seats should be updated.'''
