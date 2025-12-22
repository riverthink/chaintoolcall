import chainlit as cl
from langchain.tools import tool
from langchain_openai import ChatOpenAI

@tool
def generate_patient():
    """Generate a patient record for a hospital systems demonstration."""
    return {
        "name": "John Smith",
        "age": 67,
        "condition": "Hypertension",
        "ward": "Cardiology",
    }

@cl.on_chat_start
async def on_chat_start():
    llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

    system_instruction = (
        "You are a hospital assistant. "
        "When asked about patient information, use the 'generate_patient' tool to retrieve patient records. "
    )
    llm_with_tools = llm.bind_tools([generate_patient]).with_config({
        "system_message": system_instruction
    })

    cl.user_session.set("llm", llm_with_tools)

@cl.on_message
async def on_message(message: cl.Message):
    llm = cl.user_session.get("llm")

    response = await llm.ainvoke(message.content)
    print("Response from LLM:", response) # Show the different responses from the LLM

    # Case 1: model produced text
    if response.content:
        await cl.Message(content="From Model:"+response.content).send()
        return

    # Case 2: model decided a tool is needed
    if response.tool_calls:
        tool_output = generate_patient.invoke({})
        await cl.Message(content="From Tool:"+str(tool_output)).send()
        return

    await cl.Message(content="No response.").send()


