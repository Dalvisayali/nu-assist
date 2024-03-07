# NU Assist: Social Justice Platform for Northeastern University Students 🎓

[![FastAPI](https://img.shields.io/badge/FastAPI-Modern-green)](https://fastapi.tiangolo.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Powerful-blue)](https://beta.openai.com/docs/)
[![Streamlit](https://img.shields.io/badge/Streamlit-User%20Friendly-orange)](https://docs.streamlit.io/)

NU Assist is a cutting-edge social justice platform designed exclusively for Northeastern University students. This application aims to empower students by providing comprehensive information about social justice services, clubs, and organizations available on campus. Additionally, NU Assist includes a robust feature for reporting social injustice incidents, allowing students to submit anonymous reports with relevant details. The reported incidents are then forwarded to the appropriate campus committees for necessary actions.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Data Collection](#data-collection)
- [Pipeline Overview](#pipeline-overview)
- [User Interface](#user-interface)
- [File Structure](#file-structure)
- [References](#references)

## Features
1. **Chat Bot:** The application boasts an intelligent chat bot that serves as a one-stop solution for accessing information about social justice services, clubs, and organizations on campus.
2. **Anonymous Reporting:** Students can anonymously report incidents of social injustice through the application, providing crucial information to facilitate prompt and appropriate actions.

## Technologies Used
- **FastAPI:** The backend of NU Assist is built using FastAPI, a modern, fast, and web framework for building APIs with Python 3.7+. 🚀
- **OpenAI:** The chat bot leverages OpenAI's powerful language models to generate responses based on the information collected. 🤖
- **Streamlit:** The user interface is developed using Streamlit, a Python library for creating web applications with minimal effort. 🌐

## Data Collection
The application collects relevant data by scraping information from the official websites of various university organizations. This ensures that the information provided is up-to-date and accurate.

## Pipeline Overview
1. **Data Collection:** Relevant data is collected by scraping information from university organization websites.
2. **Embedding Generation:** The collected data is processed to generate embeddings using advanced techniques.
3. **Cosine Similarity Index:** A cosine similarity index is applied to find the embeddings closest to the user's question.
4. **OpenAI Integration:** The relevant embeddings are passed to the OpenAI API to generate accurate and contextually appropriate responses.

## User Interface
The user interface is designed with Streamlit to offer a seamless and intuitive experience for students. The application's chat bot is integrated into the UI, allowing users to easily interact with the platform.

## File Structure



## References
- FastAPI Documentation: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- OpenAI API Documentation: [OpenAI API Documentation](https://beta.openai.com/docs/)
- Streamlit Documentation: [Streamlit Documentation](https://docs.streamlit.io/)

