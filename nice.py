from random import choice

from flask import Flask, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      Hi! This is the home page.<br>
      <a href="/hello">Click here</a> to see Hello.
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          <label>First name: <input type="text" name="first_name"></label>
          <label>Last name: <input type="text" name="last_name"></label> 
          <div>Please select a compliment below:<select name="compliment">
              <option value="awesome">Awesome</option>
              <option value="terrific">Terrific</option>
              <option value="fantastic">Fantastic</option>
          </select></div>
          <input type="submit">
        </form>
      </body>
    </html>
    """

@app.route('/diss')
def diss():
    """Insulting the user."""

    player = request.args.get('person')

    insult = choice(['annoying', 'not good', 'a terrible cook'])

    player_choice = request.args.get('compliment')

    return """
    <!doctype html>
    <html>
      <head>
        <title>An insult</title>
      </head>
      <body>
        Hi, {}! You might think that you're {}, but you're actually {}.
      </body>
    </html>
    """.format(player, player_choice, insult)

@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    player_choice = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi %s I think you're %s!
        You think you're %s.
      </body>
    </html>
    """ % (player, compliment, player_choice)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True)
