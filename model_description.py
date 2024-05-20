import anthropic
import yfinance as yf
import streamlit as st
from anthropic_api_key import Anthropic_Api_Key

client = anthropic.Anthropic(api_key = str(Anthropic_Api_Key()))

# 1. Get Stock Price function / Tool
def get_stock_price(ticker_symbol):
    stock = yf.Ticker(ticker_symbol)
    hist = stock.history(period="1d")
    current_price = hist['Close'].iloc[0]
    return str(current_price)

# 2. Tool Definition
tools = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price for a given ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker_symbol": {
                    "type": "string",
                    "description": "The stock ticker symbol, e.g., AAPL for Apple Inc."
                }
            },
            "required": ["ticker_symbol"]
        }
    }
]

def process_tool_call(tool_name, tool_input):
    if tool_name == "get_stock_price":
        return get_stock_price(tool_input["ticker_symbol"])


def run_tool_interaction(user_message, model="claude-3-sonnet-20240229"):
    initial_response = client.beta.tools.messages.create(
        model=model,
        max_tokens=1024,
        tools=tools,
        messages=[{"role": "user", "content": user_message}]
    )

    # print(f"Stop Reason: {initial_response.stop_reason}")
    # print(f"Initial Response: {initial_response.content}")

    # Process tool call if indicated by stop reason
    if initial_response.stop_reason == "tool_use":
        tool_use = next(block for block in initial_response.content if block.type == "tool_use")
        tool_name = tool_use.name
        tool_input = tool_use.input

        # print(f"\nTool Used: {tool_name}")  # Example: get_stock_price
        # print(f"Tool Input: {tool_input}")  # Example: {'ticker_symbol': 'AAPL'}

        tool_result = process_tool_call(tool_name, tool_input)
        # print(f"Tool Result: {tool_result}")

        # Send the tool result back to the assistant
        response = client.beta.tools.messages.create(
            model=model,
            max_tokens=4096,
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": initial_response.content},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": tool_use.id,
                            "content": tool_result,
                        }
                    ],
                },
            ],
            tools = tools,
        )
    else:
        response = initial_response

    # Extract and return the final response
    final_response = next(
        (block.text for block in response.content if hasattr(block, "text")),
        None,
    )
    return final_response

# input_query = st.text_input("Enter query here", placeholder = "Ask me")
# if input_query:
    
#     resopnse = run_tool_interaction(input_query)
#     st.write("Response/n/n")
#     st.markdown(resopnse)