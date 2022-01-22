valid_input_characters = "abcdefghijklmnopqrstuvwxyz_"
valid_characters = "abcdefghijklmnopqrstuvwxyz"

def main():
	positions, contains, not_contains = input_state()
	find_words(positions, contains, not_contains)

def find_words(positions, contains, not_contains):
	five_letter_words = open("five_letter_words.txt", "r")
	print("Possible words: ")
	for word in five_letter_words:
		has_wrong_position_letter = False
		for i, letter in enumerate(positions):
			if letter == "_":
				continue
			if word[i] != letter:
				has_wrong_position_letter = True
		if has_wrong_position_letter:
			continue

		missing_contains_letter = False
		for letter in contains:
			if letter not in word:
				missing_contains_letter = True
				break
		if missing_contains_letter:
			continue

		has_not_contains_letter = False
		for letter in word:
			if letter in not_contains:
				has_not_contains_letter = True
				break
		if has_not_contains_letter:
			continue

		print(word.strip())



def contains_invalid_characters(series, char_set):
	for letter in series:
		if letter not in char_set:
			print(f"Error: invalid character '{letter}'.")
			return True
	return False


def contains_dupes(series):
	counts = [0] * len(valid_characters)
	for letter in series:
		if letter == "_":
			continue
		counts[valid_characters.find(letter)] += 1
		if counts[valid_characters.find(letter)] > 1:
			print(f"Error: No duplicate characters '{letter}'.")
			return True
	return False


def no_overlap(contains, positions):
	for letter in contains:
		if letter in positions:
			print("Error: overlap between known positions and contains.")
			return False
	return True


def is_positions_valid(positions):
	if len(positions) != 5:
		print("Error: length is not 5 characters.")
		return False
	if contains_invalid_characters(positions, valid_input_characters):
		return False
	if contains_dupes(positions):
		return False
	return True


def is_contains_valid(contains):
	if len(contains) > 5:
		print("Error: length is over 5 characters")
		return False
	if contains_invalid_characters(contains, valid_characters):
		return False
	if contains_dupes(contains):
		return False
	return True


def is_not_contains_valid(not_contains):
	if contains_invalid_characters(not_contains, valid_characters):
		return False
	if contains_dupes(not_contains):
		return False
	return True


def input_state():
	while True:
		positions = input("Enter known letters in position, _ for unknown letters: ").lower().strip()
		if is_positions_valid(positions):
			break

	while True:
		contains = input("Enter letters that are contained in the word: ").lower().strip()
		if is_contains_valid(contains) and no_overlap(contains, positions):
			break

	while True:
		not_contains = input("Enter letters that the word does not contain: ").lower().strip()
		if is_not_contains_valid(not_contains):
			break

	return positions, contains, not_contains


def process_words():
	five_letter_words = open("five_letter_words.txt", "w")
	all_words = open("words.txt", "r")
	for word in all_words:
		word = word.lower().strip()
		
		if len(word) != 5:
			continue
		if contains_invalid_characters(word, valid_characters):
			continue
		if contains_dupes(word):
			continue
		print(word)
		five_letter_words.write(word+"\n");
	five_letter_words.close()

		
if __name__ == "__main__":
	# process_words()
	main()
