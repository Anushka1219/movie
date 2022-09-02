from flask import Flask, jsonify, request
import csv


allmovies=[]
likedmovies=[]
unlikedmovies=[]
unwatchedmovies=[]


with open("movies.csv") as f:
    reader=csv.reader(f)
    data=list(reader)
    allmovies=data[1:]

print(allmovies)

app = Flask(__name__) 
@app.route("/get-movie")
def get_movie():
    return jsonify({ "data": all_movies[0], "status": "success" })

@app.route("/likedmovies",methods=["POST"])
def likedmovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    likedmovies.append(movie)
    return jsonify({"status":"success"}),201

@app.route("/unlikedmovies",methods=["POST"])
def unlikedmovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    unlikedmovies.append(movie)
    return jsonify({"status":"success"}),201

@app.route("/unwatchedmovies",methods=["POST"])
def unwatchedmovies():
    movie=allmovies[0]
    allmovies=allmovies[1:]
    unwatchedmovies.append(movie)
    return jsonify({"status":"success"}),201

if __name__ == "__main__":
    app.run()




    
        
        

