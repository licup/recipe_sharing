import webapp2
import jinja2
import os
from models import Recipe

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
def run_query(first_line, second_line, pic_type):
    recipe = Recipe(line1=first_line, line2 = second_line, img_choice = pic_type)
    recipe_key = recipe.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print recipe_key

    
    
def get_recipe_url(recipe_choice):
    if recipe_choice == 'old-class':
        url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
    elif recipe_choice == 'college-grad':
        url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
    elif recipe_choice == 'thinking-ape':
        url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
    elif recipe_choice == 'coding':
        url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
    return url


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        the_variable_dict = {
            "greeting": "Hello", 
            "adjective": "delicious"
        }
        
        welcome_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(welcome_template.render(the_variable_dict))

    def post(self):
        self.response.write("POST request was madfe to the EnterInfoHandler")

class AllRecipesHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        all_recipes = Recipe.query().fetch()
        
        the_variable_dict = {
            "all_recipes": all_recipes
        }
        
        all_recipes_template = the_jinja_env.get_template('templates/all_recipes.html')
        self.response.write(all_recipes_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/allrecipes', AllRecipesHandler),
], debug=True)

