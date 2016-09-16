import string
import operator

def read_entire_file(file_name):
	with open(file_name) as my_file:
	    output = my_file.read().decode("utf-8-sig").encode("utf-8")
	return output


def clean_up_file(output):
	clean_list = []

	for word in output.split(" "):
		clean_list.append(word.lower().strip(string.punctuation))
	return clean_list


def make_dict(string):
	word_dict = {}

	for word in string:
		if word not in word_dict:
			word_dict[word] = 1
		elif word in word_dict:
			word_dict[word] += 1
	return word_dict


def write_to_file(word_dictionary):
	convert_to_list = word_dictionary.items()
	convert_to_list.sort()
	second_list = sorted(convert_to_list, key = operator.itemgetter(1))
	with open("sorted_words.txt", mode = 'w') as my_file:
		my_file.write(str(convert_to_list))
		my_file.write("\n")
		my_file.write(str(second_list))


def main():
	code_app_file = read_entire_file("LoremIpsum.txt")
	clean_list = clean_up_file(code_app_file)
	word_dict_unsorted = make_dict(clean_list)
	write_to_file(word_dict_unsorted)


if __name__ == '__main__':
	main()