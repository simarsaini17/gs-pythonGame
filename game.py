from stringDatabase import frequency_dict

class Game:
    '''
    A Game class is used to calculate game score

    Attributes:
        score(int): store each game score
        badguess(int): number of times user guess the incorrect word
        missedletters(int): number of times user guess the incorrect letter
        status(str): status of the game
        answer(str): store random word each time it is generated
        covered_letters[](str): store covered letters of the word

    Methods:
        letter_guesss(guessed_letter): calculate the score when user guess the letter
        word_guess(guessed_word): calculate the score when user guess the whole word
        show_word(): calculate the score when your ask to show the word

    '''

    score=0
    sum=0
    badguess=0
    missedletter=0
    status="Success"
    answer=""
    covered_letters=[]

    def __init__(self, randomword):
        '''
        :param randomword: store randomly generated word
        '''
        self.answer = randomword


    def letter_guess(self, guessed_letter):
        '''
        Calculate the score when user guesses the letter

        :param guessed_letter: The letter that user guessed

        :return: return nothing
        '''

        if guessed_letter not in self.answer:
            self.score = self.score-5.0
            self.missedletter = self.missedletter + 1
        else:
            self.covered_letters.append(guessed_letter)
            current_score = frequency_dict[guessed_letter]
            self.score = (self.score + current_score)



    def word_guess(self, guessed_word):
        '''
        Calulate the score when user guesses a word

        :param guessed_word: The word that user guessed

        :return: return nothing

        '''

        if guessed_word == self.answer:
            for words in self.answer:
                    self.score = self.score + frequency_dict[words]


        else:
            self.badguess=self.badguess+1
            self.score = self.score-8.0

    def show_word(self):
        '''
        Calculate the score when user gave up

        :return: return nothing

        '''

        for ch in self.answer:
            if ch not in self.covered_letters:
                self.score = self.score - frequency_dict[ch]


        self.status="Gave up"













































