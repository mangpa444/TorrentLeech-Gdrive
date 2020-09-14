from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
	TG_BOT_TOKEN= "1357869332:AAG0RGnwhifl0HKnMAzAy6k9IIZkzZZK-Xw"
	APP_ID = 1709361
	API_HASH = "68f63ad737cb90ff1e12f3bfe0d0e06b"
	OWNER_ID = "1135774092" #ID of bot owner
	AUTH_CHANNEL = [-1001417827909]
	DESTINATION_FOLDER = "HelloMan" #Name of your folder read readme7
	ENV = "ANYTHING"
	CHUNK_SIZE = 128
	EDIT_SLEEP_TIME_OUT = 15
	RCLONE_CONFIG = """type = drive/nscope = drive/nroot_folder_id = 0AN7TEgZi8jMjUk9PVA/ntoken = {"access_token":"ya29.a0AfH6SMA0q1SbxiPAW1ZF8GLnKQtHmMM4Jqsp5hTk6oju75fVLYUeQDjBw7RkjmQorfWIMggnETY3eMkI2gC89AlX0DYgj4lDQ5x2O42J6bBIzBKlHW8-Gh1Q5IPx-8kwE7c5uaZEK7PZ8_ZAhwijnHbB4r1zPZRakvM","token_type":"Bearer","refresh_token":"1//04tXHjMPBozFhCgYIARAAGAQSNwF-L9IrgYi1TQLHQ_sGXbYN-9ZgMKp8xmDZaQKIRmt1v3Vur9wM2aLRxpM2OcMUTg8pESsPK0E","expiry":"2020-09-14T05:23:25.20138867+07:00"}"""
	#fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
