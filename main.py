import sys

def simple_local_ai_assistant():
    print("Merhaba! Ben terminalinizdeki yerel yapay zeka asistanınız.") # Hello! I'm your local AI assistant in the terminal.
    print("Gemma gibi büyük modellerin yerel olarak çalıştırılmasını simüle ediyorum.") # I'm simulating running large models like Gemma locally.
    print("Çıkmak için 'çıkış' veya 'exit' yazın.") # Type 'çıkış' or 'exit' to quit.

    while True:
        try:
            user_input = input("\nSiz: ").strip().lower() # You:
            if user_input in ["çıkış", "exit", "quit", "q"]:
                print("Görüşmek üzere! Yerel yapay zeka deneyiminiz devam ediyor.") # See you! Your local AI experience continues.
                break
            elif "gemma" in user_input:
                # This response simulates knowledge about Gemma, as if a local LLM is providing info.
                response = "Gemma, Google tarafından geliştirilen hafif ve güçlü bir açık model ailesidir. Yerel olarak çalıştırılabilir!"
            elif "yerel" in user_input or "local" in user_input:
                # Highlights the 'local' aspect, central to the article's theme.
                response = "Evet, bu program yerel bir yapay zeka deneyimini simüle ediyor. Gerçek Gemma modelleri daha fazla kurulum gerektirir."
            elif "yapay zeka" in user_input or "ai" in user_input:
                # Explains AI and the benefits of local execution.
                response = "Yapay zeka (AI), makinelerin insan benzeri zeka sergilemesini sağlayan teknolojidir. Yerel olarak çalıştırmak gizlilik ve hız avantajları sunar."
            elif "nasıl" in user_input or "how" in user_input:
                # Gives a hint about real-world local LLM setup, acknowledging the simulation.
                response = "Gerçek Gemma modelini yerel olarak çalıştırmak için genellikle 'ollama' veya 'llama.cpp' gibi araçlar kullanılır. Bu örnek sadece bir simülasyondur."
            else:
                # A generic response for other inputs, maintaining the assistant persona.
                response = "İlginç bir soru! Yerel yapay zeka asistanınız olarak öğrenmeye devam ediyorum."

            print(f"Asistan: {response}") # Assistant:

        except EOFError:
            print("\nEOF algılandı. Çıkılıyor.") # EOF detected. Exiting.
            break
        except KeyboardInterrupt:
            print("\nKesme algılandı. Çıkılıyor.") # Interrupt detected. Exiting.
            break

if __name__ == "__main__":
    simple_local_ai_assistant()
