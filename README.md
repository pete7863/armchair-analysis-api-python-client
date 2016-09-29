# About
This is a Python client library for the Armchair Analysis REST API (see http://www.armchairanalysis.com/data-api.php).

# Python Version
This library is intended for use with Python 3.3+. 

# Getting Started
## Initializing the Client
Initializing the client can be done with the following call:

```
client.init("USER", "PASS")
```

Where "USER" and "PASS" are the username and password for the Armchair Analysis.

##Example
Now that the client is initialized, fetch data from the API using the internal endpoints module.
For example, use the following code to fetch the player data type for Randy Moss:

```
player = endpoints.player.get_player_by_full_name("Randy Moss")
```

One can now use the following code to obtain a list of the touchdown data type for all of Randy Moss' career touchdowns:

```
tds = endpoints.player.get_touchdowns(player._player)
```
NOTE: reference http://www.armchairanalysis.com/apidoc/ for the properties present in each endpoint. In order to access those properties, append a "_" to the beginning of the property name as seen above.

Finally, the following statements could be used to print out the length in yards of each of those touchdowns:

```
for td in tds:
    print(td._yds)
```
