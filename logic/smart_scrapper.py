import requests
from bs4 import BeautifulSoup
from openai import OpenAI


def scrape_all_depths(tag, depth=0, content_set=None, content_list=None):
    """
    Recursively traverse through all the tags, extract their content,
    and skip JavaScript, images, or empty/duplicate content.
    """

    # Keeps track of unique content
    if content_set is None:
        content_set = set()

    # Collects unique content in order
    if content_list is None:
        content_list = []

    # Skip non-tag elements, JavaScript, CSS, and images
    if tag.name in ["script", "img", "style"] or not hasattr(tag, "children"):
        return content_set, content_list

    # Process the tag's text content
    if tag.string:
        text = tag.string.strip()
        if text and text not in content_set:
            content_set.add(text)
            content_list.append(text)

    # Recursively visit each child tag
    for child in tag.children:
        scrape_all_depths(child, depth + 1, content_set, content_list)

    return content_set, content_list


def scrape_homepage(url: str):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()

        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")

        # Start the recursive scraping from the root
        _, unique_content = scrape_all_depths(soup)

        # Join the unique content into a single string
        combined_content = "\n".join(unique_content)
        return combined_content, 200

    except requests.exceptions.RequestException as e:
        return e.response.content, e.response.status_code


def smart_openai_analyzer(content: str, api_key: str, model: str, structured_output):

    try:
        client = OpenAI(api_key=api_key)

        prompt = """
            Using the homepage content, your task is to find below details:
            Industry: What industry does the website belong to?

            Company Size: What is the size of the company (e.g., small, medium, large) if mentioned?. 
            If not mentioned then you can get the idea by
            1. their current employee strengh 
            2. by number of customers 
            3. by number of higher authority person. 
            4. by awards win during lifetime.
            default is small.

            Location: Where is the company located (if mentioned), try to fetch the whole address with pincode?
        """

        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {
                    "role": "user",
                    "content": content,
                },
            ],
            response_format=structured_output,
        )

        event = completion.choices[0].message.parsed
        return event, 200
    except Exception as e:
        return str(e), 400
