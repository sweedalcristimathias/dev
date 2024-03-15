Prerequisites

    Before running this application, ensure you have the following installed:

    1.Python 3.x
    2.Flask (install using pip install flask)

Install dependencies 

    pip install -r requirements.txt


Steps to setup the project
    
    Create a folder and navigate to the project folder

    Setup the API endpoints:

    (i)For getting all users: GET '/user'
    (ii)For getting user by id:GET '/user/<int:user_id>'
    (iii)Creating a user:POST '/user'
    (iv)Updating a user:PUT '/user/<int:user_id>'
    (v)Deleting a user:DELETE '/user/<int:user_id>'

Run and test the project 

    Start API server:python main.py

    Verify if Api is running:open web browser and navigate to http://127.0.0.1:5000/

    Test the endpoints using postman by sending various requests like GET,POST,PUT,DELETE.

Examples for each with request and response format 

    (i)get users: http://127.0.0.1:5000/user ,Method:GET
    RESPONSE FORMAT:
    {
    "age": 'age of the user',
    "email": "email of user",
     "id": 'id of user,
    "name": "name of user"
    }



    EXAMPLE :
    {
        "age": 28,
        "email": "john@gmail.com",
        "id": 1,
        "name": "john"
    },
    {
        "age": 28,
        "email": "max@gmail.com",
        "id": 2,
        "name": "max"
    },
    {
        "age": 22,
        "email": "jyothsna@gmail.com",
        "id": 3,
        "name": "jyothsna"
    }

    (ii)get user by id:http://127.0.0.1:5000/user/1 ,Method:GET,
    RESPONSE FORMAT:
    {
        "age": 'age of the user with id 1',
        "email": "email of user with id 1",
        "id": 'id of user',
        "name": "name of user with id 1"
    }

    EXAMPLE:
    {
    "age": 28,
    "email": "john@gmail.com",
    "id": 1,
    "name": "john"
    }

    (iii)create user:http://127.0.0.1:5000/user ,Method:POST
    REQUEST FORMAT:
    {
        "age": 'age of the user',
        "email": "email of user",
        "name": "name of user"
    }
    RESPONSE FORMAT:
    {
        "age": 'age of the user',
        "email": "email of user",
        "id": 'id of user,
        "name": "name of user"
    }
    EXAMPLE OF REQUEST FORMAT:
    {
            "age": 27,
            "email": "jake@gmail.com",
            "name": "jake"
        }
    EXAMPLE OF RESPONSE FORMAT:
    {
        "age": 27,
        "email": "jake@gmail.com",
        "id": 5,
        "name": "jake"
    }

    (iv)update user:http://127.0.0.1:5000/user/1 ,Method:PUT
    REQUEST FORMAT:
    {
        "age": 'age of the user',
        "email": "email of user",
        "name": "name of user"
    }
    RESPONSE FORMAT:
    {
        "age": 'age of the user',
        "email": "email of user",
        "id": 'id of user,
        "name": "name of user"
    }
    EXAMPLE OF REQUEST FORMAT:
     {
            "age": 32,
            "email": "john@gmail.com",
            "name": "john"
        }
    EXAMPLE OF RESPONSE FORMAT:
    {
        "age": 32,
        "email": "john@gmail.com",
        "id": 1,
        "name": "john"
    }

    (v)delete user:http://127.0.0.1:5000/user/1 ,Method:DELETE
    RESPONSE FORMAT:
    {
        "data": "Some message which says the user is deleted successfully"
    }
    EXAMPLE OF RESPONSE FORMAT
    {
        "data": "User deleted successfully"
    }

Features:

    Create, Read, Update, and Delete operations on a user database.
    RESTful API endpoints for interacting with user data.



