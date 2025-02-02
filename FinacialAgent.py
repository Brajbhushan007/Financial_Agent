
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

import os

web_agent = Agent( 
    name="Web Agent",
    model=Groq(id="Llama-3.3-70b-Versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)

Financial_agent = Agent(
    name="Financial Agent", 
    model=Groq(id="Llama-3.3-70b-Versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, historical_prices=True,technical_indicators=True, income_statements=True)],
    show_tool_calls=True,
    markdown=True,
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."]
)

agent_team = Agent(
    name="Team Agent",
    model=Groq(id="Llama-3.3-70b-Versatile"),
    team=[web_agent, Financial_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

agent_team.print_response("What are the top 5 stocks in India?", stream=True)

