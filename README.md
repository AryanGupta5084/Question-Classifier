# Question Classifier (with API + Docker + CI/CD)

A Python project that classifies questions into **factual**, **opinion**, or **math**, with CLI, REST API, Docker, and CI/CD support.

## Features
- **CLI Mode:** Run interactively from terminal.
- **API Mode:** Expose endpoints using FastAPI.
- **Docker Support:** Deploy anywhere easily.
- **CI/CD:** Automated build & push using GitHub Actions.

## How to Run
```bash
# Clone this repo
git clone https://github.com/<your-username>/question-classifier.git
cd question-classifier

# Install requirements
pip install -r requirements.txt

# Run API
uvicorn main:app --reload
```

## Example Usage (API)
```bash
curl -X POST "http://127.0.0.1:8000/classify" \\
     -H "Content-Type: application/json" \\
     -d '{"text": "2 + 3 * 5"}'
```

**Response:**
```json
{
  "question": "2 + 3 * 5",
  "response": "This looks like a math question. Answer: 17"
}
```

## Run with Docker
```bash
# Build image
docker build -t question-classifier .

# Run container
docker run -d -p 8000:8000 question-classifier
```

## CI/CD (GitHub Actions)
This project includes a workflow to:
- Build Docker image
- Push to Docker Hub on new commits to `main`

To use:
1. Set Docker Hub credentials in repo **Settings → Secrets → Actions**:
   - `DOCKERHUB_USERNAME`
   - `DOCKERHUB_TOKEN`
2. On push to `main`, the image will be auto-built and pushed.

## Future Improvements
- Replace rule-based classification with **LLM API support** (OpenAI, Hugging Face).
- Integrate **Wikipedia API** for factual answers.
- Use **SymPy** for advanced math solving.
- Add **cloud deployment** (AWS/GCP/Azure).

## License
MIT License
