### Basic




### Data Structure


##### Table `Location`

- storage locations
- columns:
	- id: primary key
	- container
	- room

##### Table `Clothes`

- created by user via button `create inventory`
- columns:
	- id: primary key
	- location: foreign key
	- category
	- description
	- quantity
	



### Authentication


#### Roles

##### Recorder 
- basically a general user
- has the following permissions
	- `get:inventory`
	- `add:inventory` 
	- `edit:inventory`
	- `delete:inventory`

##### Psychiatrist
- can see what the recorder has
- has the following permissions:
	- `get:inventory`




### Backend


#### Endpoints


##### GET `/`

- public
- generic homepage & user login
- `curl --request GET http://localhost:5000/`

##### GET `/login`

- public
- login/signup page; probably going to be auth0?
- `curl --request GET http://localhost:5000/login`

##### GET `/locations`

- permission required: `get:inventory`
- returns the contents of user's table `locations`
- `curl --request GET http://localhost:5000/locations`

##### GET `/locations/<location_id>`

- permission required: `get:inventory`
- returns the contents of user's table `locations`
- `curl --request GET http://localhost:5000/locations`

##### POST `/locations`

- permission required: `add:inventory`
- add entries to user's table `locations`
- `curl -X POST http://127.0.0.1:5000/locations`

##### PATCH `/locations`

- permission required: `edit:inventory`
- update entries of user's table `locations`
- `curl -X PATCH http://127.0.0.1:5000/locations`

##### DELETE `/locations`

- permission required: `delete:inventory`
- delete entries of user's table `locations`
- `curl -X DELETE http://127.0.0.1:5000/locations`

##### GET `/clothes`

- permission required: `get:inventory`
- returns the contents of user's table `clothes`
- `curl --request GET http://localhost:5000/clothes`

##### POST `/clothes`

- permission required: `add:inventory`
- add entries to user's table `clothes`
- `curl -X POST http://127.0.0.1:5000/clothes`

##### PATCH `/clothes`

- permission required: `edit:inventory`
- update entries of user's table `clothes`
- `curl -X PATCH http://127.0.0.1:5000/clothes`

##### DELETE `/clothes`

- permission required: `delete:inventory`
- delete entries of user's table `clothes`
- `curl -X DELETE http://127.0.0.1:5000/clothes`






