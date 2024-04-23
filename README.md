### RAG System for Contextual Question Answering

This repository contains code for building a Retrieval-Augmented Generation (RAG) system using the LangChain framework. The RAG system leverages the power of Language Models (LMs) like Gemini 1.5 Pro to answer questions based on external data, specifically the "Leave No Context Behind" paper published by Google on 10th April 2024.

### Files Included:

1. **app.py**: This file contains the main script for running the RAG system. It handles the retrieval of external data, interacts with the Gemini 1.5 Pro LM, and generates answers to questions.
   
2. **build_RAG.ipynb**: This Jupyter Notebook provides a step-by-step guide on building the RAG system using the LangChain framework. It includes code snippets, explanations, and examples to facilitate the setup and implementation process.
   
3. **template folder**: This folder contains template files used in the RAG system, such as HTML templates for the user interface.

4. **data file**: This file contains the "Leave No Context Behind" paper in PDF or text format, which serves as the external data for contextual question answering.

5. **requirements.txt**: This file lists all the Python dependencies required for running the RAG system. Install these dependencies using `pip install -r requirements.txt`.

### Usage:

1. Clone the repository to your local machine.
   
2. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
   
3. Place the "Leave No Context Behind" paper in the designated data folder.

4. Open the `build_RAG.ipynb` notebook and follow the instructions to build the RAG system using the LangChain framework.

5. Run the `app.py` script to start the RAG system.

6. Access the RAG system through the provided user interface or API endpoints to ask questions related to the "Leave No Context Behind" paper.

### Contributions:

Contributions to the repository are welcome! If you have any suggestions, bug fixes, or improvements, feel free to open an issue or submit a pull request.


### Acknowledgments:

Special thanks to the LangChain team for developing the framework and providing guidance on building the RAG system.
