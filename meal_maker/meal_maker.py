# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 11:08:31 2021

@author: =GV=
"""
import random

class courses(object):
    def __init__(self):
        self.appetizers = []
        self.mains = []
        self.desserts = []
    
    def getAppetizers(self):
        return self.appetizers
    
    def getMains(self):
        return self.mains
    
    def getDesserts(self):
        return self.desserts
    
    def setAppetizers(self, appetizer):
        self.appetizers.append(appetizer)
    
    def setMains(self, dish):
        self.mains.append(dish)
        
    def setDesserts(self, dessert):
        self.desserts.append(dessert)

class menu(object):
    def __init__(self):
        # using composition instead of inheritance
        self._courses = courses()
        
    def getCourses(self):
        return {'appetizers': self._courses.appetizers, 'mains': self._courses.mains, 'desserts':self._courses.desserts}
    
    def addDishToCourse(self, courseName, dishName, dishPrice):
        self.attributeVal = getattr(self._courses, courseName, [])
        self.attributeVal.append({'name': dishName, 'price': dishPrice})
        setattr(self._courses, courseName, self.attributeVal)
    
    def getRandomDishFromCourse(self, courseName):
        self.dish = getattr(self._courses, courseName)
        return self.dish[random.randint(0, len(self.dish) - 1)]
    
    def generateRandomMeal(self):
        self.appetizer = self.getRandomDishFromCourse('appetizers')
        self.main = self.getRandomDishFromCourse('mains')
        self.dessert = self.getRandomDishFromCourse('desserts')
        self.total = self.appetizer['price'] + self.main['price'] + self.dessert['price']
        return f'Appetizer:\t{self.appetizer["name"]}\nMain:\t\t{self.main["name"]}\nDessert:\t{self.dessert["name"]}\nTotal:\t\t{self.total}'



# test
menuVar = menu()
menuVar.addDishToCourse('appetizers', 'Cheese sticks', 5.80)
menuVar.addDishToCourse('appetizers', 'Tacos', 6.50)
menuVar.addDishToCourse('appetizers', 'Chicken wings', 7.00)
menuVar.addDishToCourse('mains', 'Steak', 20.00)
menuVar.addDishToCourse('mains', 'Lamb-chops', 16.50)
menuVar.addDishToCourse('mains', 'Cheese Pizza', 12.80)
menuVar.addDishToCourse('desserts', 'Ice cream', 3.25)
menuVar.addDishToCourse('desserts', 'Pie', 4.50)
menuVar.addDishToCourse('desserts', 'Cake', 3.00)
menuVar.addDishToCourse('drinks', 'Coffee', 2.25) #test setattr catch for courseName not in courses
meal = menuVar.generateRandomMeal()
print(meal)



