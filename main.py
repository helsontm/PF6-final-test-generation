import json
import requests

def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    typicalDish = json.loads(response.content)
    
    
    return   {
        "id": num,
        "name": typicalDish.get("name", f"Dish {num}"),
        "description": typicalDish.get("description", "No description available."),
        "Ingredients": typicalDish.get("ingredients", "No ingredients available."),
        
    }


def main():
  print("Hello learners!")
  print(dish_fetch(input("Enter a number to fetch a typical dish: ")))

if __name__=="__main__":
  main()