# Question Classifier 🚀  

A plug-and-play Python project that classifies questions into **factual**, **opinion**, or **math**.  
Supports **CLI**, **REST API**, **Docker**, and comes with **CI/CD** for automated builds and publishing.  

---

## ✨ Features  
- **CLI Mode:** Run directly from terminal  
- **API Mode:** REST API using FastAPI  
- **Dockerized:** Run anywhere with a single command  
- **CI/CD Ready:** Auto Docker builds via GitHub Actions  
- **Open Source:** Anyone can clone, run, or extend  

---

## ⚡ Quick Start  

### 🔹 Run with Docker (Recommended)  
```bash
docker pull aryangupta5084/question-classifier:latest
docker run -d -p 8000:8000 aryangupta5084/question-classifier
```
Open 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

### 🔹 Run Locally (CLI)  
```bash
# Clone repo
git clone https://github.com/AryanGupta5084/question-classifier.git
cd question-classifier

# Install dependencies
pip install -r requirements.txt

# Run app
python main.py
```

---

### 🔹 Run Locally (API)  
```bash
uvicorn main:app --reload
```
Open 👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  

---

## 🔥 Example API Usage  
```bash
curl -X POST "http://127.0.0.1:8000/classify" \     -H "Content-Type: application/json" \     -d '{"text": "2 + 3 * 5"}'
```
**Response:**  
```json
{
  "question": "2 + 3 * 5",
  "response": "This looks like a math question. Answer: 17"
}
```

---

## 🤖 CI/CD (GitHub Actions)  
This repo is CI/CD enabled 🚀  
- On push to `main`, Docker image is built & pushed to Docker Hub  
- Anyone can pull the latest image:  
```bash
docker pull aryangupta5084/question-classifier:latest
```

---

## 🚀 Future Improvements  
- LLM-powered classification (OpenAI / Hugging Face)  
- Wikipedia API for factual answers  
- SymPy for advanced math solving  
- Cloud deployment templates (AWS/GCP/Azure)  

---

