from flask import Flask, render_template , request
import pandas
data_csv = pandas.read_csv('MetaData.csv')
data=pandas.read_csv('MetaData.csv').values.tolist()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/' , methods=['GET'])
def home():
    
    return render_template('home.html',name="None" , catagory="None" )

@app.route('/movie',methods = ['POST','GET'])
def movie():
    if request.method == 'POST':
       movie=request.form.to_dict()
       movie['index']= getIndex(movie['Name'])
       if movie['index']=="Not Found":
            return render_template('home.html',name="Not Found" , catagory="None" )
       movie['Catagory']=getCatagory(movie['index'])
       print(movie)
       movie['suggestedmovie']=KNN(movie['index'])
       return render_template("home.html", name=movie['Name'] , catagory=movie['Catagory'])
       
def getCatagory(index):
    Catagory=""
    for i in range(2 , len(data_csv.columns)):
        if data[index][i]==1:
            Catagory=Catagory+ "|"+ data_csv.columns[i]
    return Catagory

def getIndex(name):
    for i in range(0,len(data)):
        if(name==data[i][1]):
            return i

    return "Not Found"
def KNN(index):
    
if __name__ == '__main__':
    app.run(debug=True)



