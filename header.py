from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()
prompt = PromptTemplate(
    template="generate a 2 to 3 word title from given question and give me the best one only. Don't try to explain the question,just generate title only\n {question}",
    input_variables=['question']
)
prompt2=PromptTemplate(
    template="enhance the generated title  based question \n {question},{title}",
    input_variables=['question','title']
)
parser=StrOutputParser()
llm=ChatGroq(model_name="Gemma2-9b-It")

question=''
app=prompt | llm | parser 

res=app.invoke(question)
print(res)

