A simple python script to convert plain text to braille in svg form.
The character set is Latvian.

## How to use

1. Clone or download this repository
2. Open a shell (terminal, command prompt, powershell) in the directory of the repository
3. Check if python is installed, by running this command:

   **Windows:**

   ```sh
   python --version
   ```

   **MacOS:**

   ```sh
   python3 --version
   ```

   You should see something like:

   ```sh
   python 3.10.4
   ```

   If you don't, download python from their website: [Python](https://www.python.org)

4. Install the nesserary python package, by running this command:

   **Windows:**

   ```sh
   pip install svgwrite
   ```

   **MacOS:**

   ```sh
   pip3 install svgwrite
   ```

5. Now run the script: (replace the text within the quotes):

   **Windows:**

   ```sh
   python ./text_to_braille_SVG.py "Your text here"
   ```

   **MacOS:**

   ```sh
   python3 ./text_to_braille_SVG.py "Your text here"
   ```
