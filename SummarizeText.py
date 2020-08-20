# Class for SummarizeText
# Class doing the behind the scenes in actually generating a summary
class SummarizeText:
    # Utilizing sumy text summary library
    # Function utilizing the Lexrank text summarizer library
    # Atttributes within the function include parser_configuration and number_of_lines_to_output
    def lex_rank_analysis(self, parser_configuration, number_of_lines_to_output):
        # Using LexRank
        # Lexrank = Based of the idea that sentences recommend other similar sentences
        from sumy.summarizers.lex_rank import LexRankSummarizer
        # Variable correlating to the LexRankSummarizer Library
        summarizer = LexRankSummarizer()
        # Summarize the text and output n sentences
        # Parsering the text essentially breaks down the text given into smaller parts
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        # For Debug console
        # Print out the results through console
        print("\nBegin Raw summary from LexRank\n")
        # for each sentence gathered in the summarization_result have it printed out.
        for sentence in summarization_result:
            # Print out the sentences
            print(sentence)
        print("\nEnd Raw summary from LexRank\n")
        # Return text summary Result from Lexrank
        return summarization_result

    # Utilizing sumy text summary library
    # Function utilizing the LSA text summarizer library
    # Atttributes within the function include parser_configuration and number_of_lines_to_output
    def lsa_analysis(self, parser_configuration, number_of_lines_to_output):
        # Using LSA
        # LSA = Based on term frequency techniques
        from sumy.summarizers.lsa import LsaSummarizer
        # Variable correlating to the LSASummarizer Library
        summarizer = LsaSummarizer()
        # Summarize the text and output n sentences
        # Parsering the text essentially breaks down the text given into smaller parts
        summarization_result = summarizer(parser_configuration.document, number_of_lines_to_output)
        # For Debug console
        # Print out the results through console
        print("\nBegin Raw summary from LSA\n")
        # for each sentence gathered in the summarization_result have it printed out.
        for sentence in summarization_result:
            # Print out the sentences
            print(sentence)
        print("\nEnd Raw summary from LSA\n")
        # Return text summary Result from LSA
        return summarization_result
