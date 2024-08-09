# Gemini Invoice Extractor

## Overview
The Gemini Invoice Extractor is a web application built with Streamlit that leverages Google Gemini 1.5 Flash for invoice processing. The application allows users to upload an invoice image or PDF and extract key details such as customer information, products, and total amount.

## Features
- Upload invoice images or PDFs
- Convert PDFs to images
- Extract invoice details using Gemini 1.5 Flash
- Display extracted information in the app

## Setup

### Prerequisites
Ensure you have Python 3.7 or higher installed on your system.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory with your Google API key:
   ```env
   GOOGLE_API_KEY=your_google_api_key
   ```

### Running the App
Run the Streamlit app using the following command:
```bash
streamlit run app.py
```

### Usage
1. Open the app in your web browser.
2. Upload an invoice image or PDF.
3. Click the "Submit" button to extract and view the invoice details.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
```

Replace `<repository_url>` and `<repository_directory>` with the actual URL and directory name of your repository if applicable. 

Let me know if you need any more details or adjustments!