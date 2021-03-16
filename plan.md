## Core


### Data Structure


##### General: `Category`

- categories of clothes
- Columns:
	- id: primary key
	- name: e.g. tshirt, jacket, etc

##### User Created: `Location_<user_id>`

- storage locations
- columns:
	- id: primary key
	- container
	- room

##### User Created: `Clothes_<user_id>`

- created by user via button `create inventory`
- columns:
	- id: primary key
	- category: foreign key
	- location: foreign key
	- description
	- quantity
	



### Authentication


#### Roles

##### Recorder
- basically a general user
- has the following permissions
	- get inventory
	- create inventory 
	- patch inventory
	- delete inventory





### Backend


#### Endpoints


##### GET `/`

- public
- generic homepage
- `curl --request GET http://localhost:5000/`

##### GET `/login`

- public
- login/signup page; probably going to be auth0?
- `curl --request GET http://localhost:5000/login`

##### GET `/<user_id>`

- user authentication required
- user's homepage
- checks if user created inventory exists, and returns:
	- `create inventory` button if doesn't exist
	- user's inventory at primary location if exists
- `curl --request GET http://localhost:5000/user123`
	
##### POST `/<user_id>/create`

- user authentication required
- creates user tables: location and clothes
- `curl -X POST http://localhost:5000/user123/create`

##### GET `/<user_id>/locations`

- user authentication required
- returns the contents of user's table `locations`
- `curl --request GET http://localhost:5000/user123/locations`

##### POST `/<user_id>/locations`

- user authentication required
- add entries to user's table `locations`
- `curl -X POST http://127.0.0.1:5000/user123/locations`

##### PATCH `/<user_id>/locations`

- user authentication required
- update entries of user's table `locations`
- `curl -X PATCH http://127.0.0.1:5000/user123/locations`

##### DELETE `/<user_id>/locations`

- user authentication required
- delete entries of user's table `locations`
- `curl -X DELETE http://127.0.0.1:5000/user123/locations`

##### GET `/<user_id>/clothes`

- user authentication required
- returns the contents of user's table `clothes`
- `curl --request GET http://localhost:5000/user123/clothes`

##### POST `/<user_id>/clothes`

- user authentication required
- add entries to user's table `clothes`
- `curl -X POST http://127.0.0.1:5000/user123/clothes`

##### PATCH `/<user_id>/clothes`

- user authentication required
- update entries of user's table `clothes`
- `curl -X PATCH http://127.0.0.1:5000/user123/clothes`

##### DELETE `/<user_id>/clothes`

- recorder role required
- delete entries of user's table `clothes`
- `curl -X DELETE http://127.0.0.1:5000/user123/clothes`





## Optional


#### Role

##### Manager 
- can manage certain aspects of database
- has following permissions in addition to Recorder
	- get category
	- add category
	- patch category
	- delete category


#### Endpoints

##### POST `/categories`

- manager role required
- add entries to the table `categories`

##### PATCH `/categories`

- manager role required
- update entries of the table `categories`

##### DELETE `/categories`

- manager role required
- delete entries of the table `categories`

















