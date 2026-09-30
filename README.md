# Password Guesser Game

A Python command-line deduction game in which players try to crack a randomly generated password using exact-match and misplaced-character feedback.

## Project overview

The game combines password-style character generation with Mastermind-like feedback. A player selects a difficulty level, submits guesses, optionally requests character-revealing hints, and earns a score for successful, efficient play. A session leaderboard records the best score for each player name.

## Features

- Three difficulty levels:
  - **Ezzy:** 4 lowercase letters and 10 attempts
  - **Mido:** 5 lowercase letters or digits and 8 attempts
  - **Hardango:** 6 uppercase/lowercase letters or digits and 6 attempts
- Feedback for exact matches and correct characters in the wrong position.
- Optional hints that reveal one hidden character and cost 15 points.
- Time-sensitive scoring with bonuses for difficulty, unused attempts, and quick completion.
- Session leaderboard showing each player's highest score.
- Rules screen and menu-driven terminal interface.
- Input validation for difficulty choices and guess length.

## Requirements

- Python 3.8 or newer
- A terminal that supports standard `input()` and console output
- No third-party packages

## How to run

From the project directory, run:

```bash
python "TANISHK PYTHON PROJECT VITYARTHI.py"
```

On Windows, this may also be:

```powershell
py -3 "TANISHK PYTHON PROJECT VITYARTHI.py"
```

Enter a player name, then choose an option from the main menu.

## How to play

1. Select **Play Game**.
2. Choose a difficulty level.
3. Enter a guess with the required number of characters.
4. Use the feedback to refine the next guess:
   - **Exact matches** are correct characters in the correct positions.
   - **Right character, wrong position** counts characters that exist in the password but are placed incorrectly.
5. Type `hint` to reveal one character. Each hint reduces the score by 15 points.
6. Type `quit` to leave the current round.
7. Crack the password before the attempts run out.

## Scoring

The score starts from this formula:

```text
(remaining attempts × 10) + (difficulty number × 20) − (hints × 15)
```

A 20-point speed bonus is added when the round lasts fewer than 30 seconds. The final score cannot be negative. The leaderboard updates only when the new score is higher than the player's previous score.

## Code structure

The project is contained in one Python file:

- `LVL` stores the difficulty configuration.
- `gen_pwd()` creates a random password and shuffles its characters.
- `chk_gss()` calculates exact and misplaced matches, including repeated characters.
- `show_pat()` displays revealed characters and underscores for hidden positions.
- `give_hint()` reveals a random unrevealed position.
- `calc_scr()` calculates the final score.
- `play_game()` runs one round.
- `show_rules()` and `show_leaderboard()` display supporting screens.
- `main()` controls the application menu.

## Design notes and limitations

- The leaderboard is stored in memory, so it is cleared when the program exits. The menu retains one player name for the entire run; it has no player-switch option.
- Hints reveal at most password length minus one positions and do not consume attempts.
- Guesses are case-sensitive, while commands are case-insensitive. Guess length is validated, but the allowed character set is not.
- A zero-point win is not recorded for a new player because leaderboard updates require a strictly higher score than the default zero.
- Scoring uses attempts remaining after the winning guess is deducted. Elapsed time includes input time and the 0.5-second checking delay per valid guess.
- Passwords are generated for gameplay and are not intended to be used as real credentials.
- The random generator is suitable for a game but is not a cryptographic password generator.
- In Easy mode, a generated password could theoretically equal the command word `hint` or `quit`; those values are treated as commands during input. A future version could reserve command words or use a separate input command format.
- Invalid guess lengths do not consume an attempt.
- The game reveals the password after a round ends without success.

## Possible future improvements

- Save leaderboards to JSON or SQLite.
- Add a configurable number of rounds and cumulative scores.
- Add color output and clearer visual feedback.
- Prevent reserved command words from being generated.
- Add automated tests for duplicate-character matching and scoring.
- Add a graphical interface or a web version.
- Use `secrets.choice()` if the project is extended to demonstrate security-oriented password generation.

## References and inspiration

- Python Standard Library documentation for [`random`](https://docs.python.org/3/library/random.html), [`string`](https://docs.python.org/3/library/string.html), and [`time`](https://docs.python.org/3/library/time.html).
- The feedback model resembles deduction games such as **Mastermind**, where exact positions and misplaced symbols provide clues. This is a conceptual comparison, not a verified account of the author's inspiration.
- The menu and score design follows common terminal game patterns used in beginner Python projects.

## Documentation and verification

See `Project_Report.pdf` for the project analysis, educational usefulness, reconstructed development stages, illustrative challenges, limitations, and references. `project_report.html` is the editable report source. Historical development stages and challenges are explicitly identified as inferred or illustrative.

Verification with Python 3.13.15 passed 16 assertions covering feedback, repeated characters, hint limits, score boundaries, generation, menu navigation, and a controlled winning round. The original game source was not modified.

## License

No license is currently specified for this project. Add a license file before redistributing the code.
