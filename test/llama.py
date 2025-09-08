import ollama
from utils.PyLogger import PyLogger as logs
from config import OLLAMA_URL


def interactive_chat():
    print("\nLlama 3 Chat Assistant (type '/quit' to exit)")
    print("-------------------------------------------\n")
    
    # Initialize conversation history
    conversation = []
    
    while True:
        try:
            prompt = input("You: ")
            
            if prompt.lower() in ['/quit', '/exit', '/bye']:
                print("Ending chat session. Goodbye!")
                break
                
            if prompt.lower() == '/clear':
                conversation = []
                print("Conversation history cleared.")
                continue
                
            conversation.append({'role': 'user', 'content': prompt})
            
            print("\nAssistant: ", end='', flush=True)
            
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
    interactive_chat()
    logs.info("Done")


if __name__ == "__main__":
    main()
