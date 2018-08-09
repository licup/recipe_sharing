import webapp2
import jinja2
import os
from models import Recipe

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
    
    
def run_query(first_line, second_line, third_line, pic_type):
    recipe = Recipe(line1=first_line, line2 = second_line, line3 = third_line, recipe_choice = pic_type)
    recipe_key = recipe.put()
    print("&&&&&&&&&&&&&&&&&&&&&&&&&")
    print recipe_key

def delete_all_recipes():
    all_recipes = Recipe.query().fetch()
    for recipe in all_recipes:
        print recipe.key.delete()
        
class DeleteRecipesHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        delete_all_recipes()
        self.response.write('query executed')
    
# def get_recipe_url(recipe_choice):
#     if recipe_choice == 'old-class':
#         url = 'https://upload.wikimedia.org/wikipedia/commons/4/47/StateLibQld_1_100348.jpg'
#     elif recipe_choice == 'college-grad':
#         url = 'https://upload.wikimedia.org/wikipedia/commons/c/ca/LinusPaulingGraduation1922.jpg'
#     elif recipe_choice == 'thinking-ape':
#         url = 'https://upload.wikimedia.org/wikipedia/commons/f/ff/Deep_in_thought.jpg'
#     elif recipe_choice == 'coding':
#         url = 'https://upload.wikimedia.org/wikipedia/commons/b/b9/Typing_computer_screen_reflection.jpg'
#     else:
#         url = False
#     return url


class EnterInfoHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        the_variable_dict = {
            "greeting": "Recipe Website", 
            "adjective": "delicious"
        }
        
        welcome_template = the_jinja_env.get_template('templates/home.html')
        self.response.write(welcome_template.render(the_variable_dict))

    def post(self):
        self.response.write("POST request was madfe to the EnterInfoHandler")

class ShowRecipeHandler(webapp2.RequestHandler):
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        recipe_first_line = self.request.get('user-first-ln')
        recipe_second_line = self.request.get('user-second-ln')
        recipe_third_line = self.request.get('user-third-ln')

        recipe_choice = self.request.get('recipe-type')
        run_query(recipe_first_line, recipe_second_line, recipe_third_line, recipe_choice)
        
        # pic_url = get_recipe_url(recipe_choice)
    
        the_variable_dict = {"line1": recipe_first_line,
                             "line2": recipe_second_line, 
                             "line3": recipe_third_line,
                             "img_url" : recipe_choice
        }
        self.response.write(results_template.render(the_variable_dict))      

class AllRecipesHandler(webapp2.RequestHandler):
    def get(self):  # for a get request
        allrecipes = Recipe.query().fetch()
        
       
        the_variable_dict = {
            "allrecipes": allrecipes,
           
        }
        
        allrecipes_template = the_jinja_env.get_template('templates/allrecipes.html')
        self.response.write(allrecipes_template.render(the_variable_dict))


app = webapp2.WSGIApplication([
    ('/', EnterInfoHandler),
    ('/showrecipe', ShowRecipeHandler),
    ('/allrecipes', AllRecipesHandler),
    ('/deleterecipes', DeleteRecipesHandler),
], debug=True)
