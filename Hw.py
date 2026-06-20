print("Hi how are you, I am ARJ chatbot")
name = input("What is your name? ")
print("Hi", name, "nice to meet you")
mood = input("How has your day been? ")

if mood.lower() == "good":
    print("That's great to hear, I hope the rest of your day is going to be good too")
elif mood.lower() == "bad":
    print("I'm sorry your day has been bad. Think of something that would get your mind off it, like watching a movie or playing a video game. I hope the rest of your day is going to be great")
else:
    print("That's okay, but your day can't be neutral, mid, or okay. It should be great. Do something you always wanted to do")
end=input("Do you want to continue talking?")
if end.lower() =="yes":
    print("Great, I am happy to continue talking with you")
else:
    print("Okay, I hope you have a great day")
