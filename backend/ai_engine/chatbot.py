from transformers import pipeline

qa = pipeline("question-answering")

def answer_question(question, context):

    result = qa(question=question, context=context)

    return result["answer"]