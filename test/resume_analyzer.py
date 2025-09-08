import ollama
import PyPDF2
from utils.ExtractInfo import extraction
from utils.PyLogger import PyLogger as logs
from config import OLLAMA_URL



def scan_pdf(*, file_content : str, job_role: str = 'general job applications'):
    # Initialize conversation history
    conversation = []
    

    try:
        
        prompt = f"""Please analyze this resume and provide constructive feedback. 
        Focus on the following aspects:
        1. Content clarity and impact
        2. Skills presentation
        3. Experience descriptions
        4. Specific improvements for {job_role}
        
        Resume content:
        {file_content}
        
        Please provide your analysis in a clear, structured format with specific recommendations."""
            
        conversation.append({"role": "system", "content": "You are an expert resume reviewer with years of experience in HR and recruitment."})
        conversation.append({"role": "user", "content": prompt})
        
        full_response = []
        
        # Explicitly specify the host in the client
        client = ollama.Client( host = OLLAMA_URL )
        stream = client.chat(
            model='llama3',
            messages=conversation,
            stream=True
        )
        
        for chunk in stream:
            part = chunk['message']['content']
            print(part, end='', flush=True)
            full_response.append(part)
        
        conversation.append({
            'role': 'assistant', 
            'content': ''.join(full_response)
        })
        
        print("\n")
        
    except KeyboardInterrupt:
        print("\nUse '/quit' to exit properly.")
    except Exception as e:
        print(f"\nError: {str(e)}")
        conversation = []





def main():
    pdf_path = "./templates/resume.pdf"
    extracted_text = extraction(pdf_path)

    scan_pdf(
        file_content= extracted_text,
        job_role = "Software Engineer"
    )
    
    logs.info("Done")
    

if __name__ == "__main__":
    main()
