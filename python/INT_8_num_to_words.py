import re
NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fithteen", "sixteen", "seventeen", "eighteen", "nineteen"];
PREFFIX = {1000000000:"billion", 1000000: "million", 1000: "thousand", 100: "hundred", 90: "ninety", 80: "eighty", 70: "seventy", 60: "sixty", 50: "fifty", 40: "forty", 30: "thirty", 20: "twenty"}
def number_to_text(x):
    result = "";

    if x < len(NUMBERS):
        return NUMBERS[x];

    for number ,text in sorted(PREFFIX.items(), key=lambda x: x[0],reverse=True):
        if x >= number:
            q = int(x / number);
            x = x % number;

            if number >= 100:
                result += "{} {} ".format(number_to_text(q),text + "s" if q > 1 else text);
            else:
                result += "{}".format(text + "-" if x > 0 else text);

    if x > 0:
        result += number_to_text(x);

    return result;

def text_to_number(x):
    total = 0;
    mult = 0;
    nPREFFIX = {y:x for x, y in PREFFIX.items()};

    for word in x.replace('-', ' ').replace(',', ' ').split(' '):
        if word in NUMBERS:
            mult = NUMBERS.index(word);
        else:
            if word[-1] == "s":
                word = word[0:-1];

            if word in nPREFFIX:
                total += nPREFFIX[word] if mult < 1 else nPREFFIX[word] * mult;
                mult = 0;

    return total + mult;

if __name__ == '__main__':
    x = input("Number? ");

    if x.isnumeric():
        print(number_to_text(int(x)));
    elif re.match("^[a-zA-Z\- ]+$", x):
        print(text_to_number(x));
    else:
        print("Not a valid number");
