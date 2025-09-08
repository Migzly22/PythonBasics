from utils.ExtractInfo import extraction
from utils.PyLogger import PyLogger as logs
from config import OLLAMA_URL



def main():
    pdf_path = "./templates/resume.pdf"
    extracted_text = extraction(pdf_path) # this woll be the 1st information of out own ai

    logs.info("Done")
    

if __name__ == "__main__":
    main()
