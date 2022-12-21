from flask import Flask, jsonify, abort

app = Flask(__name__,static_url_path='',static_folder='static')

ChristmasMovies= [
    {'id':1,'title':'The Holiday', 'genre':'Romantic/Comedy'},
    {'id':2,'title':'Miracle on 34th Street', 'genre':'Drama'},
    {'id':3,'title':'The Polar Express', 'genre':'Family'},
    {'id':4,'title':'A Christmas Carol', 'genre':'Family'},
    {'id':5,'title':'Its a Wonderful Life', 'genre':'Drama'},
    {'id':6,'title':'elf', 'genre':'Family'},
    {'id':7,'title':'Home Alone 1', 'genre':'Comedy'},
    {'id':8,'title':'Home Alone 2', 'genre':'Comedy'},
    {'id':9,'title':'Home Alone 3', 'genre':'Comedy'},
    {'id':10,'title':'The Grinch', 'genre':'Family'}
    ]

NextId=11

# get all movies and return in json format
@app.route('/ChristmasMovies',methods=['GET'])
def getAllMovies():
    return jsonify(ChristmasMovies)

# search a list for an id and return the object with that id
@app.route('/ChristmasMovies/<int:id>')
def findById(id):
    foundMovies = list(filter(lambda t : t["id"]== id, ChristmasMovies))
    if len (foundMovies)==0:
        return jsonify({}), 204
    return jsonify(foundMovies[0])

@app.route('/rate/<ChristmasMoviesTitle>',methods=['POST'])
def rateMovies(ChristmasMoviesTitle):
    return jsonify({'title': ChristmasMoviesTitle})

@app.route('/rate/<ChristmasMoviesTitle>',methods=['GET'])
def getRatingsForMovies(ChristmasMoviesTitle):
    return 9

@app.route('/rate',methods=['GET'])
def getAllRatings():
    return jsonify({'title': 'test','count': 9})

@app.route('/rate/all',methods=['DELETE'])
def deleteAllRatings():
    return jsonify({'done': True})


if __name__ == "__main__":
    app.run(debug=True)