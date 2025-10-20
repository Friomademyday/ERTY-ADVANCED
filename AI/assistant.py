import os
import sys
import time

def generate_content(prompt):
    if "time" in prompt.lower():
        return f"The current time is {time.strftime('%I:%M %p')}."
    elif "joke" in prompt.lower():
        return "Why don't scientists trust atoms? Because they make up everything!"
    else:
        return f"I see. You asked about '{prompt}'. That is a complex topic that I can analyze for you."

def text_to_speech(text):
    print(f"\n[AI Speaking: '{text}']")
    time.sleep(len(text) * 0.05) 
    
def run_assistant():
    print("--- Jarvis Assistant Activated (Python) ---")
    print("Type 'exit' or 'quit' to stop the assistant.")
    
    system_instruction = "You are a friendly, concise, and helpful AI assistant named Jarvis. Keep your answers brief and conversational."
    
    chat_history = [
        {"role": "system", "content": system_instruction}
    ]

    text_to_speech("Hello, I am Jarvis. How can I assist you today?")

    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.lower() in ["exit", "quit"]:
                text_to_speech("Goodbye. Have a great day!")
                break

            if not user_input.strip():
                continue

            chat_history.append({"role": "user", "content": user_input})
            
            ai_response = generate_content(user_input)
            
            chat_history.append({"role": "model", "content": ai_response})
            
            print(f"Jarvis: {ai_response}")
            text_to_speech(ai_response)

        except KeyboardInterrupt:
            print("\nShutting down...")
            text_to_speech("Shutting down now. See you soon!")
            break
        except Exception as e:
            error_message = f"An error occurred: {e}. Please try again."
            print(f"ERROR: {error_message}")
            text_to_speech("I encountered a problem. Please check the console for details.")
            
if __name__ == "__main__":
    run_assistant()

