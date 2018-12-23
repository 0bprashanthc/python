import wolframalpha
import wikipedia

print("Hey there! I am Tamu, how can I help you?")
while True:
    input = raw_input()
    try:
        app_id = "9U3AR2-V634XQ5Q6T"
        client = wolframalpha.Client(app_id)
        response = client.query(input)
        print(next(response.results).text)
    except:
        print(wikipedia.summary(input,sentences=2))

