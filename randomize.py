import sublime, sublime_plugin
import random, re

class RandomizeCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        selection = self.view.sel()
        for region in selection:
            region_text = self.view.substr(region)
            randomized_text = self.randomize_text(region_text)
            self.view.replace(edit, region, randomized_text)

    def is_enabled(self):
        return len(self.view.sel()) > 0

    def randomize_text(self, text):
        number_re = re.compile('\d')
        alpha_capital_re = re.compile('[A-Z]')
        alpha_lower_case_re = re.compile('[a-z]')

        randomized_chars = []
        skip_next = False
        for i in range(len(text)):
            char = text[i]
            if skip_next:
                randomized_chars.append(char)
                skip_next = False
            elif char == '\\':
                # Let's leave escaped characters as they are.
                randomized_chars.append(char)
                skip_next = True
            elif number_re.match(char):
                randomized_chars.append(str(random.randint(0, 9)))
            elif alpha_capital_re.match(char):
                randomized_chars.append(chr(random.randint(65, 90)))
            elif alpha_lower_case_re.match(char):
                randomized_chars.append(chr(random.randint(97, 122)))
            else:
                # This works, but might be a little too much.
                # randomized_chars.append(self.random_special_char())
                randomized_chars.append(char)

        return ''.join(randomized_chars)

    def random_special_char(self):
        range = [
          [33, 47],
          [58, 64],
          [91, 96],
          [123, 126]
        ][random.randint(0, 3)]

        return chr(random.randint(range[0], range[1]))
