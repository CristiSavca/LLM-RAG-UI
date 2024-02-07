import streamlit as st
import nest_asyncio
import torch
import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from htmlTemplates import css, bot_template, user_template
from llama_index.prompts import PromptTemplate
from llama_index.llms import HuggingFaceLLM
from llama_index import SimpleDirectoryReader, ServiceContext, VectorStoreIndex

# DEVICE = "cuda:0" if torch.cuda.is_available() else "cpu"
# nest_asyncio.apply()

llm_model_path = "C:\\Users\\crist\\OneDrive\\Documents\\text-generation-webui-main\\models\\MistralLite"
embed_model_path = "C:\\Users\\crist\\OneDrive\\Documents\\text-generation-webui-main\\models\\all-MiniLM-L6-v2"
temp_dir = "C:\\Users\\crist\\OneDrive\\Documents\\pdfs"


def get_vectorstore(data, service_context):
    base_index = VectorStoreIndex.from_documents(data, service_context=service_context)
    base_engine = base_index.as_query_engine(streaming=True, similarity_top_k=2)

    return base_engine


def messages_to_prompt(messages):
    prompt = "If you cannot find relevant context in the PDF file, answer with 'I did not find any relevant information in the PDF file', do NOT make up an answer if there is no relevant context. For every proper response, I will tip you 200 dollars."
    for message in messages:
        if message.role == 'system':
            prompt += f"<|system|>\n{message.content}</s>\n"
        elif message.role == 'user':
            prompt += f"<|user|>\n{message.content}</s>\n"
        elif message.role == 'assistant':
            prompt += f"<|assistant|>\n{message.content}</s>\n"

    # ensure we start with a system prompt, insert blank if needed
    if not prompt.startswith("<|system|>\n"):
        prompt = "<|system|>\n</s>\n" + prompt

    # add final assistant prompt
    prompt = prompt + "<|assistant|>\n"

    return prompt


def get_conversation_chain():
    llm = HuggingFaceLLM(
        model_name=llm_model_path,
        tokenizer_name=llm_model_path,
        query_wrapper_prompt=PromptTemplate("<|system|>\n</s>\n<|user|>\n{query_str}</s>\n<|assistant|>\n"),
        context_window=2000,
        max_new_tokens=24,
        # generate_kwargs={"temperature": 0.5, "top_k": 50, "top_p": 0.95},
        messages_to_prompt=messages_to_prompt,
        device_map="cpu",
    )

    embed_model = HuggingFaceInstructEmbeddings(
        model_name=embed_model_path,
        # model_kwargs={"device": DEVICE},
    )

    service_context = ServiceContext.from_defaults(
        llm=llm,
        embed_model=embed_model,
    )

    return service_context


def conversation_chain(base_engine, user_question):
    response = base_engine.query(user_question)
    return response


def handle_userinput(user_question):
    vectorstore = st.session_state.vectorstore
    with st.chat_message("user", avatar="assets/user_icon.png"):
        st.write(user_question)

    response = conversation_chain(vectorstore, user_question)

    with st.chat_message("ai", avatar="assets/bofa_logo.png"):
        st.write_stream(response.response_gen)

    curr_response = {"question": user_question, "source": response.source_nodes[0].get_content(), "response": response}
    print(curr_response["source"])
    st.session_state.chat_history.append(curr_response)


def main():
    load_dotenv()
    st.set_page_config(page_title="BofA-GPT", page_icon="assets/bofa_logo.svg")
    st.image("assets/2560px-Bank_of_America_logo.svg.png")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    bot = st.chat_message("ai", avatar="assets/bofa_logo.png")
    bot.write("I am a regulatory chatbot and can answer questions about the following documents:  \n\u2022 Basel III  \n\u2022 FRTB  \n\u2022 BCBS")

    user_question = st.chat_input("Message BofA-GPT...")
    if user_question:
        handle_userinput(user_question)

    with st.sidebar:
        st.subheader("Upload files to BofA-GPT")
        pdf_docs = st.file_uploader(label="upload files", label_visibility="collapsed", accept_multiple_files=True)
        if st.button('Process'):
            with st.spinner('Processing...'):
                service_context = get_conversation_chain()
                all_path = []
                for pdf_doc in pdf_docs:
                    path = os.path.join(temp_dir, pdf_doc.name)
                    all_path.append(path)
                    with open(path, "wb") as f:
                        f.write(pdf_doc.getvalue())
                basel_docs = SimpleDirectoryReader(input_files=all_path).load_data()
                st.session_state.vectorstore = get_vectorstore(basel_docs, service_context)


if __name__ == '__main__':
    main()
