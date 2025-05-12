# Travel Recommendation System

This project is a Python-based travel recommendation system that suggests cities to a user based on their budget and the number of cities they wish to visit. The system uses data from flights, hotels, and users to generate optimal travel plans using a dynamic programming approach.

## 📁 Project Structure
- `proj1.py` — Main script that handles input, processing, and outputs travel recommendations.
- `users.csv` — Dataset of users with their travel preferences.
- `flights.csv` — Dataset containing flight information between cities.
- `hotels.csv` — Dataset of hotels, destinations, and associated costs.

## ⚙️ How to Use
1. Make sure all CSV files (`users.csv`, `flights.csv`, `hotels.csv`) are in the same directory as `proj1.py`.
2. Run the script:
```bash
python proj1.py

Enter the following when prompted:

userCode: A user code from the dataset.

budget: Your budget for the trip.

number of cities: How many cities you'd like to visit.

🧠 Methodology
The system uses a dynamic programming-based knapsack algorithm to choose the best combination of cities that fit within the given budget.

Recommendations are based on maximizing attractions and minimizing cost.

✅ Features
Intelligent city recommendation

Budget-aware travel planning

Hotel and flight info integration

🛠️ Requirements
Python 3

pandas

numpy

Install requirements with:

pip install pandas numpy

👤 Author
ZeinaEltannikhy

