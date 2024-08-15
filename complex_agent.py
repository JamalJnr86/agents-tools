#complex_agent.py
from langchain_groq import ChatGroq                     #type: ignore
from langchain import LLMChain, PromptTemplate          #type: ignore
from weather_tool import get_weather
from currency_tool import convert_currency
from sentiment_tool import analyze_sentiment
from search_tool import search_web
from stock_exchange import get_stock_exchange_rate 

# Initialize the Groq client
groq_api_key = "add_your_api" 
client = ChatGroq(api_key=groq_api_key, model_name="Add_your_model_name")

# Define a prompt template for generating responses
prompt_template = PromptTemplate(
    input_variables=["user_input", "result"],
    template="User query: {user_input}\nResult: {result}\nProvide a comprehensive response based on the above information."
)

# Define the LLMChain with the Groq model and prompt template
chain = LLMChain(
    llm=client,
    prompt=prompt_template
)

class ComplexAgent:
    def __init__(self):
        self.chain = chain

    def process_input(self, user_input):
        try:
            if user_input.startswith("weather"):
                city = user_input.split(" ", 1)[1]
                result = get_weather(city)
            elif user_input.startswith("convert"):
                _, amount, from_currency, to_currency = user_input.split()
                try:
                    amount = float(amount)
                    result = convert_currency(amount, from_currency.upper(), to_currency.upper())
                except ValueError:
                    result = "Please provide a valid amount."
            elif user_input.startswith("sentiment"):
                text = user_input.split(" ", 1)[1]
                result = analyze_sentiment(text)
            elif user_input.startswith("search"):
                query = user_input.split(" ", 1)[1]
                search_results = search_web(query)
                if search_results:
                    formatted_results = "\n".join(f"{i + 1}. {item['title']}: {item['link']}" for i, item in enumerate(search_results))
                    result = formatted_results
                else:
                    result = "No results found."
            elif user_input.startswith("stock"):
                stock_symbol = user_input.split(" ", 1)[1]
                stock_rate = get_stock_exchange_rate(stock_symbol)
                formatted_result = f"{stock_symbol}: {stock_rate.get(stock_symbol, 'Data not found.')}"
                result = formatted_result

            else:
                result = "Please enter a valid command (e.g., 'weather <city>', 'convert <amount> <from_currency> <to_currency>', 'sentiment <text>', 'search <query>', or 'stock <symbol>')."

            # Generate AI response based on user input and tool result
            ai_response = self.chain.run({"user_input": user_input, "result": result})
        except Exception as e:
            ai_response = f"An error occurred: {str(e)}"
        
        return ai_response
