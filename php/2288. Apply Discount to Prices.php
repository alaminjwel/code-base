class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        words = sentence.split(' ')
        for i in range(len(words)):
            length = len(words[i])
            if (length > 1 and words[i][0] == '$' and words[i][-1].isdigit()):
                price = words[i][1:length]
                if (not price.isdigit()):
                    continue
                price = float(price) - ((float(price) * discount) / 100)
                words[i] = '$' + str("{:.2f}".format(price))
        return " ".join(words)