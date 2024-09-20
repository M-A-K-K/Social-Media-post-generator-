import os
import openai
from flask import Flask, render_template, request, abort
from dotenv import load_dotenv
import openai

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

def generate_social_media_post(answers):
    prompt = f"""
    Create a professional social media post highlighting a successful transformation story. Use the following information to craft the post:

    1. **Introduction**: Start with an engaging statistic or fact related to the challenge or outcome.
    2. **Case Study Overview**: Describe the collaboration and its purpose.
    3. **Key Results**: Present the achievements in bullet points.
    4. **Impact Data**: Include relevant statistics or quotes to underscore the impact.
    5. **Call-to-Action**: Invite the audience to join the journey or explore more.
    6. **Hashtag and Link**: Include a specific hashtag and a call-to-action link.

    Here is the information to include:
    - **Case Study**: A successful collaboration between {answers['company_name']} and {answers['partner']} to enhance leadership development across {answers['region']}.
    - **Challenge**: Addressed the need for scalable leadership development programs to engage and develop employees across diverse regions, especially in {answers['region']}.
    - **Key Results**:
      - {answers['achievement_1']}
      - {answers['achievement_2']}
      - {answers['achievement_3']}
      - {answers['achievement_4']}
      - {answers['achievement_5']}
    - **Impact Data**: 75% of classroom-style training is forgotten if it's not implemented within 6 days after.
    - **Call-to-Action**: Join thousands of coachees like {answers['testimonial']} on a journey of growth and transformation to #ExploreTheGreaterYou.
    - **Hashtag**: #ExploreTheGreaterYou
    - **Link**: {answers['link']}

    Ensure the post is professional and uses bullet points for the key achievements. End with a compelling call-to-action that encourages exploration and engagement.
    """

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  
            messages=[
                {"role": "system", "content": "You are a professional content writer."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=300,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        print(f"Error generating post: {e}")
        return "An error occurred while generating the post. Please try again later."

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            answers = {
                "company_name": request.form["company_name"],
                "industry": request.form["industry"],
                "partner": request.form["partner"],
                "region": request.form["region"],
                "achievement_1": request.form["achievement_1"],
                "achievement_2": request.form["achievement_2"],
                "achievement_3": request.form["achievement_3"],
                "achievement_4": request.form["achievement_4"],
                "achievement_5": request.form["achievement_5"],
                "testimonial": request.form["testimonial"],
                "link": request.form["link"],
            }

            post = generate_social_media_post(answers)

            return render_template("index.html", post=post)
        except KeyError as e:
            print(f"Missing form field: {e}")
            abort(400, description="One or more required fields are missing.")
    
    return render_template("index.html", post=None)

if __name__ == "__main__":
    app.run(debug=True)
