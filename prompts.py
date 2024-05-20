class PromptCls:
    def __init__(self):
        pass

    @staticmethod
    def StockPromptStyleVanilla(textLine):
        
        temp_var = f"""
        Consider the following points while answering for message. 
        
        Following points:
        1. If you don't know the answer just say that you don't know. don't try to make up an response.
        
        message: ```{textLine}``` """
        
        return temp_var
