from app import create_app

app=create_app('development2')

if __name__=='__main__':
    app.run(debug=True,port=6106)