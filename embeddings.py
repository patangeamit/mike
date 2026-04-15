from sentence_transformers import SentenceTransformer

# cosine similarity (rough idea)
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
print("Model loaded, generating embeddings...")
# embedding = model.encode("install docker on linux")
# print(embedding)

# e1 = model.encode("I am trying to set up Docker on a fresh Linux machine and would like a detailed, step-by-step explanation of the installation process. Please include all necessary prerequisites, commands to run in the terminal, and any common issues that might occur during installation along with how to resolve them. Assume I am relatively new to Docker but comfortable using the command line.")
# e2 = model.encode("Can you walk me through how to install Docker on a Linux system from scratch? I need clear instructions including required dependencies, setup steps, and troubleshooting tips in case something goes wrong during the installation process.")
# e3 = model.encode("Explain how container orchestration works in Kubernetes, including concepts like pods, deployments, services, and scaling strategies in a production environment.")
# e4 = model.encode("how to cook pasta")
texts = [
    "I am trying to set up Docker on a fresh Linux machine...",
    "Can you walk me through how to install Docker on a Linux system...",
    "Explain how container orchestration works in Kubernetes...",
    "how to cook pasta"
]

embeddings = model.encode(texts)

e1, e2, e3, e4 = embeddings
def sim(a,b):
    return np.dot(a,b) / (np.linalg.norm(a)*np.linalg.norm(b))

print(sim(e1,e2))  # should be HIGH
print(sim(e1,e3))  # should be LOW
print(sim(e1,e4))  # should be LOW
