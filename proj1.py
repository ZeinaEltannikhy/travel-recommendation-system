import pandas as pd
import numpy as np

# Load the datasets
flights = pd.read_csv('flights.csv')
users = pd.read_csv('users.csv')
hotels = pd.read_csv('hotels.csv')

def memo(i, j, memo_dict):
    if (i, j) in memo_dict:
        return memo_dict[(i, j)]
    return None

def set_memo(i, j, value, memo_dict):
    memo_dict[(i, j)] = value

# Merge the flights, users, and hotels dataframes using travelCode and userCode columns
data = pd.merge(flights, users, on='userCode')
data = pd.merge(data, hotels[['travelCode', 'userCode', 'hotel_name','place','total','days']], on=['travelCode', 'userCode'])

def travel_recommendation(userCode, budget, num_cities, data):
    # Get unique cities in the dataset
    cities = np.unique(np.concatenate((data['from'], data['to'])))
    
    city_attractions = {}
    for city in cities:
        city_attractions[city] = list(np.unique(data[(data['from'] == city) | (data['to'] == city)]['place']))

    # Create a dictionary to store the costs of attractions in each city
    city_costs = {}
    for city in cities:
        city_costs[city] = np.unique(data[(data['from'] == city) | (data['to'] == city)]['total'])

    # Create a dictionary to store the distance between each pair of cities
    city_distances = {}
    for city1 in cities:
        city_distances[city1] = {}
        for city2 in cities:
            if city1 != city2:
                distance = np.min(data[(data['from'] == city1) & (data['to'] == city2)]['distance'])
                city_distances[city1][city2] = distance

    memo_dict = {}

    def knapsack(i, j, visited):
        if i == 0 or j == 0:
            return 0

        memo_value = memo(i, j, memo_dict)
        if memo_value is not None:
            return memo_value

        if np.min(city_costs[cities[i - 1]]) <= j and cities[i - 1] not in visited:
            max_attractions = 0
            attraction_cost = 0
            temp_j = j
            for c in city_costs[cities[i - 1]]:
                if c <= temp_j:
                    max_attractions += 1
                    attraction_cost = c
                    temp_j -= c

            if attraction_cost <= j:
                value = max(knapsack(i - 1, j, visited), max_attractions + knapsack(i - 1, j - attraction_cost, visited + [cities[i - 1]]))
            else:
                value = knapsack(i - 1, j, visited)
        else:
            value = knapsack(i - 1, j, visited)

        set_memo(i, j, value, memo_dict)
        return value

    # Extract the optimal solution from the memoization dictionary
    solution = []
    i = num_cities
    j = budget
    visited = []
    while i > 0 and j > 0:
        if knapsack(i, j, visited) != knapsack(i - 1, j, visited):
            solution.append(cities[i - 1])
            for attraction_cost in city_costs[cities[i - 1]]:
                if attraction_cost <= j:
                    j -= attraction_cost
            visited.append(cities[i - 1])
        i -= 1

    # Reverse the solution list to get the recommended cities
    recommended_cities = solution[::-1]

    # Print the recommended travel plan and total distance
    for i, city in enumerate(recommended_cities):
        flightType = data[data['place'] == city]['flightType'].iloc[0]
        agency = data[data['place'] == city]['agency'].iloc[0]
        days = data[data['place'] == city]['days'].iloc[0]
        hotel = data[data['place'] == city]['hotel_name'].iloc[0]
        total = data[data['place'] == city]['total'].iloc[0]

        print(f"{i + 1}. {city}")
        print("Flight Type:", flightType)
        print("Agency:", agency)
        print("Days:", days)
        print("Hotel:", hotel)
        print("total:", total)
        print()  # Add a blank line between each city

# Get user input for userCode, budget, and num_cities
userCode = int(input("Enter userCode: "))
budget = float(input("Enter budget: "))
num_cities = int(input("Enter number of cities: "))

# Call the travel_recommendation function with the user input
travel_recommendation(userCode, budget, num_cities, data)  