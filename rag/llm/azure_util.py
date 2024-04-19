from langchain_openai import AzureChatOpenAI
import os


def create_azure_llm():
    os.environ["OPENAI_API_VERSION"] = "2024-02-15-preview"
    os.environ["AZURE_OPENAI_ENDPOINT"] = "https://yp2401.openai.azure.com"
    os.environ["AZURE_OPENAI_API_KEY"] = "2fcbec6687ec42b481bede40fbfcca15"

    llm = AzureChatOpenAI(
        deployment_name="YPgpt"
    )
    return llm
