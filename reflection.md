# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
    The game looked pretty intuitive. I noticed that it was a number guessing game and it had different modes on the side as well as ranges and attempts allowed. There was also a developer debug info page that helped with understanding what's going on under the hood. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - The hints were not accurate and allows the player to guess beyond the limit. For example, the secret number would be 96 but when guessing 100 it would tell me to "Go HIGHER"
    - New Game button only changes 'Secret' field and reverts 'Attempts' field back to 0. It doesn't erase the history from previous round.
    - The attempts allowed and ranges for each difficulty level doesn't match their corresponding difficulty level. 
      - Easy should have a range of 1-20 and attempts allowed should be 8. (Change attempts allowed from 6 to 8)
      - Normal should have a range of 1-50 and attempts allowed should be 6. (Change Range from 1-100 to 1-50 and attempts allowed from 8 to 6)
      - Hard should have a range of 1-100 and attempts allowed should be 5 (Change range from 1-50 to 1-100)
    - The Submitting Guess button doesn't record the number in history unless you press the button twice. Attempts made were inaccurate. I guessed 8 times on the hard difficulty but it only recorded 4 attempts.
    - On Difficulty setting Normal, when guessing numbers 1-10 and entering them using the Submit Guess button, the History only records 1 2 4 6 8 with an attempt of 5, when I pressed the Submit Guess button 10 times. --> Widget State Synchronization problem.
    - The first time playing the game/new game. In the first guess, when submitting "Submit Guess" the History isn't updated. It only updates after the second click of "Submit Guess."
    - The game states "Out of attempts! The secret was __. Score:0" when 1 attempt is still left.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  When Copilot suggested the new check_guess function, it included the new hint directions. I looked over what the AI suggested and verified it is correct by reading through its code line by line and playing the game to see if the hints were accurate. Also running the test cases in test_game_logic also helped verify the accuracy of the function.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  When Copilot suggested adding regression tests to test_game_logic.py for the reversed hint bug, it made 3 additional regression tests that were redundant. Not necessarily incorrect but redundant and isn't best practice. I prompted Copilot to merge the 3 existing test functions with the regression functions and remove the regression functions after reading the code. To fully understand the generated code, I asked Copilot to confirm my understanding of it. I verified the generated code by running the pytest command -- all 3 test cases were passed.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided a bug was really fixed by ensuring it ran smoothly in the game, generating test cases for it and seeing if the code passes the test cases, and reading over the code to ensure quality and peak performance. 
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  When running pytest it showed that all my test cases passed. "3 passed in 0.02s." Out of curiousity, I wanted to see how a failure looked like with pytest since this is my first time using it. So in test_winning_guess(), I changed 'assert outcome == "Win"' to 'assert outcome == "Winr"' and found that an AssertionError would occur if there was a failure. Through copilot's explaination, I discovered what the assert keyword does. "The assert keyword tests a condition and fails the program if it's false. It's essential for unit testing."
  Syntax: 
  assert condition, "optional error message"
- Did AI help you design or understand any tests? How?
  Copilot designed the test cases in test_game_logic.py. In one instance, it generated redundant regression tests which I told Copilot to remove. As this is my first time using pytest, I used Copilot to solidify my understanding of what pytest is and what the assert keyword means. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
