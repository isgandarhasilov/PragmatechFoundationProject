from flask import Flask,render_template,redirect,request

app=Flask(__name__)

users=[
]
id=1
@app.route('/')
def index():
    return render_template('index.html',users=users)

@app.route('/add',methods=['GET','POST'])
def add():
    global id
    if request.method=='POST':
        user={
        'id':id,
        'name':request.form['ad'],
        'surname':request.form['soyad']
    }
        users.append(user)
        id+=1
        return redirect('/')
    return render_template('add.html')

@app.route('/delete/<silinecekId>')
def delete(silinecekId):
    for user in users:
        if user['id']==int(silinecekId):
            users.remove(user)
            return redirect('/')
    return redirect('/')


if __name__=='__main__':
    app.run(debug=True)