print("    " + "HOW ARE YOU FEELING? ")

message = input(">")
words = message.split(" ")
emojis = {
    "sad": "😔",
    "good": "😊",
    "happy": "😆",
    "angery": "😡",
    "crush": "😍",
    "love": "❤",
}

output = ""

for word in words:
   output += emojis.get(word, word)
print(output)