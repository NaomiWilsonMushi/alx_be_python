weather = input("What's the weather like today? (sunny/rainy/cold): ")

# weather_advice.py

# Step 1: Ask user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ")

# Step 2: Give advice using if/elif/else
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
