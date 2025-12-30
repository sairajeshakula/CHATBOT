from langgraph.graph import StateGraph,START,END
from langchain_groq import ChatGroq
from langgraph.graph.message import add_messages,MessagesState
from typing import Annotated,Literal,TypedDict
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage,BaseMessage
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.prebuilt import ToolNode
from dotenv import load_dotenv

load_dotenv()

llm=ChatGroq(model_name="Gemma2-9b-It")

class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage],add_messages]


def chat_model(state:ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {'messages':[response]}

checkpointer=InMemorySaver()
graph=StateGraph(ChatState)

graph.add_node('chat_model',chat_model)
graph.add_edge(START,'chat_model')
graph.add_edge('chat_model',END)

chatbot=graph.compile(checkpointer=checkpointer)