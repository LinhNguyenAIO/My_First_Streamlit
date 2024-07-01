# My First Streamlit Project

## Introduction

Welcome to My First Streamlit! 
This Streamlit is deploying interactive web applications which included in this project are:

1. **Word Correction**: A spelling correction tool that utilizes the Levenshtein distance algorithm to find and correct misspelled words by suggesting the closest match from a pre-defined dictionary.
2. **Object Detection**: An application that uses a Deep Neural Network (DNN) model from the OpenCV library to detect and highlight objects in images.
3. **Simple Chatbot**: A simple chatbot using HugChat library, designed to provide interactive conversations and assist users with various queries.

## How to Intall
1. **Clone the repository:**
   ```sh
    git clone https://github.com/LinhNguyenAIO/My_First_Streamlit
    cd My_First_Streamlit
    ```
2. **(Optional) Create and activate a virtual environment**:
   
   For macOS and Linux:
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

    For Windows:
    ```sh
    python -m venv .venv
    .venv\Scripts\activate
    ```
3. **Intall the required dependencies:**
   ```sh
    pip install -r requirements.txt
    ```
## Running the Application

You can launch the application by running one of the following commands based on the application:

1. **Correct Word**:
    ```sh
    streamlit run levelshtein_distance.py
    ```

2. **Object Detection**:
    ```sh
    streamlit run object-detection.py
    ```

3. **Simple Chatbot**:
    ```sh
    streamlit run chatbot.py
    ```