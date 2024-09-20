Social Media Post Generator
A Flask-based web application that uses OpenAI's API to generate professional social media posts based on user-provided inputs such as company details, achievements, and testimonials. This project leverages the GPT model to create compelling transformation stories with relevant data, bullet points, and a call-to-action.

Features
Generates a social media post in a professional tone.
Collects input from users, such as company name, partner, region, and achievements.
Automatically crafts a structured social media post with an introduction, key results, impact data, and a call-to-action.
Easy-to-use web interface powered by Flask.
Outputs copy suitable for platforms like LinkedIn or Twitter.
Prerequisites
Before running this project, you will need the following:

Python 3.8+
An OpenAI API Key.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/M-A-K-K/Social-Media-post-generator-.git
cd Social-Media-post-generator-
Set up a virtual environment (optional but recommended):

bash
Copy code
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables: Create a .env file in the project root and add your OpenAI API key:

bash
Copy code
OPENAI_API_KEY=your_openai_api_key_here
Usage
Run the Flask application:

bash
Copy code
python app.py
Open the application in your web browser: Go to http://127.0.0.1:5000/ and you will see the form where you can input your data.

Generate a social media post: Fill out the form with the following fields:

Company Name
Partner Name
Region
Key Achievements (up to 5)
Testimonial
Call-to-action Link
View the generated post: After submitting the form, a custom-crafted social media post will appear based on the information provided.

Project Structure
bash
Copy code
Social-Media-post-generator-
│
├── templates
│   └── index.html         # HTML template for the web interface
├── app.py                 # Main Flask application
├── .env                   # Environment variables (ignored by Git)
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
Example
If you input the following data:

Company Name: ABC Corp
Partner: XYZ Solutions
Region: North America
Achievements: Improved efficiency by 30%, Increased revenue by 15%, Reduced costs by 10%, Expanded workforce training, Enhanced employee satisfaction
Testimonial: John Doe
Link: https://example.com
