import requests
import smtplib

def get_emails():
	emails={}

	email_file = open('emails.txt','r')

	for line in email_file:
		(email, name) = line.split(',')
		emails[email] = name.strip()

	return emails

def get_schedule():
	schedule_file = open('schedule.txt','r')
	schedule = schedule_file.read()

	return schedule

def get_weather_forecast():
	url = 'http://api.openweathermap.org/data/2.5/weather?id=1277333&units=imperial&appid=872dd0d54c54ce9e2b3ccc4fa27d1417'
	r= requests.get(url)
	weather_json= r.json()

	print(weather_json)

	description = weather_json['weather'][0]['description']
	print(description)
	
	temp_min = weather_json['main']['temp_min']
	print(temp_min)
	temp_max = weather_json['main']['temp_max']
	print(temp_max)

	forecast = 'The weather for today is '
	forecast += description + ' with max temp ' + str(temp_max) + ' and min temp ' + str(temp_min) 
	return forecast

def send_emails(emails, schedule, forecast):
	# connect to smtp server
	server = smtplib.SMTP('smtp.gmail.com', '587')
	# start tls encryption
	server.starttls()

	# login
	password = raw_input('whats ur password?: ')
	from_email = 'rlovish007@gmail.com'
	server.login(from_email, password)

	for to_email, name in emails.items():
		message = 'Subject: Welcome!\n Hi '+ name + '!\n\n' + forecast + '\n\n' + schedule + '\n\n'
		message += 'Hope you follow!'
		server.sendmail(from_email, to_email, message)
	server.quit()

def main():
	emails = get_emails()
	print(emails)

	schedule = get_schedule()
	print(schedule)

	forecast=get_weather_forecast()
	print(forecast)
	send_emails(emails, schedule, forecast)

main()