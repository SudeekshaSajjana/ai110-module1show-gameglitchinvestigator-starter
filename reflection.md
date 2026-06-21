# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The game interface looked put together. It also seemed like it would work if you put in the guesses. Overall, the game seemed like it could work properly with no bugs. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1) Sometimes, it would give the wrong hints. For example, it would say to go higher when it was actually supposed to tell me to go lower.
  2) When I used a number that was outside of the bounds of 1-100, it wouldn't give me an error or tell me to pick a number within the bounds.


**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Pressed "New Game"|New game starts |New game doesn't start | Logic Error |
| guess of 25|"Too low" hint |"Too high" hint | Logic Error |
| guess of 101|"out of bounds" message |"Too high" hint | Logic Error |
|easy mode | bounds of 1-25| outside of this bound| logic error |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used Claude Code for this project to help me fix and refactor the code. Claude helped me with most of the coding aspects of this project. At times, I used ChatGPT if I needed clarification on certain things.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One AI suggestion that it gave was to switch the hint messages in the code so that the right hint message would show up depending on the number. I verified it by making sure that error existed in the code. This was to also see if AI was fixing it correctly.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One AI suggestion that was misleading was when it said that it fixed the bug with the incorrect hints. However, the bug wasn't fixed and stayed almost similar to before. I verified this by opening up the glitch game to test it out and the same error was still occuring. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided if a big was really fixed by first checking the code to see if the fix makes sense. Then, I ran the pytest to see if the tests worked. Lastly, I opened up the glitch game again to test if the fix was truly made.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

Two of the tests I ran with pytest are test_guess_too_high and test_guess_too_low. Before the fixes, these tests didn't output the assert statement since the tests didn't pass. After the bugs were fixed, the pytests outputted the assert statements, making the tests work and be true.

- Did AI help you design or understand any tests? How?

AI helped me understand how these tests work. This was by explaining what each test was testing when I asked it to explain it to me. AI also wrote the pytest to add additional tests that were neccessary with the new fixes.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

A rerun is Streamlit re-executing your entire script after every user interaction, and session state is the mechanism that lets your app remember information across those reruns.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.

One strategy I want to reuse is asking AI to explain the bugs that were occuring in the code. This is so that I have a better understanding about what the issue is and how to approach fixing it.

- What is one thing you would do differently next time you work with AI on a coding task?

One thing I would do differently is I would try to figure out how to fix it on my own before confiding in AI to do it. This is important so I can still understand the logic behind the fix.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project made me realize that AI generated code is not always accurate and can make mistakes that humans have to fix.