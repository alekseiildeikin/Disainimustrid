class Diary:
    def __init__(self):
        self.notes = []

    def add_entry(self, text):
        entry = f"{len(self.notes)+1}: {text}"
        self.notes.append(entry)

    def remove_entry(self, index):
        self.notes.pop(index)

    def save(self, filename):
        with open(filename, 'w') as f:
            for note in self.notes:
                f.write(note + "\n")

    def load(self, filename):
        with open(filename, 'r') as f:
            self.notes = [line.strip() for line in f]

    def print_statistics(self):
        count = len(self.notes)
        total_chars = sum(len(note) for note in self.notes)
        average = total_chars / count if count > 0 else 0
        print("Entries:", count)
        print("Average length:", average)

    def __str__(self):
        return "\n".join(self.notes)