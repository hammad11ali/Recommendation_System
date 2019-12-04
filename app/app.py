from flask import Flask, render_template , request
import pandas
data_csv = pandas.read_csv('MetaData.csv')
data=pandas.read_csv('MetaData.csv').values.tolist()

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
@app.route('/' , methods=['GET'])
def home():   
    return render_template('home.html',name="None" , catagory="None" , suggestions=[] )

@app.route('/movie',methods = ['POST','GET'])
def movie():
    if request.method == 'POST':
        movie=request.form.to_dict()
        movie['index']= getIndex(movie['Name'])
        if movie['index']=="Not Found":
            return render_template('home.html',name="Not Found" , catagory="None" )
        movie['Catagory']=getCatagory(movie['index'])
        suggestedIndeces=KNN(movie['index'])
        suggestions=[]
        for i in suggestedIndeces:
            s=[]
            s.append(data[i][1])
            s.append(getCatagory(i))
            suggestions.append(s)
        return render_template("home.html", name=movie['Name'], catagory=movie['Catagory'] , suggestions=suggestions)
    else:
        return render_template('home.html',name="None" , catagory="None" , suggestions=[] )

       
       
def getCatagory(index):
    Catagory=""
    for i in range(2 , len(data_csv.columns)):
        if data[index][i]==1:
            Catagory=Catagory+ " | "+ data_csv.columns[i]
    return Catagory

def getIndex(name):
    for i in range(0,len(data)):
        if(name==data[i][1]):
            return i

    return "Not Found"
def KNN(index):
    import math
    distances=[]
    for i in range(0,len(data)):
        sum=0
        for j in range(2,len(data_csv.columns)):
            sum=float((((data[i][j]-data[index][j])**2))+sum)
        sum=math.sqrt(sum)
        distances.append((i,sum))
    distances.pop(index)    
    distance=Sort_Tuple(distances)
    
    indexes=[]
    for i in range(0,10):
        indexes.append(distance[i][0])
    
    return indexes

def Sort_Tuple(tup):  
    tup.sort(key = lambda x: x[1])  
    return tup  
            
if __name__ == '__main__':
    app.run(debug=True)



