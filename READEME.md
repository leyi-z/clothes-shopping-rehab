## API Reference



### About This API

I have A LOT of clothes, but it all gets forgotten whenever I see a nice new dress. My (hypothetical) psychiatrist suggests that I make a list of all the clothes I own, along with the places they are stored at. The lists helped me realize what I already I have and what I actually need. Now I'm buying much less clothes and saving an extra $200 every month! This web app is created so it's easier for me to create the lists and update them. My (hypothetical) psychiatrist will have some access to the lists so we can both keep track on my progress.



### To Get Started

#### Heroku

~~The api is deployed using Heroku. The host url is `csrp-deploy.herokuapp.com`. You can access the homepage with the url `https://csrp-deploy.herokuapp.com/`~~ The public host is no longer running. It can only be accessed locally.

#### Tests

I created some tests for the api using both Postman and Unittest:
- To use the postman tests, simply import the file `csrp-tests.postman_collection.json` into postman
- Unittest can be found in `test_app.py`. You can run it using `python test_app.py`

#### Dependency

In case you want to run the app locally, all required packages are specified in the file `requirements.txt`. You can use the command `pip install -r requirements.txt` to install all of them at once.

#### Environment Variables

Before running the backend locally, run command `source setup.sh` in the project directory to set up environment variables. It includes the database url, some authentication info, and some recently generated jwt codes. You will probably have to change the database url to fit your environment.

#### Frontend

This web app doesn't have a frontend yet but hopefully it will soon!

#### Run Locally

After installing all the dependencies and setting up the environment variables, run the following command in the project directory:
```
$ export FLASK_APP=app.py
$ flask run
```



### Data Structure

The database contains two tables: `Locations` and `Clothes`. `Locations` contains a list of locations that the recorder uses to store their clothes; `Clothes` contains a list of clothes that the recorder own, including their categories, descriptions, and the locations where they are stored at.



### Authentication

The authentication process is carried out through Auth0. 

#### Roles

This api uses role-based access control (RBAC) provided by Auth0. So far it has two roles that can be assigned to each user.

##### Recorder 

A recorder has full access to the api, i.e. they are allowed to view, add, update and delete data. The recorder has the following permissions:
	- `get:inventory`
	- `add:inventory` 
	- `edit:inventory`
	- `delete:inventory`

##### Psychiatrist

The psychiatrist (psych) can only see what's in the database but has no permission to make changes. They have the following permission:
	- `get:inventory`

#### Test Users

I created two users for testing purpose, each with one of the two roles. You can use the following login info to login as each user and test the endpoints. I also included JWT for each user that I recently generated (on 03/22). 

##### Test User: Recorder
- username: `recorder@gmail.com`
- password: `Recorder123!`

##### Test User: Psych
- username: `psych@gmail.com`
- password: `Psych123!`



### Endpoints


##### GET `/`

- Public
- Just a generic homepage that will return a json object `"This is the homepage!"`

##### GET `/login`

- Public
- Returns the url for the Auth0 login page:
```
{
    "url": "https://leyis-csrp.us.auth0.com/authorize?audience=csrp&response_type=token&client_id=POIEWgqUFHOKEk64fp2fDeA0LTvbuu6x&redirect_uri=https://csrp-deploy.herokuapp.com/locations"
}
```

##### GET `/locations`

- Permission required: `get:inventory`
- Returns the success value, and a list of all locations
- Sample output:
```
{
    "locaions": [
        {
            "id": 1,
            "name": "closet"
        },
        {
            "id": 2,
            "name": "attic"
        }
    ],
    "success": true
}
```

##### POST `/locations`

- Permission required: `add:inventory`
- Adds a new location with the specified name to the database
- Returns the success value and the id of the newly added location
- The names of locations cannot repeat
- Sample input:
```
{
    "name": "new location"
}
```
- Sample output:
```
{
    "new_id": 2,
    "success": true
}
```

##### GET `/locations/<location_id>`

- Permission required: `get:inventory`
- Returns the success value and a list of clothes stored at the specified location
- Sample output:
```
{
    "clothes": [
        {
            "category": "shirt",
            "description": "green long sleeve",
            "id": 3,
            "location": 1
        },
        {
            "category": "pants",
            "description": "khaki short",
            "id": 4,
            "location": 1
        }
    ],
    "success": true
}
}
```

##### PATCH `/locations/<location_id>`

- Permission required: `edit:inventory`
- Updates the name of the specified location
- Returns the success value and the id of the updated location
- The names of locations cannot repeat
- Sample input:
```
{
    "name": "location updated"
}
```
- Sample output:
```
{
    "updated_id": 2,
    "success": true
}
```

##### DELETE `/locations/<location_id>`

- Permission required: `delete:inventory`
- Deletes the selected location from the database
- Only empty locations can be deleted
- Sample output:
```
{
    "deleted_id": 2,
    "success": true
}
```

##### GET `/clothes`

- Permission required: `get:inventory`
- Returns the success value, and a list of all clothes
- Sample output:
```
{
    "clothes": [
        {
            "category": "shirt",
            "description": "blue",
            "id": 1,
            "location": 1
        },
        {
            "category": "shirt",
            "description": "green",
            "id": 2,
            "location": 2
        }
    ],
    "success": true
}
```

##### POST `/clothes`

- Permission required: `add:inventory`
- Adds a new piece of clothing to the dataase using the specified information
- Returns the success value and the id of the newly added clothing
- Sample input:
```
{
    "location": "1",
    "category": "jacket",
    "description": "blue denim"
}
```
- Sample output:
```
{
    "new_id": 3,
    "success": true
}
```

##### PATCH `/clothes/<clothes_id>`

- Permission required: `edit:inventory`
- Updates the selected piece of clothing using the given information
- Returns the success value and the id of the updated clothing
- Sample input:
```
{
    "location": "1",
    "category": "jacket updated",
    "description": "blue denim updated"
}
```
- Sample output:
```
{
    "updated_id": 3,
    "success": true
}
```

##### DELETE `/clothes/<clothes_id>`

- Permission required: `delete:inventory`
- Deletes the selected piece of clothing from the database
- Sample output:
```
{
    "deleted_id": 3,
    "success": true
}
```






