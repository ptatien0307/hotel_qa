from langchain_core.prompts import ChatPromptTemplate

entity_template = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are extracting all entities from the text.",
        ),
        (
            "human",
            "Use the given format to extract information from the following"
            "input: {question}",
        ),
    ]
)

query_template = """
    Answer the question based only on the following context:
    {context}

    Question: {question}

    Use natural language and be concise.
    
    Answer:
"""