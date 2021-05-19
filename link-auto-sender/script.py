from twilio.rest import Client

account_sid = 'put your account sid from twilio here'
auth_token = 'put the auth_token from twilio here'
client = Client(account_sid, auth_token)

linkTAFL = "https://zoom.us/j/92782378685?pwd=VTVKMnJ3aC9lR3diOG9PeEJxd2VWdz09"
linkMaths = "https://us02web.zoom.us/j/7543213087?pwd=QzNrMVFKSGZpMHAxU0ZWUEd1RndWdz09"
linkMP = "https://zoom.us/j/92441553219?pwd=Y25NVFM2YnBqRlpnS0pTeGpVWmdHZz09"
linkMentor = "https://us02web.zoom.us/j/2912114090?pwd=MXo5c1RPVURHeHRrb2llblFlVitVdz09"

def send():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your TAFL class is "+ linkTAFL,
        to='whatsapp:+91**********'
    )
    print(message.sid)


def send1():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Maths class is "+ linkMaths,
        to='whatsapp:+91**********'
    )
    print(message.sid)


def send2():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Microprocessor class is "+ linkMP,
        to='whatsapp:+91**********'
    )
    print(message.sid)


def send3():
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body="The link for your Mentoring class is "+ linkMentor,
        to='whatsapp:+91**********'
    )
    print(message.sid)
