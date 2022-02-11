



#create parent class
class Foods:
    name = "Paella"
    typeOfFood = "Spanish Food"
    origin = "Spain"
    



    def info(self):
        info = "\nName: {}\nType of Food: {}\nOrigin: {}".format(self.name,self.typeOfFood,self.origin)
        return info

#creating two child class with two different attributes from parent class
class Pasta(Foods):
    name = "Spaghetti"
    typeOfFood = "Pasta/Maccaroni"
    origin = 'Italia'
    sauce = "Alfredo"
    Meat= "Meat Balls"


    def info(self):
        info = "\nMy favorite type of food is {}, {}. It is an original dish from {}. I hope to visit one day.I usually like to eat is with {}, but {} are not really my favorite.".format(self.name,self.typeOfFood,self.origin,self.sauce,self.Meat)
        return info





class Fruit(Foods):
    name = "Banana"
    typeOfFood = "Botanically Berry"
    origin = "Southeast Asia"
    color = 'Yellow'
    growingArea = "Trees"
    


    def info(self):
        info = "\n{} are originated in {}. Even though most consider it a fruit it is cathegorize as {}.They are {} colored and usually grows on {}".format(self.name,self.origin,self.typeOfFood,self.color,self.growingArea)
        return info





##calling all classes

if __name__ == "__main__":

    food = Foods()
    print(food.info())

    pasta = Pasta()
    print(pasta.info())


    fruit = Fruit()
    print(fruit.info())














