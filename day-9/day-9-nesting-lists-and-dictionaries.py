#Nesting 
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting list in a dictionary 
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg"]
}

#Nest dictionary in a dictionary 
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg"], "total visits": 5}
}

#Nest dictionary inside a list 
travel_log = [
    {
    "country": "France", 
    "cities_visited": ["Paris", "Lille", "Dijon"], 
    "total_visits": 12
    }, 
    {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg"], 
    "total visits": 5}
]
