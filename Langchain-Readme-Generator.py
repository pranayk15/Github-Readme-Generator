from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import streamlit as st

st.title("📘 GitHub README Generator")

# col1,col2=st.columns(2)

# with col1:
project_name=st.text_input("🏷️ Project Name")

# with col2:
project_type = st.selectbox(
        "🧩 Project Type",
        [
            "🌍 Web Application",
            "📱 Mobile Application",
            "💻 Desktop Application",
            "⚙️ Command Line Tool (CLI)",
            "🔗 API / Microservice",
            "🧠 Machine Learning Model",
            "🧬 Deep Learning Model",
            "👁️ Computer Vision App",
            "💬 NLP App",
            "🪄 Generative AI / LLM Project",
            "🤖 Chatbot",
            "🎯 Recommendation System",
            "📊 Data Analytics Dashboard",
            "📈 Visualization Tool",
            "☁️ Cloud Project",
            "🧰 DevOps / CI-CD Pipeline",
            "💼 Portfolio Website",
            "🎮 Game Development",
            "📖 Educational Tool",
            "🪄 Productivity Tool",
            "🔬 Research / Experimentation Project",
            "❓ Other"
        ],
    )

# col3,col4=st.columns(2)
# col5,col6=st.columns(2)

# with col3:
tech_stack=st.text_area("🧰 Tech Stack")

# with col4:
description=st.text_area("📝 Project Description",
    height=250)

# with col5:
features=st.text_area("✨ Main Features (use bullet points)")

# with col6:
screenshot = st.file_uploader(
    "🖼️ Screenshots of your product (PNG, JPG, JPEG)",
    type=['png', 'jpg', 'jpeg'] ,# Restrict to common image file types
    key="screenshots"
)

if screenshot is not None:
    st.success("File uploaded successfully")
    # st.image(uploaded_file, caption=uploaded_file.name)

else:
    pass

license=st.selectbox("📜 License",["MIT", "Apache 2.0", "GPL 3.0", "BSD 3-Clause", "Other"])

template=PromptTemplate(
    template="""
    You are an expert technical writer skilled at creating professional, attractive, and well-structured GitHub README files for software projects.

Your task is to generate a complete README.md file for a project based on the information provided below.

---
### 📝 Project Information:
- **Project Name:** {project_name}
- **Project Type:** {project_type} (e.g., Web App, AI Model, API, Mobile App, etc.)
- **Tech Stack:** {tech_stack} (e.g., Python, TensorFlow, React, FastAPI, etc.)
- **Description:** {project_description}
- **Main Features:** {features} (list main functionalities)
- **Screenshots or Demos (optional):** {screenshots}
- **License:** {license}
---

### 🎯 Output Requirements:
- Generate a **Markdown-formatted README.md** file.
- Use **section headings**, **emojis**, and **code blocks** where needed.
- Include the following standard sections (if data is missing, write “To be added”):
  1. Project Title
  2. Description
  3. Features
  4. Tech Stack
  5. Screenshots or Demo (placeholder if not available)
  6. License
- Make the README **clear, visually appealing, and ready to publish on GitHub.**

---
### Example Style Reference:
Use a style similar to professional open-source projects like:
- TensorFlow
- LangChain
- React
(Concise, formatted, with emoji sections)

Now generate the complete README.md for the project described above.
""",
input_variables=["project_name","project_type","tech_stack","project_description","features","screenshots","license"]
)

prompt=template.invoke({
    "project_name":project_name,
    "project_type":project_type,
    "tech_stack":tech_stack,
    "project_description":description,
    "features":features,
    "screenshots":screenshot,
    "license":license
})

api_key="AIzaSyB5I_QHm08l-LrrCR6pQhputZr6GzwT9nw"

model=ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=api_key
)

if st.button("Generate File"):
    result=model.invoke(prompt)
    st.write(result.content)