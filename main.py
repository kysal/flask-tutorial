from website import create_app
import webbrowser

app = create_app()

if __name__ == '__main__':
    #webbrowser.open("http://127.0.0.1:5000", new=0, autoraise=True)

    app.run(debug=True)

    