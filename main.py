import re
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Question Classifier API")

class Question(BaseModel):
    text: str

def classify_question(question: str) -> str:
    q = question.lower().strip()
    
    # Math detection: check for numbers/operators
    if re.search(r'\d+|\+|\-|\*|\/|\=|\^', q):
        return "math"
    
    # Opinion detection: look for subjective keywords
    opinion_keywords = ["think", "feel", "opinion", "believe", "should", "better", "best"]
    if any(word in q for word in opinion_keywords):
        return "opinion"
    
    # Default: factual
    return "factual"


def generate_response(question: str) -> str:
    qtype = classify_question(question)
    
    if qtype == "math":
        try:
            # Evaluate math expression safely
            result = eval(question, {"__builtins__": None}, {})
            return f"This looks like a math question. Answer: {result}"
        except Exception:
            return "This looks like a math question, but I couldn't solve it."
    
    elif qtype == "opinion":
        return "That sounds like an opinion-based question. I think it depends on personal perspective."
    
    else:  # factual
        return "That looks like a factual question. You might need a reliable source or database to answer it."


@app.post("/classify")
def classify_api(q: Question):
    response = generate_response(q.text)
    return {"question": q.text, "response": response}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
