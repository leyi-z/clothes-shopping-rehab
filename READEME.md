## API Reference



### About This API

I have A LOT of clothes, but it all gets forgotten whenever I see a nice new dress. My (hypothetical) psychiatrist suggests that I make a list of all the clothes I own, along with the places they are stored at. The lists helped me realize what I already I have and what I actually need. Now I'm buying much less clothes and saving an extra $200 every month! This web app is created so it's easier for me to create the lists and update them. My (hypothetical) psychiatrist will have some access to the lists so we can both keep track on my progress.



### To Get Started

#### Heroku

The api is deployed using Heroku. The host url is `csrp-deploy.herokuapp.com`. You can access the homepage with the url `https://csrp-deploy.herokuapp.com/`

#### Frontend

This web app doesn't have a frontend yet but hopefully it will soon!

#### Dependency

In case you want to run the app locally, all required packages are specified in the file `requirements.txt`. You can use the command `pip install -r requirements.txt` to install all of them at once.

#### Tests

I created some postman tests for the api. To use them, simply import the file `tests/csrp-tests.postman_collection.json` into postman.



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
- jwt token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdQdUV5MzNfS00xaVpXUl9INU9EcyJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNzcnAudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTVjNzg1OGEyNGQ3MDA3MGVmYTQ4YiIsImF1ZCI6ImNzcnAiLCJpYXQiOjE2MTYzOTU2MDAsImV4cCI6MTYxNjQ4MjAwMCwiYXpwIjoiUE9JRVdncVVGSE9LRWs2NGZwMmZEZUEwTFR2YnV1NngiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImFkZDppbnZlbnRvcnkiLCJkZWxldGU6aW52ZW50b3J5IiwiZ2V0OmludmVudG9yeSIsInVwZGF0ZTppbnZlbnRvcnkiXX0.qU4CZ307M6Ku8giiejG9gsESDSR-6KQ07fzfr2MatVdrfEPOMSDdOWjvL3ZP-cp1j1I7yOLwqljtb0O3PoGmiNb33hj-ax_ItQaOLG92iVsugEJybjWA2Vu1mkc3ZkL3-m-D65094bfPWqJde95Er0HFnU-hQsPAPKrjMd8JhIpk5yvdcoyoN_LP3fP7w_TiGELiZ9vCBY2pPa__2dtMxPGnBdsz3Q9ts3ufNr71Rb9HdR8LNhGtMU1RwudkWQxr44y5PDHZABOagtDUUF0okAyl29zuKvLcM_dh0DXoDny1okdlibeUc4P6EHlvjl92_bD-JCeq-jFzByfEz2S6CA`

##### Test User: Psych
- username: `psych@gmail.com`
- password: `Psych123!`
- jwt token: `eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkdQdUV5MzNfS00xaVpXUl9INU9EcyJ9.eyJpc3MiOiJodHRwczovL2xleWlzLWNzcnAudXMuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDYwNTVjNjhlNDFiODk3MDA2OTAyOGMzZCIsImF1ZCI6ImNzcnAiLCJpYXQiOjE2MTY0MDAzMDcsImV4cCI6MTYxNjQ4NjcwNywiYXpwIjoiUE9JRVdncVVGSE9LRWs2NGZwMmZEZUEwTFR2YnV1NngiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDppbnZlbnRvcnkiXX0.NGxPr9hasEgskcKTstYi4Qr15bcnLOMpogNbP3gqzMQO44k2kjLJmLfsfEKI5naIRa647ssLgQkmE7-t6pBxiIMpUuOONv_HoDVmsnCwecGh-romq8pKp9xY8Q9rij3VU1wm9RT7gPdzv-FfiYqkigHhxtVu1bOtdvNh9qcbrteWNW-WciTZtOk99P_gbYZ3aw_90un8vk_UCwPrHTazRdZ6bpi4pmq2Dra7jhfS9eBrUKIlLUWF_j2kHYCY_H7TcTR4Cfk3AIH0xGDC9gOnxDPROV6mjBdZh8JC5uaZK4IPGmAF6y9X1ZY2Cmv5zb09vER2aH7AmycWpmJWUCh3Hg`



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






