from CTFd import create_app
app = create_app()
app.run(debug=True, host="192.168.192.128", port=80)
