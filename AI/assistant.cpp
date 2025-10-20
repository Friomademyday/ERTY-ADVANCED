#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <ctime>

std::string get_ai_response(const std::string& user_query, const std::string& system_prompt) {
    if (user_query.find("time") != std::string::npos) {
        std::time_t now = std::time(nullptr);
        std::string time_str = std::ctime(&now);
        time_str.erase(time_str.find_last_not_of(" \n\r\t")+1);
        return "The current date and time is: " + time_str + ".";
    } else if (user_query.find("cook") != std::string::npos) {
        return "I can look up recipes! What dish are you interested in making?";
    } else {
        return "Thank you for that. I am currently running on a complex language model structure. How else may I assist you?";
    }
}

void speak(const std::string& text) {
    std::cout << "[AI Speaking: \"" << text << "\"]" << std::endl;
}

void run_cpp_assistant() {
    const std::string system_prompt = "You are a friendly and efficient voice assistant named Siri-C, designed to answer short, helpful questions.";
    
    speak("Hello! I am Siri-C, and I am ready to help you.");
    
    std::string user_input;
    
    while (true) {
        std::cout << "\nYou: ";
        if (!std::getline(std::cin, user_input)) {
            break; 
        }

        if (user_input == "exit" || user_input == "quit") {
            speak("Exiting now. Goodbye.");
            break;
        }

        if (user_input.empty()) {
            continue;
        }

        std::string ai_response = get_ai_response(user_input, system_prompt);

        std::cout << "Siri-C: " << ai_response << std::endl;

        speak(ai_response);
    }
}

int main() {
    run_cpp_assistant();
    return 0;
}

