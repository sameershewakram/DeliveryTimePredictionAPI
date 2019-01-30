from webapp import app

app.config.from_object('config.DevelopmentConfig')

if __name__ == '__main__':
	app.run()