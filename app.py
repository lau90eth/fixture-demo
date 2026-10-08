def parse(text):
    return [line.strip() for line in text.splitlines() if line.strip()]

if __name__ == "__main__":
    print("parser ok")
