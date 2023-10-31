from textblob import TextBlob
# from gingerit.gingerit import GingerIt
import language_tool_python


tool = language_tool_python.LanguageTool('en-US')


class SpellCheckerModule:
    def __init__(self):
        self.spell_check = TextBlob("")
        # self.grammer_check = GingerIt()
    def correct_spell(self, text):
        # words = text.split()
        # corrected_words = []
        # for word in words:
        #     corrected_word = str(TextBlob(word).correct())
        #     corrected_words.append(corrected_word)
        # return "".join(corrected_words)
        matches = tool.check(text)
        corrected_text = language_tool_python.correct(text, matches)
        print(corrected_text)

if __name__ == "__main__":
    obj = SpellCheckerModule()
    message = "Hello World, I like mashine learnna. appple"
    obj.correct_spell(message)