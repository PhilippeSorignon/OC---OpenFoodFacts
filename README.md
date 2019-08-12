# Utilisez les données publiques de l'OpenFoodFacts

## settings.py
The user has to create a "settings.py" file with his MySQL credentials

USER_NAME = ''
PASSWORD = ''



## First screen
The user has to chose if he wants to configure the database or to use the program


### Configure database
The user has to enter his database credential


#### Copy data from OpenFoodFacts
The system make an API call to copy data from OpenFoodFacts


#### Save data to the database
The system save the copied data to the database


### Replace or display
The user has to chose if he wants to find a better food or to display substituted food


#### Replace food
The user select the food he wants to replace


##### Check database
The system check the database to find a match between the user request and a stored food


#### Display substituted food
The system display the substituted food to the user
