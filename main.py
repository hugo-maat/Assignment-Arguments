# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

"""
Assignment: Arguments, for Winc Academy course 
'Data Analytics with Python'; 
Hugo Maat, 21-1-2022
Version 1.0
"""

# Part 1

def greet(name, greet_template='Hello, <name>!'):
    if greet_template == 'Hello, <name>!':
        return f'Hello, {name}!'
    else:
        return greet_template.replace('<name>', name)

# Part 2

surface_gravity = {'sun': 274, 'jupiter': 24.92, 'neptune': 11.15,
        'saturn': 10.44, 'earth': 9.798, 'uranus': 8.87, 'venus': 8.87,
        'mars': 3.71, 'mercury': 3.7, 'moon': 1.62, 'pluto': 0.58
        }

def force(mass, body='earth'):
    force = mass * round(surface_gravity[body.lower()],1)
    return force

# Part 3

G = 6.674 * 10 ** -11 # Hardcoded the gravitational constant

def pull(m1, m2, d):
    force = G * ((m1 * m2) / (d * d))
    return force