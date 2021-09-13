const team = {
    _players: [
        {
            fname: 'Michael',
            lname: 'Jordan',
            age: 23
        },
        {
            fname: 'Kobe',
            lname: 'Bryant',
            age: 34
        },
        {
            fname: 'Lebron',
            lname: 'James',
            age: 29
        }
    ],
    _games: [
        {
            opponent: 'Clippers',
            teamPoints: 104,
            opponentPoints: 32
        },
        {
            opponent: 'Lakers',
            teamPoints: 177,
            opponentPoints: 25
        },
        {
            opponent: 'Heat',
            teamPoints: 129,
            opponentPoints: 46
        }
    ],

    get players() {
        return this._players
    },

    get games() {
        return this._games
    },

    addPlayer(fname, lname, age) {
        this._players.push(
            {
                fname,
                lname,
                age
            }
        )
    },

    addGame(opponent, teamPoints, opponentPoints){
        this._games.push(
            {
                opponent,
                teamPoints,
                opponentPoints
            }
        )
    }
}

team.addPlayer('Steph', 'Curry', 28)
team.addPlayer('Lisa', 'Leslie', 44)
team.addPlayer('Bugs', 'Bunny', 76)
team.addGame('Bulls', 209, 26)
team.addGame('Hornets', 183, 35)
team.addGame('Cavaliers', 420, 69)
console.log(team.players)
console.log(team.games)