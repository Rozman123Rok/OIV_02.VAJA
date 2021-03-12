from website import create_app

app = create_app() # ustvarimo app

if __name__ == '__main__':
    app.run(debug=True) # pozenemo app ce zazenemo file direktno (True je da se sama reruna ko spreminjamo)