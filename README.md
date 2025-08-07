
# 🧠 streamlit-local-llm

A minimal web-based UI built with [Streamlit](https://streamlit.io/) to run **local LLMs** using [llama.cpp](https://github.com/ggerganov/llama.cpp).  
Supports chat history, multiple models, and runs entirely offline with quantized GGUF models.

---

## 🚀 Features

- ✅ Local inference using `llama.cpp` backend
- ✅ Clean Streamlit UI with persistent chat history
- ✅ Works with any GGUF model (e.g. Q4_K_M, Q6_K)
- ✅ Sidebar with model selector and past threads
- ✅ No internet or OpenAI key required
- ✅ LAN access for other devices (e.g. Vision Pro)

---

## 📦 Requirements

- Python 3.10+
- `llama-cpp-python` compiled with:
  - `metal` for Apple Silicon (M1/M2/M3)
  - `cuda` / `rocm` for NVIDIA / AMD
- GGUF-format quantized model (see [Hugging Face](https://huggingface.co/collections/ggml/gguf-models-656464cd5f7413fbb7b5fcb3))

### Install dependencies

```bash
pip install -r requirements.txt––
