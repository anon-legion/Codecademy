const menu = {
    _courses: {
        appetizers: [],
        mains: [],
        desserts: []
    },
    get appetizers() {
        return this._courses.appetizers
    },
    get mains() {
        return this._courses.mains
    },
    get desserts() {
        return this._courses.desserts
    },
    set appetizers(appetizer) {
        this._courses.appetizers = appetizer
    },
    set mains(dish) {
        this._courses.mains = dish
    },
    set desserts(dessert) {
        this._courses.desserts = dessert
    },
    get courses() {
        return this._courses
    },
    addDishToCourse(courseName, name, price) {
        const dish = {
            name,
            price
        }
        this._courses[courseName] ? this._courses[courseName].push(dish) : this._courses[courseName] = [dish]
    },
    getRandomDishFromCourse(courseName) {
        return this[courseName][Math.floor(Math.random() * this[courseName].length)]
    },
    generateRandomMeal() {
        const appetizer = this.getRandomDishFromCourse('appetizers')
        const main = this.getRandomDishFromCourse('mains')
        const dessert = this.getRandomDishFromCourse('desserts')
        const total = appetizer.price + main.price + dessert.price
        return `Appetizer:\t${appetizer.name}\nMain:\t\t${main.name}\nDessert:\t${dessert.name}\nTotal:\t$${total}`
    }
}


// test

menu.addDishToCourse('appetizers', 'Cheese sticks', 5.80)
menu.addDishToCourse('appetizers', 'Tacos', 6.50)
menu.addDishToCourse('appetizers', 'Chicken wings', 7.00)
menu.addDishToCourse('mains', 'Steak', 20.00)
menu.addDishToCourse('mains', 'Lamb-chops', 16.50)
menu.addDishToCourse('mains', 'Cheese Pizza', 12.80)
menu.addDishToCourse('desserts', 'Ice cream', 3.25)
menu.addDishToCourse('desserts', 'Pie', 4.50)
menu.addDishToCourse('desserts', 'Cake', 3.00)
menu.addDishToCourse('drinks', 'Coffee', 2.25)
let meal = menu.generateRandomMeal()
console.log(meal)

/*
console.log(menu.appetizers)
menu.appetizers = 'foo'
console.log(menu.appetizers)
console.log(menu._courses['appetizers'] ? 'true' : 'false')
*/