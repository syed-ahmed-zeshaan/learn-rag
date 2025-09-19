def generate_prompt(context_data, user_query):
    context = ('\n').join(context_data)
    return f'''
        You are an expert assistant. Answer the question below **naturally and helpfully**, using the information provided in the context.
        Try to explain it as if you already know it, without explicitly saying "based on the context".

        Context:
        {context}

        Question:
        {user_query}

        Answer:
    '''
