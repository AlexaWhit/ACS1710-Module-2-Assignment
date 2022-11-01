from flask import Flask, request, render_template
import random
from random import randint

app = Flask(__name__)

def sort_letters(message):
    """A helper method to sort the characters of a string in alphabetical order
    and return the new string."""
    return ''.join(sorted(list(message)))


@app.route('/')
def homepage():
    """A homepage with handy links for your convenience."""
    return render_template('home.html')

## FROYO ##
@app.route('/froyo')
def choose_froyo():
    """Shows a form to collect the user's Fro-Yo order."""
    return render_template('froyo_form.html')

@app.route('/froyo_results')
def show_froyo_results():
    """Shows the user what they ordered from the previous page."""
    context = {
        'froyo_flavor': request.args.get('flavor'),
        'froyo_toppings': request.args.get('toppings')
    }
    return render_template('froyo_results.html', **context)

## FAVORITE THINGS ##
@app.route('/favorites')
def favorites():
    """Shows the user a form to choose their favorite color, animal, and city."""
    return """
    <form action="/favorites_results" method="GET">
        What is your favorite color? <br/>
        <input type="text" name="color"><br/>
        What is your favorite animal? <br/>
        <input type="text" name="animal"><br/>
        What is your favorite city? <br/>
        <input type="text" name="city"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/favorites_results')
def favorites_results():
    """Shows the user a nice message using their form results."""
    users_fav_color = request.args.get('color')
    users_fav_animal = request.args.get('animal')
    users_fav_city = request.args.get('city')
    return f'Wow, I did not know {users_fav_color} {users_fav_animal} lived in {users_fav_city}!'

## SECRET MESSAGE ##
@app.route('/secret_message')
def secret_message():
    """Shows the user a form to collect a secret message. Sends the result via
    the POST method to keep it a secret!"""
    return """
    <form action="/message_results" method="POST">
        Enter a secret message: <br/>
        <input type="text" name="message"><br/>
        <input type="submit" value="Submit!">
    </form>
    """

@app.route('/message_results', methods=['POST'])
def message_results():
    """Shows the user their message, with the letters in sorted order."""
    users_message = request.form.get('message')
    secret = sort_letters(users_message)
    return f'Here is your secret message! <br/> {secret}'

## CALCULATOR ##
@app.route('/calculator')
def calculator():
    """Shows the user a form to enter 2 numbers and an operation."""
    return render_template('calculator_form.html')

@app.route('/calculator_results')
def calculator_results():
    """Shows the user the result of their calculation."""
    number1 = int(request.args.get('operand1'))
    number2= int(request.args.get('operand2'))
    operator = request.args.get('operation')

    if operator == "add":
        result = int(number1 + number2)
        return f'You chose to {operator} {number1} and {number2}. Your result is: {result}'
    elif operator == "subtract":
        result = int(number1 - number2)
        return f'You chose to {operator} {number1} and {number2}. Your result is: {result}'
    elif operator == "multiply":
        result = int(number1 * number2)
        return f'You chose to {operator} {number1} and {number2}. Your result is: {result}'
    elif operator == "divide":
        result = int(number1 / number2)
        return f'You chose to {operator} {number1} and {number2}. Your result is: {result}'

    # --- I HAVE NO IDEA HOW TO DO THE CONTEXT DICTIONARY WITH ALSO NEEDING THE VARIABLES ABOVE TO DO THE MATH 
    # -- WHERE DO I PUT THE LOGIC?? ##
    context = {
        'number1': number1,
        'number2': number2,
        'operator': operator,
        'result': result,
    }
    return render_template('calculator_results.html', **context)
  

## HOROSCOPE ##

HOROSCOPE_PERSONALITIES = {
    'aries': 'Adventurous and energetic',
    'taurus': 'Patient and reliable',
    'gemini': 'Adaptable and versatile',
    'cancer': 'Emotional and loving',
    'leo': 'Generous and warmhearted',
    'virgo': 'Modest and shy',
    'libra': 'Easygoing and sociable',
    'scorpio': 'Determined and forceful',
    'sagittarius': 'Intellectual and philosophical',
    'capricorn': 'Practical and prudent',
    'aquarius': 'Friendly and humanitarian',
    'pisces': 'Imaginative and sensitive'
}

@app.route('/horoscope')
def horoscope_form():
    """Shows the user a form to fill out to select their horoscope."""
    return render_template('horoscope_form.html')

@app.route('/horoscope_results')
def horoscope_results():
    """Shows the user the result for their chosen horoscope."""
    users_name = request.args.get('users_name')

    # TODO: Get the sign the user entered in the form, based on their birthday
    horoscope_sign = request.args.get('horoscope_sign')

    # TODO: Look up the user's personality in the HOROSCOPE_PERSONALITIES
    # dictionary based on what the user entered
    # users_personality = request.args.get('users_personality')
    if horoscope_sign == 'aries':
        users_personality = 'Adventurous and energetic'
    elif horoscope_sign == 'taurus':
        users_personality = 'Patient and reliable'
    elif horoscope_sign == 'gemini':
        users_personality = 'Adaptable and versatile'
    elif horoscope_sign == 'cancer':
        users_personality = 'Emotional and loving'
    elif horoscope_sign == 'leo':
        users_personality = 'Generous and warmhearted'
    elif horoscope_sign == 'virgo':
        users_personality = 'Modest and shy'
    elif horoscope_sign == 'libra':
        users_personality = 'Easygoing and sociable'
    elif horoscope_sign == 'scorpio':
        users_personality = 'Determined and forceful'
    elif horoscope_sign == 'sagittarius':
        users_personality = 'Intellectual and philosophical'
    elif horoscope_sign == 'capricorn':
        users_personality = 'Practical and prudent'
    elif horoscope_sign == 'aquarius':
        users_personality = 'Friendly and humanitarian'
    elif horoscope_sign == 'pisces':
        users_personality = 'Imaginative and sensitive'

    # TODO: Generate a random number from 1 to 99
    lucky_number = randint(1,99)

    context = {
        'horoscope_sign': horoscope_sign,
        'users_personality': users_personality, 
        'users_name': users_name,
        'lucky_number': lucky_number
    }

    return render_template('horoscope_results.html', **context)

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
