# Scrabble scoring system

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Create a dictionary to map letters to their corresponding points
letter_to_points = {letter: point for letter, point in zip(letters,points)}
print(letter_to_points)

# Add a point value for the blank space 
letter_to_points[" "] = 0

# Convert all letters to lowercase and map them to the same points
for letter in letters:
    letter_to_points[letter.lower()] = letter_to_points[letter]

# Function to calculate the score of a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letter_to_points.get(letter, 0)
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

# Dictionary to hold players and their words
player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT"], 
  "wordNerd": ["EARTH", "EYES", "MACHINE"],
  "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
  "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

player_to_points = {}

# Function to update the total points for each player
def update_point_totals():
  player_to_points.clear()
  for player, words in player_to_words.items():
    player_points = 0
    for word in words:
      player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)

# Extras

# Function to get the highest scoring player
def play_word(player, word):
  if player in player_to_words:
    player_to_words[player].append(word)
  else:
    player_to_words[player] = [word]

# Function to get the highest scoring player
play_word("player1", "PYTHON")
print(player_to_words["player1"])

# Testing lowercase functionality
print(score_word("Python")) 