import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    
    [r"(hi|hello|hey|greetings)",  
     ["Hello! I'm Nubye. What's your name?"]],
    
    [r"(.*my name is|.*i am|.*call me) (.*)",  
     ["Nice to meet you, %2! How are you today?"]],
    
    [r"(i am|i'm) (good|great|fine|ok|okay|happy)",  
     ["That's nice to hear! What would you like to talk about?"]],
    
    [r"(i am|i'm) (bad|sad|tired|angry)",  
     ["I'm sorry to hear that. Maybe I can help with something?"]],
    
    [r"(who are you|what are you|tell me about yourself)",  
     ["I'm Nubye, a simple chatbot created using Python's NLTK library"]],
    
    [r"how are you",  
     ["I'm just a computer program, so I don't have feelings, but I'm functioning well!"]],
    
    [r"(bye|goodbye|see ya|quit)",  
     ["Goodbye! It was nice talking to you."]],
    
    [r"(.*)",  
     ["I'm not sure I understand. You can ask me about myself or tell me how you feel."]]
]

my_reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "i'm": "you are",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "your": "my",
    "yours": "mine"
}

def nubye_chat():
    print("=" * 40)
    print("Nubye: Hi! I'm your chatbot friend. Type 'quit' to exit.")
    print("=" * 40)
    
    chat = Chat(pairs, my_reflections)
    chat.converse()

if __name__ == "__main__":
    nubye_chat()
