## HW 1
## SI 364 W18
## 1000 points

#################################

## List below here, in a comment/comments,
 ##the people you worked with on this assignment AND
 ##any resources you used to find code (50 point deduction
 ##for not doing so). If none, write "None".
 ##resources= https://prettyprinted.com/blog/1128685/creatign-todo-list-app-with-flask, http://werkzeug.pocoo.org/docs/0.14/tutorial/
 ##worked with: none
## [PROBLEM 1] - 150 points
## Below is code for one of the simplest
# possible Flask applications. Edit the
 #code so that once you run this application
 #locally and go to the URL 'http://localhost:5000/class',
  #you see a page that says "Welcome to SI 364!"

from flask import Flask, request
import requests
from werkzeug.wrappers import Request, Response ##Fixes google chrome 404 redirecting error with each route by adding favicon to the route because chrome calls it after the first request. I wasted many hours finding this :( source:https://github.com/pallets/flask/issues/405 and http://werkzeug.pocoo.org/docs/0.14/tutorial/

app = Flask(__name__)
app.debug = True

@app.route('/')
def hello_to_you():
    return 'Hello!'
@app.route('/class')
def greeting_class():
    return "<h1>Welcome to SI 364!</h1>"

import json
## [PROBLEM 2] - 250 points
## Edit the code chunk above again so that if you go to the URL 'http://localhost:5000/movie/<name-of-movie-here-one-word>' you see a big dictionary of data on the page. For example, if you go to the URL 'http://localhost:5000/movie/ratatouille', you should see something like the data shown in the included file sample_ratatouille_data.txt, which contains data about the animated movie Ratatouille. However, if you go to the url http://localhost:5000/movie/titanic, you should get different data, and if you go to the url 'http://localhost:5000/movie/dsagdsgskfsl' for example, you should see data on the page that looks like this:
@app.route('/movie/<nameofmovieoneword>')
def movie_form(nameofmovieoneword):
    url = "https://itunes.apple.com/search"
    par_dict={}
    par_dict['term']=nameofmovieoneword
    return requests.get(url, params= par_dict).text
# {
#  "resultCount":0,
#  "results": []
# }
## You should use the iTunes Search API to get that data.
## Docs for that API are here: https://affiliate.itunes.apple.com/resources/documentation/itunes-store-web-service-search-api/
## Of course, you'll also need the requests library and knowledge of how to make a request to a REST API for data.

## Run the app locally (repeatedly) and try these URLs out!

## [PROBLEM 3] - 250 points

## Edit the above Flask application code so that if you run the application locally and got to the URL http://localhost:5000/question, you see a form that asks you to enter your favorite number.
## Once you enter a number and submit it to the form, you should then see a web page that says "Double your favorite number is <number>". For example, if you enter 2 into the form, you should then see a page that says "Double your favorite number is 4". Careful about types in your Python code!
## You can assume a user will always enter a number only.
@app.route('/question',methods=['POST', 'GET'])
def times_two():
    s='''
    <html>
    <body>
    <form method = 'POST'>
    <form>
        Please enter your favorite number:<br>
        <input type='text' name='number'>
        <br>
        <input type='submit' value='Submit'>
    </form>
    </body>
    </html>'''
    if request.method == 'POST':
        choice=int(request.form['number'])
        timestwo=choice*2
        return 'Double your favorite number is ' +str(timestwo)
    else:
        return s


## [PROBLEM 4] - 350 points

## Come up with your own interactive data exchange that you want to see happen dynamically in the Flask application, and build it into the above code for a Flask application, following a few requirements.

## You should create a form that appears at the route: http://localhost:5000/problem4form

## Submitting the form should result in your seeing the results of the form on the same page.

## What you do for this problem should:
# - not be an exact repeat of something you did in class
# - must include an HTML form with checkboxes and text entry
# - should, on submission of data to the HTML form, show new data that depends upon the data entered into the submission form and is readable by humans (more readable than e.g. the data you got in Problem 2 of this HW). The new data should be gathered via API request or BeautifulSoup.

# You should feel free to be creative and do something fun for you --
# And use this opportunity to make sure you understand these steps: if you think going slowly and carefully writing out steps for a simpler data transaction, like Problem 1, will help build your understanding, you should definitely try that!

# You can assume that a user will give you the type of input/response you expect in your form; you do not need to handle errors or user confusion. (e.g. if your form asks for a name, you can assume a user will type a reasonable name; if your form asks for a number, you can assume a user will type a reasonable number; if your form asks the user to select a checkbox, you can assume they will do that.)

# Points will be assigned for each specification in the problem.
@app.route('/problem4form', methods=['POST','GET'])
def enterData():
    s = """<!DOCTYPE html>
<html>
<body>
<method = 'POST'>
<form>
  INGREDIENT:<br>
  <input type="checkbox" name="Ingredient" value="Peanut Butter"> Do you like Peanut Butter? <br>
  <input type="checkbox" name="Ingredient" value="Jelly"> Do you like jelly? <br>
  <input type="checkbox" name="Ingredient" value="Nutella"> Do you like Nutella? <br>
  <input type="checkbox" name="Ingredient" value="Banannas"> Do you like Banannas? <br>
  <input type='text' name='Ingredient' value='enter here'> What do you like? <br>
  <br>
  <input type="submit" value="Submit">
</form>
</body>
</html>"""
    if request.method == 'POST':
        data =request.values.get('Ingredient') # Your form's
        # data=request.form['Ingredient']
        url="https://api.edamam.com/search?q=PeanutButter&app_id=${ac89334e}&app_key=${6e18d70b624fa73e890d0be694e0acef}"
        json=requests.get(url +data)
        return 'you should try:' +json
    return 'you have no taste' 



if __name__ == '__main__':
    app.run()

##https://www.google.com/search?rlz=1C1CHBF_enUS763US763&ei=l3RdWp_EDOusjwTAxoQo&q=new+ranging+botas&oq=new+ranging+botas&gs_l=psy-ab.3...20798.25764.0.26689.6.6.0.0.0.0.339.1214.0j2j1j2.5.0....0...1c.1.64.psy-ab..1.3.755...0i22i10i30k1j0i22i30k1j33i21k1j33i160k1.0.FRyLKY_h9Z8
    # else:
    #     return 'tryagain'
