import json
import requests

def dish_fetch(num):
    response = requests.get(f"https://api-colombia.com/api/v1/TypicalDish/{num}")
    typicalDish = json.loads(response.content)
    
    
    return   {
        "id": num,
        "name": typicalDish.get("name", f"Dish {num}")
    }


#print(typicalDish["description"])
#print(typicalDish["ingredients"])







def main():
  print("Hello learners!")
  print(dish_fetch(input("Enter a number to fetch a typical dish: ")))

if __name__=="__main__":
  main()