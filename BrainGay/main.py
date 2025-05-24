# main.py
import engine
import games.nok as nok
import games.geometric_progression as gp

def main():
    print("Select a game to play:\n1. GCD (НОК)\n2. Geometric Progression")
    choice = input("Enter 1 or 2: ").strip()
    if choice == '1':
        engine.run_game(nok)
    elif choice == '2':
        engine.run_game(gp)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()