import os

files = [
    "Prompt and LLM",
    "RAG",
    "Quering an SQL DB",
    "Agents",
    "With multiple chains",
    "Routing by Semantic Similarity",
    "Adding memory",
    "Adding moderation",
    "Managing prompt size",
    "using langchain tools",
    "code writing",
]

for file in files:
    file_name = os.path.join(os.getcwd(), "-".join(file.split()) + ".ipynb")
    with open(file_name, "w") as f:
        print(f"created {file_name}")