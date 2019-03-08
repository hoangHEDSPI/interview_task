def groupDishes(dishes):
    ingredient = []
    for i in range(len(dishes)):
        for j in range(1, len(dishes[i])):
            ingredient.append(dishes[i][j])
    return ingredient

def dict_groupDishes(dishes):
    hash_ingredient = {}
    for i in range(len(dishes)):
        for j in range(len(dishes[i])-1):
            hash_ingredient[dishes[i][j+1]] = dishes[i][0]
    return hash_ingredient


dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

result = []
hash_result = {}
result = groupDishes(dishes)
hash_result = dict_groupDishes(dishes)
# result  =set(result)
# print type(result)
# print result
# for i in range(len(hash_result)):
print hash_result