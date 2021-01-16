from Data_mongo.base_document import Document, db


class Question(Document):
    '''
    {
    Id: autoinc,
    question: string,
    category: string,
    diff: int,
    answers:[{
        id: auto,
        answer: string,
        correctBool: bool,
    }]
    }
    '''
    collection = db.questions


class PlayedGame(Document):
    '''
    {
    Id: autoinc
    timestamp: timestamp
    players: [{
        id: int
        score: int
    }]
    }
    '''
    collection = db.playedgames


class User(Document):
    '''
    {
        id_user: autoinc
        username: String,
        email: String,
        password: String,
        score: int,
        friends: [
            id_user: String
        ]
    }
    '''
    collection = db.users
