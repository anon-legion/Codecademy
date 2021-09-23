class Media {
    constructor(title, isCheckedOut = false, ratings = []) {
        this._title = title;
        this._isCheckedOut = isCheckedOut;
        this._ratings = ratings;
    }

    get title() {
        return this._title;
    }

    get isCheckedOut() {
        return this._isCheckedOut;
    }

    get ratings() {
        return this._ratings;
    }

    set isCheckedOut(status) {
        this._isCheckedOut = status;
    }

    toggleCheckOutStatus() {
        this.isCheckedOut ? this.isCheckedOut = false : this.isCheckedOut = true;
    }

    getAverageRating() {
        let sumRating = this.ratings.reduce((sum, rating) => sum + rating);
        return sumRating / this.ratings.length;
    }

    addRating(rating) {
        if (0 < rating && rating <= 5) {
            this._ratings.push(rating);
        } else {
            console.log('error: invalid rating!');
        }
        this._ratings.push(rating);
    }

}

class Book extends Media {
    constructor(author, title, pages) {
        super(title);
        this._author = author;
        this._pages = pages;
    }

    get author() {
        return this._author;
    }

    get pages() {
        return this._pages;
    }

}

class Movie extends Media {
    constructor(director, title, runTime) {
        super(title);
        this._director = director;
        this._runTime = runTime;
    }

    get director() {
        return this._director;
    }

    get runtime() {
        return this._runTime;
    }

}

class CD extends Media {
    constructor(artist, title, songs = []) {
        super(title);
        this._artist = artist;
        this._songs = songs;
    }

    get artist() {
        return this._artist;
    }

    get songs() {
        return this._songs;
    }

    shuffle() {
        let result = this.songs.slice(0), randomIndex;
        for (let i = this.songs.length - 1; i > 0; i--) {
            randomIndex = Math.floor(Math.random() * i);
            [result[i], result[randomIndex]] = [result[randomIndex], result[i]];
        }
        return result;
    }
}



const historyOfEverything = new Book('Bill Bryson', 'A Short History of Nearly Everything', 544)
historyOfEverything.toggleCheckOutStatus()
console.log(historyOfEverything.isCheckedOut)
historyOfEverything.addRating(4)
historyOfEverything.addRating(5)
historyOfEverything.addRating(5)
console.log(historyOfEverything.getAverageRating())

const speed = new Movie('Jan de Bont', 'Speed', 116)
speed.toggleCheckOutStatus()
console.log(speed.isCheckedOut)
speed.addRating(1)
speed.addRating(1)
speed.addRating(5)
console.log(speed.getAverageRating())
speed.addRating(6)

const Californication = ['Around the world', 'Parallel Universe', 'Scar Tissue', 'Otherside', 'Get On Top', 'Californication', 'Easily', 'Porcelain', 'Emit Remmus', 'I Like Dirt', 'This Velvet Glove', 'Savior'];
const RHCP = new CD('Red Hot Chili Peppers', 'Californication', Californication)
console.log(RHCP.shuffle())


