import requests
import turtle
import time

__author__ = 'Tyler Ward'


def astronaut_info():
    """
        fetches a list of astronauts in space,
        and the craft they are on.  Prints their
        name, craft and total # of astronauts
    """
    r = requests.get('http://api.open-notify.org/astros.json')
    r_json = r.json()
    astronauts = [astro for astro in r_json['people']]
    total_num_astros = r_json['number']

    print(f'\nTotal astronauts in space: {total_num_astros}\n')

    for astro in astronauts:
        name = astro['name']
        craft = astro['craft']
        print(f'name: {name}\t\t spacecraft: {craft}')


def geo_cord_iss():
    r = requests.get('http://api.open-notify.org/iss-now.json')
    r_json = r.json()

    pos = r_json['iss_position']
    timestamp = r_json['timestamp']
    lat = pos['latitude']
    long = pos['longitude']

    print('\nSpace Station Current Position:\n')
    print(f'Latitude: {lat}, Longitude: {long}, Timestamp: {timestamp}')
    return {'latitude': lat, 'longitude': long, 'time': timestamp}


def turtle_screen_setup():
    """
    sets up the turtle screen for the ISS locator
    """
    screen = turtle.Screen()
    screen.bgpic('map.gif')
    screen.reset()
    screen.setup (720, 360)
    screen.setworldcoordinates(-180, -90, 180, 90)
    screen.register_shape('iss.gif')
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.setheading(90)
    iss.penup()

    pos = geo_cord_iss()
    iss.goto(-86.1581, 39.7684)
    iss.pendown()
    iss.dot(10, 'red')
    iss.write(f'\nThe next time the ISS will be in Inday: {time.ctime(next_indy_pass())}')
    iss.goto(float(pos['longitude']), float(pos['latitude']))

    print(f'\nThe next time the ISS will be in Inday: {time.ctime(next_indy_pass())}')

    turtle.mainloop()


def next_indy_pass():
    indy = requests.get('http://api.open-notify.org/iss-pass.json', params={'lat': 39.7684, 'lon': 86.1581})
    indy = indy.json()
    return indy['response'][0]['risetime']



def main():
    """Calls functions that fetch from APIs"""
    # astronaut_info()
    # geo_cord_iss()
    turtle_screen_setup()

if __name__ == '__main__':
    main()
