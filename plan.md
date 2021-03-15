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

##### Manager
- can manage certain aspects of database
- has following permissions in addition to Recorder
	- get category
	- add category
	- patch category
	- delete category





### Backend


#### Endpoints


##### GET `/`

- no permission required
- generic homepage
- test with: `curl --request GET http://localhost:5000/`


##### GET `/login`

- no permission required
- login/signup page; probably going to be auth0?


##### GET `/<user_id>`

- recorder role required
- unique to each user
- checks if user created inventory exists, and returns:
	- `create inventory` button if doesn't exist
	- user's inventory at primary location if exists
	
##### POST `/<user_id>/create`

- recorder role required
- creates user tables: location and clothes

##### GET `/<user_id>/locations`

- recorder role required
- returns the contents of table `locations`

##### POST `/<user_id>/locations`

- recorder role required
- add entries to the table `locations`

##### PATCH `/<user_id>/locations`

- recorder role required
- update entries of the table `locations`

##### DELETE `/<user_id>/locations`

- recorder role required
- delete entries of the table `locations`

##### GET `/<user_id>/clothes`

- recorder role required
- returns the contents of table `clothes`

##### POST `/<user_id>/clothes`

- recorder role required
- add entries to the table `clothes`

##### PATCH `/<user_id>/clothes`

- recorder role required
- update entries of the table `clothes`

##### DELETE `/<user_id>/clothes`

- recorder role required
- delete entries of the table `clothes`

##### GET `/categories`

- manager role required
- returns the contents of table `categories`

##### POST `/categories`

- manager role required
- add entries to the table `categories`

##### PATCH `/categories`

- manager role required
- update entries of the table `categories`

##### DELETE `/categories`

- manager role required
- delete entries of the table `categories`

















