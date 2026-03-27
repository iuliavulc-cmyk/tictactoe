
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ui.app import App

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
