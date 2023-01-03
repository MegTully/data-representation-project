from flask import Flask, jsonify, abort, request
from ChristmasMovieDAO import ChristmasMovieDao

app = Flask(__name__,static_url_path='',static_folder='static')



# get all movies and return in json format
@app.route('/ChristmasMovies')
def getAll():
    results = ChristmasMovieDao.getAll()
    return jsonify(results)

# search a list for an id and return the object with that id
@app.route('/ChristmasMovies/<int:id>')
def findById(id):
    foundMovies = ChristmasMovieDao.findByID(id)

    return jsonify(foundMovies)
    #foundMovies = list(filter(lambda t : t["id"]== id, ChristmasMovies))
    #if len (foundMovies)==0:
    #    return jsonify({}), 204
    #return jsonify(foundMovies[0])

# create a new entry for Christmas movie
@app.route('/ChristmasMovies', methods = ['POST'])
def createChristmasMovie():
    if not request.json:
        abort(400)
    # other checking 
    ChristmasMovie = {
        "title": request.json['title'],
        "genre": request.json['genre']
        }
    values =(ChristmasMovie['title'],ChristmasMovie['genre'])
    newId = ChristmasMovieDao.create(values)
    ChristmasMovie['id'] = newId
    return jsonify(ChristmasMovie)

# Update an entry in the christmas movie list by searching the Id then changing the values
@app.route('/ChristmasMovies/<int:id>', methods=['PUT'])
def UpdateById(id):
    foundMovies =ChristmasMovieDao.findByID(id)
    if not foundMovies:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json

    if 'title' in reqJson:
        foundMovies['title'] = reqJson['title']
    if 'genre' in reqJson:
        foundMovies['genre'] = reqJson['genre']
    values = (foundMovies['title'],foundMovies['genre'],foundMovies['id'])
    ChristmasMovieDao.update(values)
    return jsonify(foundMovies)


# Find and entry in the christmas movie list by searching its id and then delete it
@app.route('/ChristmasMovies/<int:id>', methods=['DELETE'])
def DeleteById(id):
    ChristmasMovieDao.delete(id)
    return jsonify({"done":True})

if __name__ == "__main__":
    app.run(debug=True)