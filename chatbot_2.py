import streamlit as st 
# import nltk 
import speech_recognition as sr
from nltk.chat.util import Chat, reflections


#Setting the data
data = [
    # Greetings
    [r"(.*Hi|.*Hello|.*Hey|.*What's up|.*Good [a-z]+)", 
     ["Hello! How can I assist you today?", 
      "Hi there! What brings you here?", 
      "Hey! Feel free to ask me anything.", 
      "Good day! How can I help you?"]],

    # Name-related Queries
    [r"(.*name|who are you|what are you called)", 
     ["My name is Uthman, your friendly chatbot.", 
      "I'm Uthman, nice to meet you!"]],

    # Age-related Queries
    [r"(.*age|.*old|how old are you)", 
     ["I'm 450 years old but still learning new tricks every day!", 
      "I’m ageless, but if you insist—450 years, give or take. 😉"]],

    # Economic Terms - Demand
    [r"(.*demand|.*what is demand|.*explain demand)", 
     ["Demand refers to the quantity of a good or service that consumers are willing and able to purchase at various prices over a given period of time.",
      "In economics, demand is how much of a product people want and can afford to buy at different prices."]],

    # Economic Terms - Supply
    [r"(.*supply|.*what is supply|.*explain supply)", 
     ["Supply is the total amount of a product or service that is available to consumers at various price levels over a certain time frame.",
      "In simple terms, supply is how much of a product producers are willing to sell at different prices."]],

    # Economic Terms - Inflation
    [r"(.*inflation|.*what is inflation|.*explain inflation)", 
     ["Inflation is the rate at which the general level of prices for goods and services rises, eroding purchasing power over time.",
      "In economics, inflation means prices increase, and the value of money decreases over time."]],

    # Economic Terms - GDP
    [r"(.*GDP|.*gross domestic product|.*what is GDP)", 
     ["Gross Domestic Product (GDP) measures the total monetary value of all finished goods and services produced within a country's borders in a specific time period.",
      "GDP is a key indicator of a country's economic performance and health."]],

    # Economic Terms - Opportunity Cost
    [r"(.*opportunity cost|.*what is opportunity cost|.*explain opportunity cost)", 
     ["Opportunity cost is the value of the next best alternative forgone when a choice is made.",
      "It represents the benefits you miss out on when choosing one option over another."]],

    # Economic Terms - Elasticity
    [r"(.*elasticity|.*what is elasticity|.*explain elasticity)", 
     ["Elasticity measures how much the quantity demanded or supplied of a product changes in response to price or income changes.",
      "For example, if the price of a good increases and demand drops significantly, it is considered elastic."]],

    # Economic Terms - Market Equilibrium
    [r"(.*market equilibrium|.*equilibrium|.*what is market equilibrium)", 
     ["Market equilibrium occurs when the quantity of a good demanded by consumers equals the quantity supplied by producers at a given price.",
      "At equilibrium, there’s no shortage or surplus of goods in the market."]],

    # Economic Terms - Comparative Advantage
    [r"(.*comparative advantage|.*what is comparative advantage)", 
     ["Comparative advantage occurs when a country or entity can produce a good or service at a lower opportunity cost than others.",
      "It’s the foundation of international trade and specialization."]],

    # Economic Terms - Fiscal Policy
    [r"(.*fiscal policy|.*what is fiscal policy|.*explain fiscal policy)", 
     ["Fiscal policy involves government spending and taxation decisions to influence economic activity.",
      "Governments use fiscal policy to promote growth, reduce unemployment, and control inflation."]],

    # Economic Terms - Monetary Policy
    [r"(.*monetary policy|.*what is monetary policy|.*explain monetary policy)", 
     ["Monetary policy refers to actions by a central bank to control money supply and interest rates to influence economic activity.",
      "It’s used to manage inflation, stabilize currency, and promote employment."]],

    # Economic Terms - Recession
    [r"(.*recession|.*what is a recession|.*explain recession)", 
     ["A recession is a period of significant economic decline, typically identified by a fall in GDP for two consecutive quarters.",
      "During a recession, businesses may close, unemployment rises, and consumer spending drops."]],

    # Economic Terms - Trade Deficit
    [r"(.*trade deficit|.*what is a trade deficit)", 
     ["A trade deficit occurs when a country imports more goods and services than it exports.",
      "It means the value of imports exceeds the value of exports."]],

    # Goodbye
    [r"(.*bye|.*goodbye|.*see you|.*take care)", 
     ["Goodbye! Have a fantastic day!", 
      "See you later! Don’t hesitate to reach out again.", 
      "Take care and stay awesome!"]],

    # Default Response
    [r"(.*)", 
     ["I'm not sure I understand. Can you please rephrase?", 
      "That's an interesting question. Let me think...", 
      "I couldn't quite catch that. Can you clarify?"]]
]



chatbot = Chat(data, reflections)

def main():
    st.title("Chatbot Interface")
    st.write("Hello! I'm your chatbot. You can type your question below or use your voice. Type 'exit' to end the conversation.")

    # Speech Recognition
    recognizer = sr.Recognizer()

    # Button to activate speech input
    if st.button("Use Voice Input"):
        st.write("Listening...")
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=5)
                user_input = recognizer.recognize_google(audio)
                st.write(f"You (voice): {user_input}")
            except sr.UnknownValueError:
                st.write("Chatbot: I couldn't understand your voice input. Please try again.")
                user_input = ""
            except sr.RequestError as e:
                st.write(f"Chatbot: Speech recognition error: {e}")
                user_input = ""
            except sr.WaitTimeoutError:
                st.write("Chatbot: Listening timed out. Please try again.")
                user_input = ""
    else:
        user_input = st.text_input("You (text): ")

    if user_input.lower() == 'exit':
        st.write("Chatbot: Goodbye!!")
        st.stop()
    elif user_input.strip():
        response = chatbot.respond(user_input)
        if response:
            st.write(f"Chatbot: {response}")
        else:
            st.write("Chatbot: I could not understand your statement. Kindly rephrase your statement.")

if __name__ == "__main__":
    main()


