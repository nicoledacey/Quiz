import QuestionsND
question1 = QuestionsND.Questions("In what country would you find the mouths of the river Rhine?",4,["Holland","England","Norway","The Netherlands"])
question2 = QuestionsND.Questions("What US state's civil law is most closely based on the Napoleonic Code?",2,["Massachusetts","Louisiana","Texas","Kansas"])
question3 = QuestionsND.Questions("What metal is also known as quicksilver?",3,["Gallium","Silver","Mercury","Bismuth"])
question4 = QuestionsND.Questions("What US State was the first to host the Olympics?",2,["North Carolina","Missouri","California","New York"])
question5 = QuestionsND.Questions("What breed of dog's evidence is admissible in court?",1,["Bloodhound","German Shepherd","Labrador Retriever","St Bernard"])
question6 = QuestionsND.Questions("How many legs does a butterfly have?",3,["8","4","6","2"])
question7 = QuestionsND.Questions("What is the first plant to grow back after a fire?",1,["Moss","Weeds","Tree","Bush"])
question8 = QuestionsND.Questions("What country produces 2/3 of the world's vanilla",4,["Indonesia","Guatemala","Mexico","Madagascar"])
question9 = QuestionsND.Questions("What is the longest river in the world?",3,["Congo","Nile","Amazon","Yangtze"])
question10 = QuestionsND.Questions("What is the smallest country?",1,["Vatican","Monaco","Nauru","Liechtenstein"])
question_storage = [question1,question2,question3,question4,question5,question6,question7,question8,question9,question10]

player1_score = 0
player2_score = 0
counter = 0
print("Let's play some trivia! Remember no googling!")

for i in question_storage:
    print("Question",(counter+1),": ",i)

    try:
        choice = input("Please enter your choice: 1-4 ")
            #if len(choice) == 0:
    except SyntaxError:
        print("{0} You did not enter anything!".format(choice))
                #if type(choice) != type(int):
    except ValueError:
        print("{0} is not an int".format(choice))
#                    if choice.isnumeric() == False:
    except ValueError:
        print("{0} is not a choice".format(choice))
                        #if int(choice) < 0:
    except ValueError:
        print("{0} is not a positive choice".format(choice))
        pass

    if(QuestionsND.Questions.get_answer(i,int(choice)) == True):
        print("Correct!")
        if(counter % 2 == 0):
            player1_score += 1
            print("Player 1's score: ",player1_score)
        else:
            player2_score += 1
            print("Player 2's score: ",player2_score)
    else:
        print("That was incorrect. The correct answer was: ",QuestionsND.Questions.answer(i))
    counter += 1
if(player1_score > player2_score):
    print("Player 1 won with a score of: ",player1_score)
    print("Player 2 had: ", player2_score)
else:
    if(player2_score > player1_score):
        print("Player 2 won with a score of: ",player2_score)
        print("Player 1 had: ", player1_score)
    else:
        if(player1_score == player2_score):
              print("It was a tie! Player 1's score: ",player1_score,"Player 2's scoure: ",player2_score)
