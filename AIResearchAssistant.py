"""
The purpose of this project is to provide students a helping tool. No matter if the student is no college,university,
or high school. This program offers such tools as a text summarizer, Wikipedia scraper, text-to-speech to give
presentations, text-to-PDF tool, and a chatbot which will act as extra help with providing helpful information to
students.
"""


# General Libraries
import tkinter as tk
# Library for wikipedia data collection
import wikipedia
from tkinter import *
# Specific GUI Window Tabs Libraries
from tkinter import ttk
from tkinter.scrolledtext import *
# Import from SummarizeText.py
from SummarizeText import SummarizeText
# Importing Google text-to-speech library
from gtts import gTTS
# Importing pyttsx3 text-to-speech library
import pyttsx3
# Importing fpdf library
from fpdf import FPDF
# Importing ChattberBot library
from chatterbot import ChatBot
# Importing Chatterbot.trainers library
from chatterbot.trainers import ListTrainer
# Importing pyjokes library
import pyjokes

# Imported to play the converted audio file
import os

# Create GUI
# Create Window
# Build Main Window
window = tk.Tk()
# Main Window Title
# AI Research Assistant
window.title("AI Research Assistant")
# Window Size
# Wide x Tall
# window.geometry('825x800')
window.geometry("825x800")

# Set style of tabs
style = ttk.Style(window)
# Set location of tabs
# wn = West North
style.configure('lefttab.TNotebook', tabpostition='wn')

# tab_control =ttk.Notebook(window)
# Collect and display all tabs starting from left to right.
tab_control = ttk.Notebook(window, style='lefttab.TNotebook')

# Create tabs
# Tab for AI that generates AI
tab_summarize = ttk.Frame(tab_control)
# Tab for Wikipedia Search
tab_wikipedia_search = ttk.Frame(tab_control)
# Tab for verbal presentation
tab_verbal_presentation = ttk.Frame(tab_control)
# Tab for verbal presentation that can be used offline
tab_verbal_presentation_2 = ttk.Frame(tab_control)
# Tab for text to PDF file converter
tab_pdf_converter = ttk.Frame(tab_control)
#
tab_chatbot = ttk.Frame(tab_control)

# Add tabs to window
# Name for this tab is AI Summarizer
tab_control.add(tab_summarize, text='AI Summarizer')
# Name for this tab is AI Wikipedia Searcher
tab_control.add(tab_wikipedia_search, text='AI Wikipedia Searcher')
# Name for this tab is AI Verbal Presenter
tab_control.add(tab_verbal_presentation, text='AI Verbal Presenter')
# Name for this tab is AI Verbal Presenter 2
tab_control.add(tab_verbal_presentation_2, text='AI Offline Verbal Presenter')
# Name for this tab is AI PDF Converter
tab_control.add(tab_pdf_converter, text='AI PDF Converter')
# Name for this tab is AI ChatBot
tab_control.add(tab_chatbot, text='AI Chatbot')


# Create GUI Labels
# Place GUI Labels
# Label on the text summarizer tab will state AI Summarizer Assistant
label_summarize = Label(tab_summarize, text='AI Summarizer Assistant', padx=5, pady=5).grid(column=0, row=0)
# Label on the Wikipedia Searcher will state AI Wikpedia Searcher
label_wikipedia_search = Label(tab_wikipedia_search, text='AI Wikipedia Searcher', padx=5, pady=5).grid(column=0, row=0)
# Label on the AI Verbal Presenter will state AI Verbal Text-To-Speech Assistant
label_verbal_presentation = Label(tab_verbal_presentation, text='AI Verbal Text-To-Speech Assistant', padx=5, pady=5)\
    .grid(column=0, row=0)
# Label on the Offline AI Verbal Presenter will state AI Verbal Text-To-Speech Assistant Offline Mode
label_verbal_presentation_2 = Label(tab_verbal_presentation_2, text='AI Verbal Text-To-Speech Assistant Offline Mode',
                                    padx=5, pady=5).grid(column=0, row=0)
# Label on text to PDF file converter will state AI Convert Text to PDF
label_pdf_converter = Label(tab_pdf_converter, text='AI Convert Text to PDF', padx=5, pady=5)\
    .grid(column=0, row=0)
# Label on text to PDF file converter will state AI Chatbot Named Peanut
label_chatbot = Label(tab_chatbot, text='AI Chatbot Named Peanut', padx=5, pady=5).grid(column=0, row=0)

# 0,0 is top left of window

# Pack to make visible
tab_control.pack(expand=1, fill='both')


# Functions
# Function to summarize text
def text_summary():
    # Imports for parser_config
    # Using sumy library for text summarization
    # Text parsing used to split up the sequence of text
    from sumy.parsers.plaintext import PlaintextParser
    # Importing sumy tokenizer library
    # Tokenization is used for splitting up large bodies of text into smaller ones
    from sumy.nlp.tokenizers import Tokenizer
    # Collect user input from the entry box
    text_format = summary_entry.get('1.0', tk.END)
    # We can use this parse format for all three when we use raw strings
    # Parsing all text using Lexrank, Luhn, and LSA
    # Lexrank = Based of the idea that sentences recommend other similar sentences
    # Luhn = Based on frequency of important words
    # LSA = Based on term frequency techniques
    # Tokenize the words in English
    parser_config = PlaintextParser.from_string(text_format, Tokenizer("english"))
    # variable correlating to the SummarizeText.py / SummarizeText class
    summarize_text = SummarizeText()
    # Summarize all text using Lexrank
    # Lexrank = Based of the idea that sentences recommend other similar sentences
    # summer_all = print(), summer_all
    summer_all = summarize_text.lex_rank_analysis(parser_config, 2)
    # summarize all text using LSA
    # LSA = Based on term frequency techniques
    # summer_all = print(), summer_all
    summer_all = summer_all + summarize_text.lsa_analysis(parser_config, 2)
    # An Array to collect the summarized text
    text_summary_list = []
    # for each sentence that has gone through parsing display them and split them up using {}
    for sentence in summer_all:
        # String concatenation for each sentence
        concat = str(sentence) + "\n\n\n"
        # Split up all sentences using {}
        concat.replace("", "{")
        concat.replace("", "}")
        # Add the item (sentence) to the list
        text_summary_list.append(concat)
    # Display the summarized text
    summary_output_display.insert(tk.END, text_summary_list)
    # For Debug console
    # Print out the results through console
    print("\nAbout to print summer all results\n")
    print(summer_all)


# Function to delete user input in the summary entry box
def summary_erase_input():
    # Delete all user input placed in the entry box
    summary_entry.delete(1.0, END)


# Function to delete what the program outputs
def summary_erase_output():
    # Delete all text placed in the output display box
    summary_output_display.delete(1.0, END)


# Function to generate a Wikipedia summary
def wikipedia_summary():
    # A variable that correlates to what the user inputs in the wikipedia_entry box
    search_phrase = wikipedia_entry.get()
    # A variable that correlates to what the user inputs in the Wikipedia_amount_of_sentences entry box
    number_of_sentences = wikipedia_amount_of_sentences.get()
    # A variable that correlates to the Wikipedia algorithm that generates the Wikipedia summary
    wikipedia_output = wikipedia.summary(search_phrase, sentences=number_of_sentences)
    # Display the Wikipedia summary in the wikipedia_output_display box
    wikipedia_output_display.insert(tk.END, wikipedia_output + '\n=================================================='
                                                               '==============================')


# Function to generate a Wikipedia article
def wikipedia_article():
    # A variable that correlates to what the user inputs in the wikipedia_entry box
    search_phrase = wikipedia_entry.get()
    # A variable that correlates to the Wikipedia algorithm that generates the Wikipedia article
    wikipedia_output = wikipedia.page(search_phrase).content
    # Display the Wikipedia summary in the wikipedia_output_display box
    wikipedia_output_display.insert(tk.END, wikipedia_output + '\n===================================================='
                                                               '============================')


# Function that deletes user input in th Wikipedia Searcher tab
def wikipedia_erase_input():
    # Delete any input in the wikipedia topic search box
    wikipedia_entry.delete(0, 'end')
    # Delete any input in the amount of sentences box
    wikipedia_amount_of_sentences.delete(0, 'end')


# Function that deletes what the program outputs
def wikipedia_erase_output():
    # Delete all text placed in the output display box
    wikipedia_output_display.delete(1.0, END)


# Function that collects user input and convert it into an audio file
def text_to_speech_user_input():
    # English language
    language = 'en'
    # Collect user input
    user_text_to_speech = verbal_entry.get('1.0', END)
    # Convert user input into audio file
    text_to_speech_output = gTTS(text=user_text_to_speech, lang=language, slow=False)
    # Save the audio file
    text_to_speech_output.save("audioOverwrite.mp3")
    # Play the converted file
    os.system("start audioOverwrite.mp3")
    # Collect user input to convert it into the output display
    user_text_to_speech_output = user_text_to_speech
    # Display user input into the output display box
    # Output display box will also have a divider
    verbal_output_display.insert(tk.END, user_text_to_speech_output + '==============================================='
                                                                      '=================================')


# Function that collects text from text file and convert it into an audio file
def text_to_speech_file():
    # English language
    language = 'en'
    # Open the text file (TextSpeech.txt)
    text_file = open("TextSpeech.txt", "r").read().replace("\n", " ")
    # Convert the text in the text file into audio
    speech_file = gTTS(text=text_file, lang=language, slow=False)
    # Save the audio file
    speech_file.save("audioOverwrite.mp3")
    # Play the converted file
    os.system("start audioOverwrite.mp3")
    # Display the text from the text file into the output display box
    # Output display box will also have a divider
    verbal_output_display.insert(tk.END, text_file + '\n============================================================'
                                                     '====================')


# Function to delete user input in the verbal entry box
def verbal_erase_input():
    # Delete all text placed in the entry box
    verbal_entry.delete(1.0, END)


# Function to delete what the program outputs
def verbal_erase_output():
    # Delete all text placed in the output display box
    verbal_output_display.delete(1.0, END)


# Function that collects user input and converts it into speech
def text_to_speech_user_input_2():
    # Creating the engine pyttsx3 object
    engine = pyttsx3.init()

    # Setting the rate of thr speech to 155
    engine.setProperty('rate', 155)
    # Setting the volume to 1.0 = MAX
    engine.setProperty('volume', 1.0)

    # Collect user input
    user_text_to_speech_2 = verbal_entry_2.get('1.0', END)
    # Variable that correlates to user input
    user_text_to_speech_output_2 = user_text_to_speech_2
    # Display the user input into the output display box
    # Output display will also have a divider
    verbal_output_display_2.insert(tk.END, user_text_to_speech_output_2 + '==========================================='
                                                                          '=====================================')
    # Converting the text to speech
    engine.say(user_text_to_speech_2)
    # Run and block all queued commands
    engine.runAndWait()


# Function to delete all user input
def verbal_erase_input_2():
    # Delete all text placed in the entry box
    verbal_entry_2.delete(1.0, END)


# Function to delete the text in the output display box
def verbal_erase_output_2():
    # Delete all text in the output display box
    verbal_output_display_2.delete(1.0, END)


# Function to delete input for PDF paper title
def pdf_erase_input_settings():
    # Delete all text in the pdf title entry box
    pdf_title_entry.delete(0, 'end')


# Function to delete all text in the scrolled bar user text input
def pdf_erase_text_input():
    # Delete all text in the pdf user text entry
    pdf_text_entry.delete(1.0, END)


# Function to generate a pdf file from user text
def pdf_text_to_pdf_file():
    # Variable for PDF
    pdf = FPDF()
    # Adding a PDF file page
    pdf.add_page()

    # Variable that correlate to collecting user input for PDF title
    pdf_title = pdf_title_entry.get()
    # Variable that correlates to collecting user text input
    pdf_body_text = pdf_text_entry.get('1.0', END)

    # Font for the PDF text will be Times in size 12
    pdf.set_font("Times", size=12)

    # PDF header text
    pdf.cell(200, 10, txt=pdf_title, ln=1, align='C')

    # PDf body text
    pdf.multi_cell(200, 10, txt=pdf_body_text, align='L')

    # save the pdf with name .pdf
    pdf.output("AI-Assistant.pdf")


# Function to erase output in ScrolledText (Text history log)
def chatbot_erase_output():
    # delete any text in the chatbot output display box
    chatbot_output_display.delete(1.0, END)


# Function for Chatbot to process text
def chatbot_text_process():
    # chatbot_text_entry.delete(0, 'end')
    bot = ChatBot(
        'Peanut',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        logic_adapters=[
            {
                # Best choice logic adapter
                'import_path': 'chatterbot.logic.BestMatch',
                # If the user inputs a something the chatbot does not understand state this below
                'default_response': 'I am sorry, but I do not understand.',
                'maximum_similarity_threshold': 0.90
            },
            # Logic adapter to solve math questions
            'chatterbot.logic.MathematicalEvaluation',
            # Logic adapter to tell time
            'chatterbot.logic.TimeLogicAdapter',
            # Logic adapter to solve unit conversion questions
            'chatterbot.logic.UnitConversion',
        ],
        # Provide a database uri with sqlite
        database_uri='sqlite:///database.sqlite3'
    )

    # Training the chatbot in introducing itself to user
    conversation_intro = [
        "Hello",
        "Hi there!",
        "How are you doing?",
        "I'm doing great.",
        "That is good to hear",
        "Thank you.",
        "You're welcome."
    ]

    # Training the chatbot in providing a link to a chatbot guide website
    conversation_create_chatbot_help = [
        'I want to create a chat bot',
        'Have you read the documentation?',
        'No, I have not',
        'I recommend this chatbot guide website: http://chatterbot.rtfd.org/en/latest/quickstart.html'
    ]

    # Training the chatbot in providing a link to a quiz help website
    conversation_quiz_help = [
        'I want help with quizzes',
        'I recommend this quiz website: https://quizlet.com/'
    ]

    # Training the chatbot in providing a link to a grammar assistant website
    conversation_grammar_help = [
        'I want help with grammar',
        'I recommend this grammar website: https://www.grammarly.com/'
    ]

    # Training the chatbot in providing a link to a studying assistant website
    conversation_studying_help = [
        'I want help with studying',
        'I recommend this studying website: https://www.wolframalpha.com/'
    ]

    # Training the chatbot in providing a link to a college/university website
    conversation_college_help = [
        'I want help with college/university',
        'I recommend this college help website: https://www.koofers.com/'
    ]

    # Training the chatbot in providing a website to a website that helps form good habits
    conversation_habits_help = [
        'I want help with forming good habits',
        'I recommend this website to get into good habits: https://habitica.com/static/home'
    ]

    # Training the chatbot in providing a website that help's in citation
    conversation_citation_help = [
        'I want help with citation',
        'I recommend this citation website: https://www.citefast.com/?s=APA7#_Webpage'
    ]

    # Training the chatbot in providing a website in helping find jobs
    conversation_work_help = [
        'I want help with finding a job',
        'I recommend this website to find work: https://www.indeed.com/'
    ]

    # Training the chatbot in providing a website in helping find digital storage
    conversation_storage_help = [
        'I want help with storage',
        'I recommend this digital storage website: https://www.google.com/drive/'
    ]

    # Training the chatbot in telling programming jokes
    conversation_programmer_joke = [
        'Tell me a programmer joke',
        pyjokes.get_joke(),  # Tell a programmer joke
        'Tell me another joke',
        pyjokes.get_joke(),  # Tell a different programmer joke
        'Tell me one more joke',
        pyjokes.get_joke(),  # Tell a different programmer joke
        'One more joke',
        pyjokes.get_joke(),  # Tell a different programmer joke
        'Okay one last joke',
        pyjokes.get_joke(),  # Tell a different programmer joke
    ]

    # Establish training modules for the chatbot
    trainer = ListTrainer(bot)

    # Establish the training module for conversation_intro conversation sequence
    trainer.train(conversation_intro)
    # Establish the training module for conversation_create_chatbot_help conversation sequence
    trainer.train(conversation_create_chatbot_help)
    # Establish the training module for conversation_quiz_help conversation sequence
    trainer.train(conversation_quiz_help)
    # Establish the training module for conversation_grammar_help conversation sequence
    trainer.train(conversation_grammar_help)
    # Establish the training module for conversation_studying_help conversation sequence
    trainer.train(conversation_studying_help)
    # Establish the training module for conversation_college_help conversation sequence
    trainer.train(conversation_college_help)
    # Establish the training module for conversation_habits_help conversation sequence
    trainer.train(conversation_habits_help)
    # Establish the training module for conversation_citation_help conversation sequence
    trainer.train(conversation_citation_help)
    # Establish the training module for conversation_work_help conversation sequence
    trainer.train(conversation_work_help)
    # Establish the training module for conversation_storage_help conversation sequence
    trainer.train(conversation_storage_help)
    # Establish the training module for conversation_programmer_joke conversation sequence
    trainer.train(conversation_programmer_joke)

    # The following loop will execute each time the user enters input
    while True:
        # Collect user input from entry box
        user_input = chatbot_text_entry.get()
        # delete text when text is sent
        chatbot_text_entry.delete(0, 'end')

        # Chatbot will not process the text
        response = bot.get_response(user_input)

        # Display the chatbot's response through ths format
        chatbot_output_display.insert(
            tk.END, "Human: " + user_input + "\n" + "Peanut: " + str(response.text) + "\n"
        )


# Main Home Tab
# AI Text Summary Tab
# Create label to instruct the user on how to use the AI summarizer program
Label(tab_summarize, text='Enter any text you want in the box below to be summarized...', padx=5, pady=5)\
    .grid(row=1, column=0)
# Create a label to instruct the user on how to use the AI Wikipedia search program
Label(tab_wikipedia_search, text='1) Enter any word or phrase in the designated box.\n2) Type the amount of sentences'
                                 'you want in the wiki summary (OPTIONAL).\n 3) Click Generate Wikipedia Summary to '
                                 'generate a'
                                 'Wikipedia summary which length will depend on your amount of sentences.\n4) Click'
                                 'Generate Wikipedia Article to generate the entire Wikpedia article on your topic.',
      padx=5, pady=5).grid(row=1, column=0)

# Create a label to instruct the user to input the word or phrase they want AI to search in Wikipedia
Label(tab_wikipedia_search, text="Enter the word or phrase here (TOPIC):").grid(row=2)
# Create a label to instruct the user to input the amount of sentences they in their Wikipedia summary
Label(tab_wikipedia_search, text='Enter the amount of sentences you want in the Wikipedia summary here (OPTIONAL):')\
    .grid(row=3)
# Create a label to instruct the user to input the text they want converted into audio
Label(tab_verbal_presentation, text='Enter any text you want in the box below to be converted to text-to-speech...',
      padx=5, pady=5).grid(row=1, column=0)
# Create a label that says OR
Label(tab_verbal_presentation, text='OR', padx=5, pady=5).grid(row=2, column=0)
# Create a label that instructs the user they can edit the text file in the project they want converted into audio
Label(tab_verbal_presentation, text='You can also edit the text file.', padx=5, pady=5).grid(row=3, column=0)

# Create a label that will inform the user to use this AI verbal presenter if they don't internet
Label(tab_verbal_presentation_2, text='Use this AI verbal presenter if you do not have an internet connection.', padx=5,
      pady=5).grid(row=1, column=0)
# Create a label that will instruct the user on how to operate the offline AI verbal presenter
Label(tab_verbal_presentation_2, text='Enter any text you want in the box below to be converted to text-to-speech...',
      padx=5, pady=5).grid(row=2, column=0)

# Create a label that will inform the user to use the AI PDF converter to convert their text into a PDf file
Label(tab_pdf_converter, text='Use this AI PDF Converter to convert your text into a PDF file.', padx=5, pady=5).grid(
    row=1, column=0)
# Create a label that will instruct the user on how to use the AI PDF Converter
Label(tab_pdf_converter, text='1) Enter the title for your PDF paper.'
                              '\n2) Enter the text you want to implement into the PDF file.\n3) Check the PDF file in '
                              'the project folder located in the file explorer.', padx=5, pady=5).grid(row=2, column=0)

# Create a label that informs the user to enter a title for their PDF paper
Label(tab_pdf_converter, text='Enter the title of the PDF file:', padx=5, pady=5).grid(row=4, column=0)
# Create a label to instruct the user to put text in the scrolled text box below
Label(tab_pdf_converter, text='Enter the body text you want in the PDF file...', padx=5, pady=5).grid(row=8, column=0)

# Create a label that informs to use this AI to interact with the chatbot named Peanut
Label(tab_chatbot, text='Use this AI to interact with the chatbot named Peanut.', padx=5, pady=5).grid(row=1, column=0)
# Create a label that informs the user to enter the text they want to send to peanut
Label(tab_chatbot, text='Enter the text you want to send to peanut:', padx=5, pady=5).grid(row=2, column=0)


# Establish that the user entry box be scrolled text giving it scroll bar
summary_entry = ScrolledText(tab_summarize, height=10, wrap=WORD)
# Create a grid for user entry box
summary_entry.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Entry box for user to input their Wikipedia subject
wikipedia_entry = Entry(tab_wikipedia_search)
# Entry box for user to input the amount of sentences they want in their Wikipedia summary
wikipedia_amount_of_sentences = Entry(tab_wikipedia_search)

# Create a grid for the wikipedia_entry box
wikipedia_entry.grid(row=2, column=1)
# Create a grid for the wikipedia_amount_of_sentences entry box
wikipedia_amount_of_sentences.grid(row=3, column=1)

# Create a entry box with a scrolled text property
verbal_entry = ScrolledText(tab_verbal_presentation, height=10, wrap=WORD)
# Create a grid for the verbal_entry box
verbal_entry.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Create a entry box with a scrolled text property for the offline AI verbal presenter
verbal_entry_2 = ScrolledText(tab_verbal_presentation_2, height=10, wrap=WORD)
# Create a grid for verbal_entry_2 box
verbal_entry_2.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Create a entry box for the user to input their title for the PDF paper
pdf_title_entry = Entry(tab_pdf_converter)
# Create a grid for the pdf_title_entry
pdf_title_entry.grid(row=4, column=1)
# Create a entry box with a scrolled text property for user to input text to convert to the PDF file
pdf_text_entry = ScrolledText(tab_pdf_converter, height=10, wrap=WORD)
# Create a grid fpr pdf_text_entry
pdf_text_entry.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

# Create an entry box for user input
chatbot_text_entry = Entry(tab_chatbot)
# Create a grid for chatbot_text_entry
chatbot_text_entry.grid(row=2, column=1)

# Buttons
# Buttons for AI Text Summary
# Button to erase all text from the entry box
# Button with text saying Clear Input to instruct user
# Button correlates to the erase_input function
# Button is blue with white text
button_text_summary_input = Button(tab_summarize, text='Clear Input', command=summary_erase_input, width=30, bg='blue',
                                   fg='#fff')
# Create a grid for the Clear Input button
button_text_summary_input.grid(row=3, column=0, padx=10, pady=10)

# Button to process user input
# Button with text saying Generate Summary to instruct user
# Button correlates to text_summary function
# Button is red with white text
button_text_summary_process = Button(tab_summarize, text="Generate Summary", command=text_summary, width=30, bg='red',
                                     fg='#fff')
# Create a grid for the Generate Summary button
button_text_summary_process.grid(row=4, column=0, padx=10, pady=10)

# Button to erase all text in the display box
# Button with text saying Clear Output to instruct user
# Button correlates to the erase_output function
# Button is blue with white text
button_text_summary_output = Button(tab_summarize, text='Clear Output', command=summary_erase_output, width=30,
                                    bg='blue',
                                    fg='#fff')
# Create a grid for the Clear Output button
button_text_summary_output.grid(row=5, column=0, padx=10, pady=10)

# Button to clear all user input in the entry boxes
# Button with text saying Clear Output to instruct user
# Button correlates to wikipedia_erase_input function
# Button is green with white text
button_wikipedia_search_input = Button(tab_wikipedia_search, text='Clear Input', command=wikipedia_erase_input,
                                       width=30, bg='green', fg='#fff')
# Create a grid for the Clear Input button
button_wikipedia_search_input.grid(row=7, column=0, padx=10, pady=10)

# Button to clear all program output in the output display box
# Button with text saying Clear Output to instruct user
# Button correlates to wikipedia_erase_output function
# Button is green with white text
button_wikipedia_search_output = Button(tab_wikipedia_search, text='Clear Output', command=wikipedia_erase_output,
                                        width=30, bg='green', fg='#fff')
# Create a grid for the Clear Output button
button_wikipedia_search_output.grid(row=8, column=0, padx=10, pady=10)

# Button to generate Wikipedia summary
# Button with text saying Generate Wikipedia Summary
# Button correlates to wikipedia_summary function
# Button is green with white text
button_wikipedia_summary_process = Button(tab_wikipedia_search, text='Generate Wikipedia Summary',
                                          command=wikipedia_summary, width=30, bg='green', fg='#fff')
# Create a grid for Generate Wikipedia Summary button
button_wikipedia_summary_process.grid(row=9, column=0, padx=10, pady=10)

# Button to generate Wikipedia article
# Button with text saying Generate Wikipedia Article
# Button correlates to wikipedia_article function
# Button is green with white text
button_wikipedia_article_process = Button(tab_wikipedia_search, text='Generate Wikipedia Article',
                                          command=wikipedia_article, width=30, bg='green', fg='#fff')
# Create a grid for Generate Wikipedia Article
button_wikipedia_article_process.grid(row=10, column=0, padx=10, pady=10)

# Button to clear all user input in the entry boxes
# Button with text saying Clear Input to instruct user
# Button that correlates to verbal_erase_input function
# Button is blue with white text
button_verbal_erase_input = Button(tab_verbal_presentation, text='Clear Input', command=verbal_erase_input, width=30,
                                   bg='blue', fg='#fff')
# Create a grid for the Clear Input button
button_verbal_erase_input.grid(row=5, column=0, padx=10, pady=10)

# Button to clear all program output in the output display box
# Button with text saying Clear Output to instruct user
# Button that correlates to verbal_erase_output function
# Button is blue with white text
button_verbal_erase_output = Button(tab_verbal_presentation, text='Clear Output', command=verbal_erase_output, width=30,
                                    bg='blue', fg='#fff')
# Create a grid for the Clear Output button
button_verbal_erase_output.grid(row=8, column=0, padx=10, pady=10)

# Button to generate speech audio from user input
# Button saying Generate Speech Audio to instruct user
# Button correlates with text_to_speech_user_input function
# Button is red with white text
button_verbal_process = Button(tab_verbal_presentation, text='Generate Speech Audio', command=text_to_speech_user_input,
                               width=30, bg='red', fg='#fff')
# Create a grid for the Generate Speech audio from user input button
button_verbal_process.grid(row=6, column=0, padx=10, pady=10)

# Button to Generate Speech Audio From Text File
# Button saying Generate Speech Audio From Text File to instruct user
# Button correlates to Generate Speech Audio From Text File function
# Button is red with white text
button_verbal_text_file_process = Button(tab_verbal_presentation, text='Generate Speech Audio From Text File',
                                         command=text_to_speech_file, width=30, bg='red', fg='#fff')
# Create a grid for Generate Speech Audio From Text File
button_verbal_text_file_process.grid(row=7, column=0, padx=10, pady=10)

# Button to clear all user input in the entry boxes
# Button with text saying Clear Text Input to instruct user
# Button that correlates to verbal_erase_input_2 function
# Button is blue with white text
button_verbal_erase_input_2 = Button(tab_verbal_presentation_2, text='Clear Text Input', command=verbal_erase_input_2,
                                     width=30, bg='blue', fg='#fff')
# Create a grid for the Clear Input button
button_verbal_erase_input_2.grid(row=4, column=0, padx=10, pady=10)

# Button to clear all program output in the output display box
# Button with text saying Clear Output to instruct user
# Button that correlates to verbal_erase_output_2 function
# Button is blue with white text
button_verbal_erase_output_2 = Button(tab_verbal_presentation_2, text='Clear Output', command=verbal_erase_output_2,
                                      width=30, bg='blue', fg='#fff')
# Create a grid for the Clear Output button
button_verbal_erase_output_2.grid(row=6, column=0, padx=10, pady=10)

# Button to generate speech audio
# Button with text saying Generate Speech Audio
# Button correlates to text_to_speech_user_input_2 function
# Button is red with white text
button_verbal_process_2 = Button(tab_verbal_presentation_2, text='Generate Speech Audio',
                                 command=text_to_speech_user_input_2, width=30, bg='red', fg='#fff')
# Create a grid for generating speech audio button
button_verbal_process_2.grid(row=5, column=0, padx=10, pady=10)

# Button to clear title input
# Button with text saying clear Title Input
# Button correlates to pdf_erase_input_settings function
# Button is blue with white text
button_pdf_erase_input_settings = Button(tab_pdf_converter, text='Clear Title Input',
                                         command=pdf_erase_input_settings, width=30, bg='blue', fg='#fff')
# Create a grid for clearing title input button
button_pdf_erase_input_settings.grid(row=5, column=0, padx=10, pady=10)

# Button to Clear text input
# Button with text saying Clear Text Input
# Button correlates to pdf_erase_text_input function
# Button is blue with white text
button_pdf_input_text_erase = Button(tab_pdf_converter, text='Clear Text Input', command=pdf_erase_text_input, width=30,
                                 bg='blue', fg='#fff')
# Create a grid for clearing text input
button_pdf_input_text_erase.grid(row=6, column=0, padx=10, pady=10)

# Button to Generate PDF File
# Button with text saying Generate PDF File
# Button correlates to pdf_text_to_pdf_file function
# Button is red with white text
button_pdf_text_process = Button(tab_pdf_converter, text='Generate PDF File', command=pdf_text_to_pdf_file, width=30,
                                 bg='red', fg='#fff')
# Create a grid for generating pdf file button
button_pdf_text_process.grid(row=7, column=0, padx=10, pady=10)

# Button that will execute the chatbot_erase_output function
button_chatot_erase_output = Button(tab_chatbot, text='Clear Output', command=chatbot_erase_output, width=30, bg='blue',
                                    fg='#fff')
# Create a grid for the button_chatot_erase_output
button_chatot_erase_output.grid(row=4, column=0, padx=10, pady=10)

# Button that will execute the chatbot_text_process function
button_chatbot_text_process = Button(tab_chatbot, text='Send Text', command=chatbot_text_process, width=30, bg='red',
                                     fg='#fff')
# Create a grid for the button_chatbot_text_process
button_chatbot_text_process.grid(row=3, column=0, padx=10, pady=10)


# Output displaying the results gathered from the AI Text Summary
# Create a scroll bar for the output display box
# WORD wrap to organize the text to not be cutoff.
summary_output_display = ScrolledText(tab_summarize, wrap=WORD)
# Create a grid for the output display box
summary_output_display.grid(row=8, column=0, columnspan=3, padx=5, pady=5)

# Create a scroll bar for the output display box
# WORD wrap to organize the text to not be cutoff.
wikipedia_output_display = ScrolledText(tab_wikipedia_search, wrap=WORD)
# Create a grid for the output display box
wikipedia_output_display.grid(row=11, column=0, columnspan=3, padx=5, pady=5)

# Create a scroll bar output display box
# WORD wrap to organize the text to not be cutoff.
verbal_output_display = ScrolledText(tab_verbal_presentation, wrap=WORD)
# Create a grid for the output display box
verbal_output_display.grid(row=9, column=0, padx=10, pady=10)

# Create a scroll bar output display box
# WORD wrap to organize the text to not be cutoff.
verbal_output_display_2 = ScrolledText(tab_verbal_presentation_2, wrap=WORD)
# Create a grid for the output display box
verbal_output_display_2.grid(row=7, column=0, padx=10, pady=10)

# Create a scroll bar output display box for the chatbot (text log)
chatbot_output_display = ScrolledText(tab_chatbot, wrap=WORD)
# Create a grid for the chatbot_output_display ScrolledText
chatbot_output_display.grid(row=5, column=0, padx=10, pady=10)

# Keep window alive
window.mainloop()
