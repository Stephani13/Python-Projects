




class Foods:
    name = "Paella"
    typeOfFood = "Spanish Food"
    origin = "Spain"



    def info(self):
        info = "\nName: {}\nType of Food: {}\nOrigin: {}".format(self.name,self.typeOfFood,self.origin)
        return info


class Pasta(Foods):
    name = "Spaghetti"
    typeOfFood = "Pasta/Maccaroni"
    origin = 'Italia'


    def info(self):
        info = "\nMy favorite type of food is {}, {}. It is an original dish from {}. I hope to visit one day.".format(self.name,self.typeOfFood,self.origin)
        return info





class Fruit(Foods):
    name = "Banana"
    typeOfFood = "Botanically Berry"
    origin = "Southeast Asia"


    def info(self):
        info = "\n{} are originated in {}. Even though most consider it a fruit it is cathegorize as {}.".format(self.name,self.origin,self.typeOfFood)
        return info







if __name__ == "__main__":

    food = Foods()
    print(food.info())

    pasta = Pasta()
    print(pasta.info())


    fruit = Fruit()
    print(fruit.info())














