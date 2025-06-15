from dotenv import load_dotenv

from langchain_groq import ChatGroq

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough, RunnableParallel

from langchain_community.graphs import Neo4jGraph
from langchain_community.vectorstores import Neo4jVector

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from graph_entity import Entities
from utils import generate_full_text_query
from templates import entity_template, query_template
load_dotenv()



graph = Neo4jGraph()
llm = ChatGroq(temperature=0, model_name="llama3-8b-8192")

embedding_model = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001", task_type="retrieval_query"
)

vector_index = Neo4jVector.from_existing_graph(
    embedding_model,
    search_type="hybrid",
    node_label="Document",
    text_node_properties=["text"],
    embedding_node_property="embedding"
)






entity_chain = entity_template | llm.with_structured_output(Entities)

graph.query("CREATE FULLTEXT INDEX entity IF NOT EXISTS FOR (e:__Entity__) ON EACH [e.id]")

def structured_retriever(question: str) -> str:
    """
    Collects the neighborhood of entities mentioned
    in the question
    """
    result = ""
    entities = entity_chain.invoke({"question": question})
    for entity in entities.names:
        response = graph.query(
            """
                CALL db.index.fulltext.queryNodes('entity', $query, {limit:2})
                YIELD node, score
                CALL {
                    MATCH (node)-[r:!MENTIONS]->(neighbor)
                    RETURN node.id + ' - ' + type(r) + ' -> ' + neighbor.id AS output

                    UNION

                    MATCH (node)<-[r:!MENTIONS]-(neighbor)
                    RETURN neighbor.id + ' - ' + type(r) + ' -> ' +  node.id AS output
                }
                RETURN output LIMIT 15
            """,
            {"query": generate_full_text_query(entity)},
        )
        result += "\n".join([el['output'] for el in response])
    return result

def retriever(question: str):
    structured_data = structured_retriever(question)
    unstructured_data = [el.page_content for el in vector_index.similarity_search(question, k=15)]
    final_data = f"""
        Structured data:
        {structured_data}
        Unstructured data:
        {"#Document ". join(unstructured_data)}
    """
    return final_data


query_prompt = ChatPromptTemplate.from_template(query_template)

query_chain = (
    RunnableParallel(
        {
            "context": retriever,
            "question": RunnablePassthrough(),
        }
    )
    | query_prompt
    | llm
    | StrOutputParser()
)


async def execute(user_query: str):
    return query_chain.invoke(user_query)