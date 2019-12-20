# TSHIRT STORE

### Introduction
---
TSHIRT STORE is an online ecommerce website, where user can browse and purchase tshirts where they find fit. It is equipped with login functionality and payment capabilities.

### Demo
---
The live demonstration of the app can be accessed in the following link : [https://tshirt-project4.herokuapp.com/](https://tshirt-project4.herokuapp.com/)
### User Interface
---
The website aims to be minimalist as not to distract users with functionalities that might deter and make users not want to stay on the site.

### User Stories

As a user, I want to be able to:
- Access the website on any devices (computer,tablets,phones)
- View all products available in the store
- Register and Log in to the website
- Make purchase of the items in the store
- Remove any items that I might change my mind

As a superuser, I want to be able to:
- View all available users
- Perform CRUD capabilities of the products in the website
- Update/upload images for the product item in the website
---
### Features
Certain features have been integrated which enables users to:
 - Register and login to the site
 - Browse to available collection of shirt
 - Add products to cart
 - Remove item from cart
 - Make payments of selected item using STRIPE API
 
Additionally, the superuser is able to:
 - Make CRUD (Create,Read,Upate,Delete) for the Items in the store
 - Track and view all users registered in the site
 
Features to be implemented in future:
- Password reset functionality
- Filtering of products(once more products has been added)
- User Profile (to track history of purchase from users)
- Product Reviews
---
## Technology 
HTML
CSS
JAVASCRIPT
PYTHON
DJANGO
JINJA2
BOOTSTRAP
DJANGO-CRISPYFORMS
DJANGO-ALLAUTH
HEROKU
HEROKU POSGRES
GUNICORN
AWS C9
AWS S3 STORAGE
STRIPE API
---
## TESTING

The website has been tested by the following browser:
- Google Chrome
- Firefox

CRUD Testing was done manually using the /admin site.

#### User Authentication testing
| Test Case (Login)       | Expected Results           | Status |
| ------------- |:-------------:| -----:|
| Key in unregistered username      | Unable to login | Pass |
| Key in unregistered password     | Unable to login    |   Pass |
| Never key in anything | Unable to login     |   Pass |

| Test Case (Registration)       | Expected Results           | Status |
| ------------- |:-------------:| -----:|
| Missing Parameters in any field     | Unable to register | Pass |
| Using a registered email    | Error Message    |   Pass |
| Password not up to standard  | Error Message     |   Pass |
| Password retype not the same  | Error Message     |   Pass |

| Test Case (Payments)       | Expected Results           | Status |
| ------------- |:-------------:| -----:|
| Using valid card number(4242... )    | Payments success | Pass |
| Using invalid card number    | Payment error    |   Pass |
| Using expired card  |  Payment error     |   Pass |
---
## Deployment
The site is being deploy and hosting in Heroku, using Heroku Postgres as the backend database.
To deploy, the following steps is required:
1. Install dependancies and folders.
     - pip install (gunicorn, heroku , psycopg2 , Pillow)
     - setup cloud storage i.e( AWS S3) , with settings.py update for static folder root and directories
     
2. pip3 freeze --local > requirements.txt 
     - create a requirements.txt file so heroku will know it is a python application with the necessary dependancies
     
3. Create a Procfile with web: gunicorn <PROJECT_FOLDER>.wsgi:application
    - has to be in the same directory as manage.py
4. Create a git repository add, commit and push changes inside terminal
    - git add. , git commit -m , git push origin master
5. Go to heroku website and create a new app and setup postgres
6. Setup config vars for environ variables inside your project
   - add a .git ignore file to hide sensitive info in your project [https://github.com/jpadilla/django-project-template/blob/master/.gitignore""]
7. push your github to your heroku master and create a superuser
   - Superuser required since we are now using the heroku database
8. Site should be deployed if steps are followed correctly.
---
## Credits
Pictures was taken from Pexels and GoogleImages
Tutorials are derived from CodeInstitute website and Youtube resources.