import random
import string
import time


LVL = {
    "1": ("Ezzy", 4, string.ascii_lowercase, 10),
    "2": ("Mido", 5, string.ascii_lowercase + string.digits, 8),
    "3": ("Hardango", 6, string.ascii_letters + string.digits, 6),
}

leaderboard = {}


def gen_pwd(length, chars):
    pwd = [random.choice(chars) for _ in range(length)]
    random.shuffle(pwd)
    return "".join(pwd)


def chk_gss(sec, gss):
    ex = sum(
        1 for a, b in zip(sec, gss)
        if a == b
    )

    tot = sum(
        min(sec.count(ch), gss.count(ch))
        for ch in set(gss)
    )

    mis = tot - ex

    return ex, mis


def show_pat(sec, rev):
    return " ".join(
        ch if i in rev else "_"
        for i, ch in enumerate(sec)
    )


def give_hint(sec, rev):
    hid = [
        i for i in range(len(sec))
        if i not in rev
    ]

    if len(hid) <= 1:
        return False

    rev.add(random.choice(hid))
    return True


def calc_scr(rem, hints, sec, lvl):
    scr = (rem * 10) + (int(lvl) * 20)

    scr -= hints * 15

    if sec < 30:
        scr += 20

    return max(scr, 0)


def chs_lvl():
    print("\nSelect Difficulty:")

    for key, (name, length, _, attempts) in LVL.items():
        print(f"  [{key}] {name} — {length} characters, {attempts} tries")

    ch = input("Option (1-3): ")

    while ch not in LVL:
        ch = input(
            "Invalid option. Please choose 1, 2, or 3: "
        )

    return ch


def play_game(pnm):
    lvl = chs_lvl()
    lvl_name, pwd_len, chars, max_att = LVL[lvl]

    sec = gen_pwd(pwd_len, chars)

    rev = set()
    hints = 0
    att_left = max_att

    st = time.time()

    print(f"{lvl_name.upper()} MODE")
    print(
        f"Guess the {pwd_len}-character password. "
        "Type 'hint' (-15 pts) or 'quit' to give up."
    )

    while att_left > 0:
        print(f"Password: {show_pat(sec, rev)}")
        print(f"Attempts remaining: {att_left}")

        gss = input("Enter guess: ")
        cmd = gss.lower()

        if cmd == "quit":
            break

        if cmd == "hint":
            if give_hint(sec, rev):
                hints += 1
                print("Hint used! One character has been revealed.")
            else:
                print("No additional hints are available!")

            continue

        if len(gss) != pwd_len:
            print(
                f"Your guess must be exactly "
                f"{pwd_len} characters long."
            )
            continue

        att_left -= 1

        print("Checking..")
        time.sleep(0.5)

        if gss == sec:
            dur = time.time() - st
            scr = calc_scr(
                att_left,
                hints,
                dur,
                lvl
            )

            print(
                f"Success! You cracked it in "
                f"{dur:.1f} seconds."
            )
            print(f"Score: {scr}")

            if scr > leaderboard.get(pnm, 0):
                leaderboard[pnm] = scr
                print("New high score!")

            return

        ex, mis = chk_gss(sec, gss)

        print(
            f"Exact matches: {ex} | "
            f"Right character, wrong position: {mis}"
        )

    print(f"Game Over The correct password was: {sec}")


def show_rules():
    print("\n" + "=" * 12 + " HOW TO PLAY " + "=" * 12)

    print("1.Figure out the secret password using the feedback.")
    print("2.Exact matches are characters in the correct position.")
    print("3.Misplaced matches are correct characters in the wrong position.")
    print("4.Type 'hint' to reveal a character, but it costs 15 points.")
    print("5.Faster guesses, fewer hints, and unused attempts give higher scores.")


def show_leaderboard():
    print("\n" + "=" * 12 + " LEADERBOARD " + "=" * 12)

    if not leaderboard:
        print("No high scores recorded yet. Play a game to set one!")
        return

    scores = sorted(
        leaderboard.items(),
        key=lambda item: item[1],
        reverse=True
    )

    for pos, (name, score) in enumerate(scores, start=1):
        print(f"{pos}. {name:<15} {score} pts")


def main():
    print("PASSWORD GUESSER GAME")
    
    pnm = input("Enter player name: ").strip() or "Player"

    while True:
        print(f"Main Menu ({pnm})")
        print("1.Play Game")
        print("2.Rules")
        print("3.Leaderboard")
        print("4.Exit")

        ch = input("Choice: ").strip()

        if ch == "1":
            play_game(pnm)

        elif ch == "2":
            show_rules()

        elif ch == "3":
            show_leaderboard()

        elif ch == "4":
            print("Thanks for playing! See you next time.")
            break

        else:
            print("Invalid input, please try again.")


if __name__ == "__main__":
    main()
