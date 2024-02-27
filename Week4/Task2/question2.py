import os

class Filewriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.delete_file = False

    def __enter__(self):
        self.file = open(self.filename, 'w')
        return self

    def write(self, text):
        self.file.write(text)

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        if exc_type is not None or self.delete_file:
            os.remove(self.filename)

    def check_for_bug(self, text):
        if 'bug' in text:
            self.delete_file = True


filename = input("Enter the filename: ")

try:
    with Filewriter(filename) as writer:
        lines = []
        print("Enter text. Type 'done' on a new line to finish.")
        while True:
            line = input()
            if line.strip().lower() == 'done':
                break
            lines.append(line + '\n')
        writer.write(''.join(lines))
        writer.check_for_bug(''.join(lines))
except Exception as e:
    print("An error occurred:", e)
