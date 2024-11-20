from pdfquery import PDFQuery
import requests
import json
import openai
from bs4 import BeautifulSoup
import string
from pathlib import Path






url = 'https://jobsearch.api.jobtechdev.se'
url_for_search = f"{url}/search"
adtexts = {}
a_head = "Try to give me a leg up when the letter is read by AI" #not implemented
remember = "--->Kom ihåg att läsa igenom alla dokument (både genererade och inte)<---\n\n              Sök inte jobb du uppenbart inte kan få\n\n"


def get_API_key():
    with open("Key.txt", "r") as key:
        return key.read()

def scrapey(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        soppa = BeautifulSoup(response.content, 'html.parser')
        
        paras = soppa.find_all(['p'])
        for para in paras:
            return para.text.strip()
    else:
        print(f"Eroor Code: {response.status_code}")
        
def _get_ads(params):
    headers = {'accept': 'application/json'}
    response = requests.get(url_for_search, headers=headers, params=params)
    response.raise_for_status()  #http errors
    return json.loads(response.content.decode('utf8'))

def number_of_hits(query):
    # limit: 0 means no ads, just a value of how many ads were found.
    search_params = {'q': query, 'limit': 0}
    json_response = _get_ads(search_params)
    number_of_hits = json_response['total']['value']
    print(f"\nNumber of hits = {number_of_hits} \n")
    print(f"\n\n{remember}")
    
def PDFreader(CuVi, adds):
    curr = PDFQuery(f'CV/{CuVi}.pdf')
    curr.load()

    adndm = PDFQuery(f'add/{adds}.pdf')
    adndm.load()

    # Use CSS-like selectors to locate the elements
    text_els1 = curr.pq('LTTextLineHorizontal')
    text_els2 = adndm.pq('LTTextLineHorizontal')

    # Extract the text from the elements
    text = [t.text for t in text_els1]
    text2 = [t.text2 for t in text_els2]

    #print(text)
    return(text, text2)

def Adreader(ad):
    with open(f"textfiler/{ad}", "r") as ad:
        return ad.read()

def LLMhelper(exp, adtext):

    openai.api_key = f'{get_API_key()}'  # Actual OpenAI API key


    openai.default_headers = {"x-foo": "true"}
    message = f"Using my experiences: {exp}, write me a concise cover letter for this ad: {adtext} in the same language as the ad, (my name is {name}) and end the document with a CV curated for the role."
    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return(completion.choices[0].message.content)

def LLMhelper2():

    openai.api_key = f'{get_API_key()}'
    

    openai.default_headers = {"x-foo": "true"}
    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return(completion.choices[0].message.content)
  

def loop_through_hits(query, amount):
    # limit = 100 is the max number of hits that can be returned.
    # If there are more (which you find with ['total']['value'] in the json response)
    # you have to use offset and multiple requests to get all ads.
    count = 0
    search_params = {'q': query, 'limit': amount}
    json_response = _get_ads(search_params)
    hits = json_response['hits']
    with open("Sok.json", "w") as file:
        file.write(json.dumps(json_response))
    for hit in hits:
        jobb = hit['headline']
        jobb_clean = f"{jobb.translate(str.maketrans('','', string.punctuation))}"
        print(f"{hit['headline']}, {hit['employer']['name']}")
        count += 1
        
        emp = hit['employer']
        if isinstance(emp, dict) and 'workplace' in emp:
            filename_helper = emp['workplace']
        
        emurl = hit['application_details']
        if isinstance(emurl, dict) and 'url' in emurl:
            surl = emurl['url']
        
        directory = Path(f"{filename_helper.translate(str.maketrans('','', string.punctuation))}")
        directory.mkdir(parents=True, exist_ok=True)
        
        filename = f"{jobb_clean} - Ad - {count}.txt"
        filePath = directory / filename
        filename2 = f"{jobb_clean} - Application - {count}.txt"
        filePath2 = directory / filename2
        
        
        description = hit['description']
        
        with open(filePath, "w") as textfile:
            textfile.write("Adlink:  " + hit['webpage_url'] + "\n\n")
        with open(filePath, "a") as tf:
            tf.write("Applylink: " + str(surl) + "\n\n")
        
        if isinstance(description, dict) and 'text' in description:
            adtexts[count] = description['text']
            with open(filePath, "a") as specfile:
                specfile.write(adtexts[count] + "\n\n")
            with open(filePath2, "w") as spcfile:
                spcfile.write(LLMhelper(PDFreader(curriculum), adtexts[count]))
           

if __name__ == "__main__":
    print("Se till att filer som ska läsas ligger i \"textfiler\"")
    name = input("Vad heter du?: ")
    curriculum = input("Vad heter din CV-fil? var noga och skriv inte in \".pdf\"\n")
    antal = input("Max antal förslag: ")
    funk = input("Vilken funktion vill du använda?(skriv nummer) \n1. Cover Letter utifrån CV och hämtade annonser.\n2. Osäker på vad du ska söka efter?\n3. Presentationstext byggd på information i CV.\n4. Teckenbegränsad Presentation.\n5. Internship email.\n6. Annons från fil.\n7. Skrapad Om-Oss till e-mail\n8. Passar jag för företaget?\n")
    if funk == "1":
        query1 = input("Skriv en sökterm (Företag, Jobb etc.): ")
        query2 = input("Var vill du jobba? (lämna tomt om N/A): ")
        query = query1+" "+query2
        loop_through_hits(query, antal)
        number_of_hits(query)
    
    if funk == "2":
        lang = input("Vilket språk? ")
        message = f"Using my experiences: {PDFreader(curriculum)} write three jobs I can do, in {lang} as three words, not a list(Maritime officer is \"fartygsbefäl\" in swedish)"
        query1 = LLMhelper2()
        query2 = input("Var vill du jobba? (lämna tomt om N/A): ")
        query = query1+" "+query2
        print(f"\nSöker efter {query1} i {query2}: \n")
        loop_through_hits(query, antal)
        number_of_hits(query)
    
    elif funk == "3":
        lang = input("Vilket språk? ")
        message = f"Using my experiences: {PDFreader(curriculum)}, write me a concise introduction in {lang} (my name is {name})"
        with open(f"Intro-{name}.txt", "w") as filli:
            filli.write(LLMhelper2())
        print(f"\n\n{remember}")
        
    elif funk == "4":
        lang = input("Vilket språk? ")
        chrs = input("Hur många tecken? ")
        message = f"Using my experiences: {PDFreader(curriculum)}, write me an introduction in {chrs} charachters, in {lang} omit name to save space"
        with open(f"{chrs}ch-{name}.txt", "w") as filli:
            filli.write(LLMhelper2())
        print(f"\n\n{remember}")
        
    elif funk == "5":
        lang = input("Vilket språk? ")
        timeframe = input("Hur lång är praktikperioden? ")
        message = f"Using my experiences: {PDFreader(curriculum)}, write me a short introduction email in {lang} asking for an {timeframe} internship (my name is {name})"
        with open(f"Email-{name}.txt", "w") as filli:
            filli.write(LLMhelper2())
        print(f"\n\n{remember}")
        
    elif funk == "6":
        adtext = input("Vad heter filen (Fullt namn med filtyp)? ")
        message = f"Using my experiences: {PDFreader(curriculum)}, write me a concise cover letter for this ad: {Adreader(adtext)} in the same language as the ad, (my name is {name}) and end the document with a CV curated for the role"
        with open(f"Applikation-{name}.txt", "w") as filli:
            filli.write(LLMhelper2())
        print(f"\n\n{remember}")
        
    elif funk == "7":
        lang = input("Vilket språk? ")
        ScURL = input("Skriv in hemsidan (Gärna en \"Om-Oss\" eller liknande): ")
        message = f"Using my experiences: {PDFreader(curriculum)}, write me an introdution email for this company: {scrapey(ScURL)}, in {lang}, my name is {name}"
        with open(f"Scrape-Intro-Email-{name}.txt", "w") as filli:
            filli.write(LLMhelper2())
        print(f"\n\n{remember}")
    
    elif funk == "8":
        ScURL = input("Skriv in hemsidan (Gärna en \"Om-Oss\" eller liknande): ")
        message = f"Using my experiences: {PDFreader(curriculum)}, In a couple of sentences, Am I a good fit for this company: {scrapey(ScURL)}? Yes or No (in Swedish)"
        
        print(f"\n{LLMhelper2()}")    
        
    else:
        print("Välj ett nummer i listan")
        
                