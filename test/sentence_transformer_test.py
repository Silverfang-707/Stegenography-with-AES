from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Example sentences to encode
sentences = [
    "This framework generates embeddings for each input sentence.",
    "Sentences are passed as a list of strings.",
    "The quick brown fox jumps over the lazy dog."
]

# Encode the sentences
embeddings = model.encode(sentences)

# Print the embeddings
for sentence, embedding in zip(sentences, embeddings):
    print("Sentence:", sentence)
    print("Embedding:", embedding)
    print()
