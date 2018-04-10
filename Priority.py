import random

def output(input):
	
	list1 = ["shower", "breakfast", "lunch", "dinner", "brunch", "work", "homework", "assignment", "paper", "proj", "wrk", "workbook", "reading", "hw", "read", "exam", "quiz", "interview"]
	list2 = ["class", "study", "review", "brainstorm", "draft", "laundry", "errands", "finish", "groceries", "food", "meet", "attend", "exercise", "gym", "email", "research", "start",]
	list3 = ["coffee", "practice", "rehearse", "reply", "call", "print", "clean room", "atm", "money", "cash", "resume"]
	list4 = ["arrange", "plan", "organize", "rent"]
	list5 = ["talk", "chat", "order", "go to the party", "date", "watch", "Netflix", "shop", "YouTube"]
	default_list = ["1. Hydrate yourself, hun.", "1. Eat!", "1. Have you taken a shower in the last 24 hours?", "2. Are you low on underwear? Do laundry.", "2. Channel your inner Beyonce and go work out.", "4. Clean your room?", "5. Get some down time."]

	messages = []

	found1 = False
	for word1 in list1:	
		if word1 in input:
			messages.append("1. " + word1.capitalize() + ".")
			found1 = True
			break

	if not found1:
		messages.append(default_list[random.randint(0, 2)])

	found2 = False
	for word2 in list2:
		if word2 in input:
			messages.append("2. " + word2.capitalize() + ".")
			found2 = True
			break
	
	if not found2:
		messages.append(default_list[random.randint(3, 4)])

	found3 = False
	for word3 in list3:
		if word3 in input:
			messages.append("3. " + word3.capitalize() + ".")
			found3 = True
			break
	
	if not found3:
		messages.append("3. Make sure to eat!")

	found4 = False
	for word4 in list4:
		if word4 in input:
			messages.append("4. " + word4.capitalize() + ".")
			found4 = True
			break
	
	if not found4:
		messages.append(default_list[5])
	
	found5 = False				
	for word5 in list5:
		if word5 in input:
			messages.append("5. "+ word5.capitalize() + ".")
			found5 = True
			break
	if not found5:
		messages.append(default_list[6])
	return messages
			

def main():
	input = "Take a shower Rent books Call your mom Do laundry"
	input = input.lower()
	output(input)

if __name__ == '__main__':
	main()