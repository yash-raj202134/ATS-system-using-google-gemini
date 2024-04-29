# ATS System using Google Gemini

## Overview

The ATS system is designed to help job seekers craft and optimize their resumes for Applicant Tracking Systems (ATS). Leveraging the power of Google Gemini, the system processes job descriptions and resumes to provide valuable insights and recommendations for optimizing resumes for ATS compatibility.

## Features

- **Job Description Input**: Allows users to input a job description they are targeting.
- **Resume Upload**: Users can upload their resume in PDF format.
- **PDF to Image Conversion**: Converts the uploaded PDF to an image format.
- **Image Processing**: Uses an API to process the image and extract information.
- **Google Gemini Integration**: Connects with Google Gemini Pro for advanced text analysis and recommendations.
- **Prompts Template**: Utilizes multiple prompts for fine-tuned analysis and optimization.
- **PDF to Text Conversion**: Converts PDF resumes to text format for additional processing and analysis.
- **Recommendations and Insights**: Provides tailored recommendations for optimizing resumes based on job descriptions.

## Prerequisites

- **Python 3.x**: Ensure Python is installed and up to date.
- **API Access**: API credentials for the Google Gemini Pro and other relevant services.
- **Libraries**: Make sure you have the necessary Python libraries installed.

## Required Libraries

- `pdf2image`
- `Pypdf2`
- `NumPy`
- `Matplotlib`
- `pandas`
- `requests`

## Installation

1. **Clone the repository**:

    ```bash
    git clone <repository-url>
    ```

2. **Navigate to the project directory**:

    ```bash
    cd ats-system
    ```

3. **Install required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API credentials**: Obtain necessary API credentials for Google Gemini Pro and any other services, and store them securely.

## Usage

1. **Provide Job Description**: Input the job description you are targeting.
2. **Upload Resume**: Upload your resume in PDF format.
3. **Run the ATS System**: The system will process the PDF resume, convert it to image format, and extract relevant information using the API and Google Gemini Pro.
4. **Review Recommendations**: The system will provide tailored recommendations and insights based on the job description.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests for any features, improvements, or bug fixes.

## License

This project is licensed under the Apache-2.0 License.

## Acknowledgements

- [Google Gemini Pro](https://cloud.google.com/) for providing the advanced AI and text analysis capabilities.
- The open-source community for various Python libraries used in this project.

## Contact

For any inquiries or support, please [contact us](mailto:example@example.com).
